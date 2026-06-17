"""
org_tree_integration.py
═══════════════════════════════════════════════════════════════════════════════
Full OrgTree Integration for Digi Valet  (digi_valet_chat.py)
═══════════════════════════════════════════════════════════════════════════════

WHAT THIS FILE DOES
───────────────────
This file contains ALL the code changes needed to fully integrate org_tree.py
into digi_valet_chat.py.  It covers:

  1.  OrgTree import & safe fallback
  2.  Auto-load CSV from multiple search paths on startup
  3.  Enhanced /digivalet command handler (search, stats, lookup, fuzzy, dept, loc)
  4.  /digivalet reload  — hot-reload CSV without restarting the app
  5.  Org-tree context injected into the LLM system prompt
  6.  New quick-command button  "/digivalet"  in the toolbar
  7.  Sidebar org-tree status indicator
  8.  Natural-language org queries routed to OrgTree before hitting Ollama
  9.  Export org search results to CSV
 10.  Full department & location filter commands

HOW TO USE THIS FILE
────────────────────
Each section below is labelled with the EXACT location in digi_valet_chat.py
where the snippet belongs.  Search for the anchor comment shown above each
block and paste the new code right there.

No existing code needs to be deleted — every change is an addition or a
clean replacement of the one small function it supersedes.
═══════════════════════════════════════════════════════════════════════════════
"""


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  SECTION 1 — Import block (top of digi_valet_chat.py, after stdlib imports) ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
#
# ANCHOR: replace the existing try/except OrgTree import (lines ~36-41)
# ─────────────────────────────────────────────────────────────────────

SECTION_1_IMPORT = '''
# ── OrgTree import (safe fallback if org_tree.py is missing) ──────────────────
try:
    from org_tree import OrgTree
    _ORG_TREE_AVAILABLE = True
except ImportError:
    _ORG_TREE_AVAILABLE = False

    class OrgTree:                                      # minimal no-op shim
        loaded = False
        source_path = None

        def __init__(self, *a, **kw):
            pass

        def load_from_csv(self, *a) -> str:
            return "⚠️ org_tree.py not found — place it next to digi_valet_chat.py"

        def get_employee(self, *a):
            return None

        def search(self, *a, **kw):
            return []

        def list_by_department(self, *a, **kw):
            return []

        def list_by_location(self, *a, **kw):
            return []

        def stats(self):
            return {"total": 0, "departments": {}, "locations": {}}

        def to_context_snippet(self, *a, **kw):
            return ""

        @staticmethod
        def format_employee(info):
            return str(info)

        @staticmethod
        def format_results_table(results):
            return "No results."
'''


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  SECTION 2 — QUICK_COMMANDS dict  (add the new /digivalet entry)           ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
#
# ANCHOR: inside QUICK_COMMANDS dict, after the "/digivalet" key (line ~466)
# Replace the existing  "/digivalet"  entry with this:

SECTION_2_QUICK_COMMANDS_ENTRY = '''
    "/digivalet": (
        "Show me how to use the /digivalet org-chart lookup command "
        "(e.g. /digivalet Rahul Salgia, /digivalet QA, /digivalet Indore, "
        "/digivalet stats, /digivalet dept:Projects, /digivalet loc:Indore, "
        "/digivalet reload)."
    ),
'''


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  SECTION 3 — Natural-language org keywords                                 ║
# ║  Place this as a module-level constant near QUICK_COMMANDS                 ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

# Add this constant AFTER the QUICK_COMMANDS dict (around line ~471)

ORG_NL_TRIGGERS = [
    # "who is …" / "find … in the org"
    "who is ", "who's ", "look up ", "find employee", "search org",
    "show me the employee", "employee details", "employee info",
    # department / location queries
    "who works in ", "people in ", "list the ", "employees in ",
    "how many people in ", "show department", "show location",
    # reporting
    "how many reports", "direct reports", "reportees",
    # org stats
    "org stats", "org chart", "org tree", "organisation stats",
    "how many employees", "total employees", "headcount",
]
"""
These substrings, if found in a user message, cause _maybe_handle_org_query()
to intercept the message and answer from OrgTree before it reaches Ollama.
"""


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  SECTION 4 — DigiValetWindow.__init__  additions                           ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
#
# ANCHOR: inside DigiValetWindow.__init__, right after  self.org_tree = OrgTree()
# (around line ~2190).  ADD these lines immediately below that assignment:

SECTION_4_INIT_ADDITIONS = '''
        # ── Org tree: load CSV + expose status in the sidebar ────────────────
        self._org_csv_path: str | None = None          # track which file is loaded
        self._load_org_tree_csv()                       # auto-discover OrgTree.csv
'''


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  SECTION 5 — _load_org_tree_csv()  (FULL replacement)                     ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
#
# ANCHOR: replace the existing _load_org_tree_csv method (around line ~2193)

def _load_org_tree_csv(self):
    """
    Auto-discover OrgTree.csv from several candidate paths.

    Search order:
      1. Explicit --csv flag (stored in self._csv_arg, set by CLI parser)
      2. Same folder as digi_valet_chat.py
      3. Current working directory
      4. User's home directory  (~/.digi_valet_orgtree.csv  or  ~/OrgTree.csv)

    On success the loaded CSV path is stored in self._org_csv_path and a green
    status line is shown in the sidebar.  On failure a warning is printed.
    """
    import sys
    from pathlib import Path

    candidates = []

    # 1 — explicit CLI flag
    if hasattr(self, "_csv_arg") and self._csv_arg:
        candidates.append(Path(self._csv_arg))

    # 2 — next to the script
    script_dir = Path(sys.argv[0]).resolve().parent
    candidates += [
        script_dir / "OrgTree.csv",
        script_dir / "orgtree.csv",
        script_dir / "org_tree.csv",
    ]

    # 3 — current working directory
    cwd = Path.cwd()
    candidates += [
        cwd / "OrgTree.csv",
        cwd / "orgtree.csv",
    ]

    # 4 — home directory
    home = Path.home()
    candidates += [
        home / "OrgTree.csv",
        home / ".digi_valet_orgtree.csv",
    ]

    for path in candidates:
        if path.exists():
            msg = self.org_tree.load_from_csv(str(path))
            self._org_csv_path = str(path)
            print(msg)
            self._update_org_status()          # update sidebar label
            return

    print("ℹ️  OrgTree.csv not found — /digivalet will report 'not loaded' until you add one.")
    self._update_org_status()


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  SECTION 6 — _update_org_status()   NEW method                             ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
#
# ANCHOR: add this method right after _load_org_tree_csv() in DigiValetWindow

def _update_org_status(self):
    """Refresh the sidebar org-tree status label (if it exists)."""
    if not hasattr(self, "org_status_label"):
        return                                  # label not built yet — skip
    if self.org_tree.loaded:
        stats = self.org_tree.stats()
        from pathlib import Path
        fname = Path(self._org_csv_path).name if self._org_csv_path else "OrgTree.csv"
        self.org_status_label.setText(
            f"◈ Org: {stats['total']} employees  •  {fname}"
        )
        self.org_status_label.setStyleSheet("color: #6a9e6a; font-size: 9px; padding: 2px 0;")
    else:
        self.org_status_label.setText("◈ Org: not loaded  (add OrgTree.csv)")
        self.org_status_label.setStyleSheet("color: #8a6a4a; font-size: 9px; padding: 2px 0;")


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  SECTION 7 — Sidebar org-status label  (_build_sidebar addition)           ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
#
# ANCHOR: inside _build_sidebar(), AFTER  layout.addWidget(self.task_widget)
# (around line ~2421).  Paste the block below:

SECTION_7_SIDEBAR_LABEL = '''
        # ── Org Tree status line ──────────────────────────────────────────────
        layout.addSpacing(10)
        org_sec = QLabel("ORG TREE")
        org_sec.setObjectName("sectionLabel")
        org_sec.setFont(QFont("Georgia", 8))
        layout.addWidget(org_sec)
        layout.addSpacing(4)

        self.org_status_label = QLabel("◈ Org: initialising…")
        self.org_status_label.setFont(QFont("Georgia", 8))
        self.org_status_label.setWordWrap(True)
        layout.addWidget(self.org_status_label)

        # Reload-CSV button
        reload_org_btn = QPushButton("↺  Reload OrgTree.csv")
        reload_org_btn.setObjectName("clearBtn")
        reload_org_btn.setFont(QFont("Georgia", 9))
        reload_org_btn.setToolTip("Re-scan for OrgTree.csv and reload employee data")
        reload_org_btn.clicked.connect(self._reload_org_csv)
        layout.addWidget(reload_org_btn)
        layout.addSpacing(6)

        # Call _update_org_status now that the label exists
        self._update_org_status()
'''


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  SECTION 8 — _reload_org_csv()   NEW method                                ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
#
# ANCHOR: add this method right after _update_org_status()

def _reload_org_csv(self):
    """Hot-reload OrgTree.csv without restarting the app."""
    # If we know where the CSV lives, reload it directly
    if self._org_csv_path:
        from pathlib import Path
        if Path(self._org_csv_path).exists():
            msg = self.org_tree.load_from_csv(self._org_csv_path)
            self._update_org_status()
            self._add_system_notice(msg)
            return

    # Otherwise re-run auto-discovery
    self._load_org_tree_csv()
    if self.org_tree.loaded:
        self._add_system_notice(
            f"✅ Org tree reloaded — {self.org_tree.stats()['total']} employees"
        )
    else:
        self._add_system_notice("⚠️ Could not find OrgTree.csv — add it next to the app and try again.")


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  SECTION 9 — _handle_digivalet_command()   FULL REPLACEMENT                ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
#
# ANCHOR: replace the existing _handle_digivalet_command method (around line ~2829)

def _handle_digivalet_command(self, text: str) -> str:
    """
    Handle  /digivalet <query>  — answered locally from OrgTree, no LLM call.

    Supported sub-commands
    ──────────────────────
    /digivalet                      → help + top departments
    /digivalet help | ?             → same as above
    /digivalet stats                → full department + location breakdown
    /digivalet reload               → hot-reload OrgTree.csv
    /digivalet dept:<name>          → list all employees in a department
    /digivalet loc:<name>           → list all employees at a location
    /digivalet export               → export current search results to CSV
    /digivalet <emp_number>         → look up by employee number  (e.g. PD036)
    /digivalet <full name>          → look up by display name     (case-insensitive)
    /digivalet <keyword>            → fuzzy search across name/title/dept/location
    """
    import csv as _csv
    import os as _os
    from pathlib import Path as _Path

    query = text[len("/digivalet"):].strip()
    q_lower = query.lower()

    # ── Not loaded ────────────────────────────────────────────────────────────
    if not self.org_tree.loaded:
        return (
            "⚠️ **Org tree not loaded.**\n\n"
            "Place **OrgTree.csv** (columns: `Employee Number, Display Name, "
            "Job Title, Department, Location, Reportees Count`) "
            "next to `digi_valet_chat.py` and press **↺ Reload OrgTree.csv** "
            "in the sidebar — or use:\n\n"
            "```\n/digivalet reload\n```"
        )

    # ── reload ────────────────────────────────────────────────────────────────
    if q_lower == "reload":
        self._reload_org_csv()
        if self.org_tree.loaded:
            stats = self.org_tree.stats()
            return (
                f"✅ **Org tree reloaded** from `{_Path(self._org_csv_path).name}`\n\n"
                f"• **{stats['total']}** employees loaded\n"
                f"• **{len(stats['departments'])}** departments\n"
                f"• **{len(stats['locations'])}** locations"
            )
        return "⚠️ Reload failed — OrgTree.csv not found. See sidebar for details."

    # ── help / empty ─────────────────────────────────────────────────────────
    if not query or q_lower in ("help", "?"):
        stats = self.org_tree.stats()
        dept_lines = "\n".join(
            f"  • {d}: {c}" for d, c in list(stats["departments"].items())[:10]
        )
        loc_lines = "\n".join(
            f"  • {loc}: {c}" for loc, c in list(stats["locations"].items())[:6]
        )
        return (
            f"**◈ Digi Valet Org Lookup** — **{stats['total']} employees** loaded\n\n"
            "**Commands:**\n"
            "| Command | Example |\n"
            "|---|---|\n"
            "| `/digivalet <name>` | `/digivalet Rahul Salgia` |\n"
            "| `/digivalet <emp #>` | `/digivalet PB001` |\n"
            "| `/digivalet <keyword>` | `/digivalet QA` |\n"
            "| `/digivalet dept:<name>` | `/digivalet dept:Projects` |\n"
            "| `/digivalet loc:<name>` | `/digivalet loc:Indore` |\n"
            "| `/digivalet stats` | full breakdown |\n"
            "| `/digivalet reload` | reload CSV |\n"
            "| `/digivalet export` | save results to CSV |\n\n"
            f"**Top departments:**\n{dept_lines}\n\n"
            f"**Locations:**\n{loc_lines}"
        )

    # ── stats ─────────────────────────────────────────────────────────────────
    if q_lower == "stats":
        stats = self.org_tree.stats()
        dept_lines = "\n".join(f"| {d} | {c} |" for d, c in stats["departments"].items())
        loc_lines  = "\n".join(f"| {loc} | {c} |" for loc, c in stats["locations"].items())
        managers = sum(
            1 for e in self.org_tree.employees.values() if e.get("reports_count", 0) > 0
        )
        return (
            f"**◈ Org Tree Overview** — **{stats['total']} employees**\n\n"
            f"• Managers (with direct reports): **{managers}**\n"
            f"• Departments: **{len(stats['departments'])}**\n"
            f"• Locations: **{len(stats['locations'])}**\n\n"
            f"**By Department**\n\n| Department | Headcount |\n|---|---|\n{dept_lines}\n\n"
            f"**By Location**\n\n| Location | Headcount |\n|---|---|\n{loc_lines}"
        )

    # ── dept:<name> ───────────────────────────────────────────────────────────
    if q_lower.startswith("dept:"):
        dept_query = query[5:].strip()
        results = self.org_tree.list_by_department(dept_query)
        if not results:
            return f"No employees found in department matching **'{dept_query}'**."
        header = (
            f"**{len(results)} employee(s)** in department matching "
            f"**'{dept_query}'**:\n\n"
        )
        return header + self.org_tree.format_results_table(results)

    # ── loc:<name> ────────────────────────────────────────────────────────────
    if q_lower.startswith("loc:"):
        loc_query = query[4:].strip()
        results = self.org_tree.list_by_location(loc_query)
        if not results:
            return f"No employees found at location matching **'{loc_query}'**."
        header = (
            f"**{len(results)} employee(s)** at location matching "
            f"**'{loc_query}'**:\n\n"
        )
        return header + self.org_tree.format_results_table(results)

    # ── export ────────────────────────────────────────────────────────────────
    if q_lower == "export":
        # Export ALL employees to CSV in the user's home directory
        out_path = _Path.home() / "digi_valet_org_export.csv"
        try:
            with open(out_path, "w", newline="", encoding="utf-8") as f:
                writer = _csv.DictWriter(
                    f,
                    fieldnames=["emp_num", "name", "title", "dept", "location", "reports_count"],
                )
                writer.writeheader()
                for emp in self.org_tree.employees.values():
                    writer.writerow(emp)
            return (
                f"✅ **Org data exported** to:\n\n"
                f"`{out_path}`\n\n"
                f"**{len(self.org_tree.employees)}** employees written."
            )
        except Exception as exc:
            return f"❌ Export failed: {exc}"

    # ── Exact match on employee number or full name ───────────────────────────
    emp = self.org_tree.get_employee(query)
    if emp:
        # Show full profile including a mini-stat about their department
        dept_count = sum(
            1 for e in self.org_tree.employees.values()
            if e["dept"].lower() == emp["dept"].lower()
        )
        profile = self.org_tree.format_employee(emp)
        profile += f"\n• Colleagues in same dept: {dept_count - 1}"
        return profile

    # ── Fuzzy search across name / title / dept / location ───────────────────
    results = self.org_tree.search(query, limit=30)
    if not results:
        # Last resort: try partial department match
        dept_results = self.org_tree.list_by_department(query, limit=30)
        if dept_results:
            return (
                f"**{len(dept_results)} employee(s)** in departments matching "
                f"**'{query}'**:\n\n"
                + self.org_tree.format_results_table(dept_results)
            )
        # Try partial location match
        loc_results = self.org_tree.list_by_location(query, limit=30)
        if loc_results:
            return (
                f"**{len(loc_results)} employee(s)** at locations matching "
                f"**'{query}'**:\n\n"
                + self.org_tree.format_results_table(loc_results)
            )
        return (
            f"No matches found in the org tree for **'{query}'**.\n\n"
            "Try `/digivalet stats` to browse departments, "
            "or `/digivalet help` for usage."
        )

    header = f"Found **{len(results)} match(es)** for **'{query}'**:\n\n"
    return header + self.org_tree.format_results_table(results)


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  SECTION 10 — _maybe_handle_org_query()   NEW method                       ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
#
# ANCHOR: add this method right after _handle_digivalet_command()
# It intercepts plain-English org questions before they reach Ollama.

def _maybe_handle_org_query(self, text: str) -> str | None:
    """
    If 'text' looks like a natural-language org question AND the org tree is
    loaded, answer directly from OrgTree and return the markdown string.

    Returns None if the question should be forwarded to Ollama normally.

    Examples intercepted:
      "who is Rahul Salgia?"             → employee profile
      "who works in the QA department?"  → department listing
      "how many employees are in Indore?" → location count
      "show me org stats"                → stats table
      "people in Projects"               → department listing
    """
    if not self.org_tree.loaded:
        return None

    t = text.lower().strip()

    # Bail on very short or obviously non-org messages
    if len(t) < 8:
        return None

    # Check against known trigger phrases
    triggered = any(phrase in t for phrase in ORG_NL_TRIGGERS)
    if not triggered:
        return None

    # ── "org stats" / "headcount" ─────────────────────────────────────────
    if any(kw in t for kw in ("org stats", "total employees", "how many employees", "headcount")):
        return self._handle_digivalet_command("/digivalet stats")

    # ── "who is <name>" ───────────────────────────────────────────────────
    for prefix in ("who is ", "who's ", "look up ", "find employee ", "show me the employee "):
        if prefix in t:
            idx = t.index(prefix) + len(prefix)
            candidate = text[idx:].strip().rstrip("?.,!")
            emp = self.org_tree.get_employee(candidate)
            if emp:
                return self.org_tree.format_employee(emp)
            # Try search
            results = self.org_tree.search(candidate, limit=10)
            if results:
                return (
                    f"Found **{len(results)}** match(es) for **'{candidate}'**:\n\n"
                    + self.org_tree.format_results_table(results)
                )

    # ── "people in / who works in / employees in <place>" ─────────────────
    for prefix in ("who works in ", "people in ", "employees in ",
                   "how many people in ", "list the "):
        if prefix in t:
            idx = t.index(prefix) + len(prefix)
            place = text[idx:].strip().rstrip("?.,!")
            dept_results = self.org_tree.list_by_department(place, limit=40)
            loc_results  = self.org_tree.list_by_location(place, limit=40)
            if dept_results or loc_results:
                parts = []
                if dept_results:
                    parts.append(
                        f"**{len(dept_results)}** employee(s) in dept **'{place}'**:\n\n"
                        + self.org_tree.format_results_table(dept_results)
                    )
                if loc_results:
                    parts.append(
                        f"**{len(loc_results)}** employee(s) at location **'{place}'**:\n\n"
                        + self.org_tree.format_results_table(loc_results)
                    )
                return "\n\n".join(parts)

    # ── "direct reports" / "reportees" ────────────────────────────────────
    if any(kw in t for kw in ("direct reports", "reportees", "how many reports")):
        managers = [
            e for e in self.org_tree.employees.values()
            if e.get("reports_count", 0) > 0
        ]
        managers.sort(key=lambda x: -x["reports_count"])
        if not managers:
            return "No employees with direct reports found in the org tree."
        lines = ["**Employees with direct reports:**\n",
                 "| Name | Title | Dept | Location | Reports |",
                 "|---|---|---|---|---|"]
        for m in managers[:20]:
            lines.append(
                f"| {m['name']} | {m['title']} | {m['dept']} "
                f"| {m['location']} | {m['reports_count']} |"
            )
        return "\n".join(lines)

    # Nothing matched precisely — let Ollama handle it
    return None


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  SECTION 11 — Inject org context into system prompt                        ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
#
# ANCHOR: inside build_system_prompt() (around line ~474), AFTER the kb block.
# Replace the existing function with this version:

def build_system_prompt(tone: str = "balanced", language: str = "English",
                        kb=None, org_tree=None) -> str:
    """
    Build the Ollama system prompt.

    Parameters
    ──────────
    tone      : "formal" | "balanced" | "casual"
    language  : one of LANGUAGE_ADDONS keys
    kb        : KnowledgeBase instance (optional)
    org_tree  : OrgTree instance (optional) — injects a compact employee list
    """
    from digi_valet_chat import BASE_PERSONALITY, LANGUAGE_ADDONS  # adjust import if needed

    base  = BASE_PERSONALITY.get(tone, BASE_PERSONALITY["balanced"])
    addon = LANGUAGE_ADDONS.get(language, "")
    prompt = base + ("\n" + addon if addon else "")

    # ── Inject knowledge base ─────────────────────────────────────────────
    if kb is not None and not kb.is_empty():
        prompt += "\n\n" + kb.system_prompt_block()

    # ── Inject org tree (compact — max 200 rows) ──────────────────────────
    if org_tree is not None and org_tree.loaded:
        snippet = org_tree.to_context_snippet(max_rows=200)
        if snippet:
            prompt += (
                "\n\n"
                "# Employee Directory (use this to answer org-chart questions)\n"
                + snippet
            )

    return prompt


# NOTE: Inside DigiValetWindow._get_system_prompt() and _refresh_system_prompt(),
# change the call from:
#
#   build_system_prompt(tone, language, kb=self.kb)
#
# to:
#
#   build_system_prompt(tone, language, kb=self.kb, org_tree=self.org_tree)
#
# This passes the loaded org tree into every LLM context window so Ollama can
# also answer org questions even without a /digivalet command.


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  SECTION 12 — Natural-language interception in _send_message()             ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
#
# ANCHOR: inside _send_message(), right AFTER the /digivalet block
# (after line ~3038).  Add the following block:

SECTION_12_NL_INTERCEPT = '''
        # ── Natural-language org query: answer locally if possible ───────────
        nl_answer = self._maybe_handle_org_query(text)
        if nl_answer is not None:
            self.input_box.clear()
            user_bubble = MessageBubble(text, "user")
            self.chat_layout.insertWidget(self.chat_layout.count() - 1, user_bubble)
            reply_bubble = MessageBubble(nl_answer, "assistant")
            self.chat_layout.insertWidget(self.chat_layout.count() - 1, reply_bubble)
            self._scroll_to_bottom()
            self.messages.append({"role": "user",      "content": text})
            self.messages.append({"role": "assistant", "content": nl_answer})
            self.all_chats[self.current_chat_id]["messages"] = self.messages
            self._populate_sidebar_list()
            if not self.privacy_mode:
                self._save_all_chats()
            return
'''


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  SECTION 13 — /digivalet quick-command toolbar button                      ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
#
# ANCHOR: inside _build_chat_area() (or wherever the quick-command buttons are
# added, around line ~2550).  The existing code already has a /digivalet button;
# if it doesn't, paste the snippet below right after the other cmd_btn widgets:

SECTION_13_TOOLBAR_BUTTON = '''
        dv_btn = QPushButton("/digivalet")
        dv_btn.setObjectName("cmdBtn")
        dv_btn.setFont(QFont("Georgia", 9))
        dv_btn.setToolTip(
            "Org chart lookup — /digivalet <name|keyword|stats|dept:…|loc:…|reload>"
        )
        dv_btn.setCursor(Qt.PointingHandCursor)
        dv_btn.clicked.connect(lambda: self._run_quick_command("/digivalet"))
        cmd_row.addWidget(dv_btn)
'''


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  SECTION 14 — _run_quick_command()  small tweak                            ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
#
# ANCHOR: inside _run_quick_command(), replace the existing /digivalet block
# (around line ~2813) with:

SECTION_14_QUICK_CMD = '''
        if cmd == "/digivalet":
            if self.org_tree.loaded:
                stats = self.org_tree.stats()
                # Show help with live employee count
                self.input_box.setPlainText("/digivalet help")
            else:
                self.input_box.setPlainText("/digivalet help")
            self._send_message()
            return
'''


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  SECTION 15 — requirements.txt addition                                    ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
#
# No extra pip packages are needed — org_tree.py uses only the stdlib (csv,
# pathlib, typing).  Your existing requirements.txt is sufficient:
#
#   PySide6>=6.4.0
#
# If you also want fuzzy name matching (not included above), add:
#   thefuzz>=0.20.0
# and in org_tree.py replace the search() method with a fuzzy variant using:
#   from thefuzz import fuzz
#   fuzz.partial_ratio(q, haystack) >= 70


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  QUICK-REFERENCE: full list of /digivalet sub-commands after this patch    ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
"""
/digivalet                        — help + top depts
/digivalet help                   — same
/digivalet stats                  — full dept + location table
/digivalet reload                 — hot-reload OrgTree.csv
/digivalet export                 — export all employees to ~/digi_valet_org_export.csv
/digivalet dept:Projects          — list everyone in the Projects dept
/digivalet loc:Indore             — list everyone in Indore
/digivalet PD036                  — employee profile by emp number
/digivalet Anil Dhanotiya         — employee profile by name
/digivalet QA                     — fuzzy search keyword across all fields
/digivalet Regional Lead          — search by job title keyword

Natural-language (no /digivalet needed):
  "who is Anil Dhanotiya?"
  "who works in QA?"
  "how many employees are in Indore?"
  "show org stats"
  "who has direct reports?"
"""