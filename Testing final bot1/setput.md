# Digi Valet — Desktop Setup Guide
_Native PyQt6 app · Works on Windows, macOS, Linux_

---

## Your files

Put all three files in the **same folder**:

```
📁 DigiValet/
  ├── digi_valet_chat_enhanced.py   ← backend (the one you already had)
  ├── digi_valet_desktop.py         ← NEW native launcher  ← run this
  ├── requirements.txt              ← pip dependencies
  └── OrgTree.csv                   ← optional, for /digivalet org lookups
```

---

## One-time setup

### Windows
```bat
python -m pip install -r requirements.txt
```

### macOS
```bash
pip3 install -r requirements.txt
```

### Linux (Ubuntu / Debian)
```bash
pip3 install -r requirements.txt
# If WebEngine fails on Linux, also run:
sudo apt install python3-pyqt6.qtwebengine   # or use pip
```

> **Also make sure Ollama is installed and running:**  
> Download from https://ollama.com and run `ollama serve` before launching Digi Valet.

---

## Launch

```bash
python digi_valet_desktop.py
```

Optional flags:
```bash
python digi_valet_desktop.py --port 5174          # change port
python digi_valet_desktop.py --csv OrgTree.csv    # explicit CSV path
```

---

## What you get

| Feature | Details |
|---|---|
| **Native window** | No browser needed — runs as a real desktop app |
| **Custom title bar** | Drag to move, double-click to maximise |
| **System tray icon** | Close → minimises to tray; double-click tray icon to restore |
| **Keyboard shortcuts** | `F5` / `Ctrl+R` reload · `F11` fullscreen · `Ctrl+W` close to tray |
| **Loading screen** | Shows while the server starts up |
| **All existing features** | File attachments, org lookup, tasks, dark/light mode — everything |

---

## Making a clickable shortcut (optional)

### Windows — create `launch.bat`
```bat
@echo off
start pythonw digi_valet_desktop.py
```
Double-click `launch.bat` to open with no terminal window.

### macOS — create an Automator app
1. Open **Automator** → New Document → **Application**
2. Add **Run Shell Script** action
3. Paste: `cd /path/to/DigiValet && python3 digi_valet_desktop.py`
4. Save as `Digi Valet.app`

### Linux — create `DigiValet.desktop`
```ini
[Desktop Entry]
Name=Digi Valet
Exec=python3 /path/to/DigiValet/digi_valet_desktop.py
Icon=/path/to/DigiValet/icon.png
Terminal=false
Type=Application
Categories=Utility;
```
Place it in `~/.local/share/applications/` and it will appear in your app launcher.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `No module named PyQt6` | Run `pip install PyQt6 PyQt6-WebEngine` |
| `No module named PyQt6.QtWebEngineWidgets` | Run `pip install PyQt6-WebEngine` separately |
| Blank white window | Make sure Ollama is running: `ollama serve` |
| Port already in use | Add `--port 5174` (or any free port) |
| Linux: app won't open | Try `sudo apt install libxcb-cursor0` |
| Backend not found | Ensure `digi_valet_chat_enhanced.py` is in the same folder |