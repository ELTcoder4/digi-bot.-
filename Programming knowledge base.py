"""
programming_knowledge_base.py
══════════════════════════════════════════════════════════════════════
Comprehensive Programming & ML Knowledge Base for Digi Valet
══════════════════════════════════════════════════════════════════════

HOW TO USE
──────────
1. Place this file next to digi_valet_chat.py
2. In digi_valet_chat.py, find build_system_prompt() and add ONE line:

    from programming_knowledge_base import PROGRAMMING_KNOWLEDGE
    
    Then inside build_system_prompt(), before the return statement:
    
        prompt += "\\n\\n" + PROGRAMMING_KNOWLEDGE

3. That's it — Digi Valet will now answer ANY programming or ML question.

OR use it as a standalone knowledge base file that gets auto-loaded
by the KnowledgeBase system (/kb learn programming_knowledge_base.py).
══════════════════════════════════════════════════════════════════════
"""

PROGRAMMING_KNOWLEDGE = """
══════════════════════════════════════════════════════════════════════
PROGRAMMING & MACHINE LEARNING KNOWLEDGE BASE
You are an expert software engineer and ML scientist. Use this
knowledge to answer ANY programming or ML question accurately.
══════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 1: PYTHON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Python is a high-level, interpreted, dynamically typed language.

BASICS:
  x = 10              # integer
  y = 3.14            # float
  s = "hello"         # string
  b = True            # boolean
  lst = [1,2,3]       # list (mutable)
  tup = (1,2,3)       # tuple (immutable)
  dct = {"a":1}       # dict
  st  = {1,2,3}       # set

CONTROL FLOW:
  if x > 5: ...
  elif x == 5: ...
  else: ...
  for i in range(10): ...
  while x > 0: x -= 1
  [x**2 for x in range(10)]   # list comprehension
  {k:v for k,v in d.items()}  # dict comprehension

FUNCTIONS:
  def greet(name, greeting="Hello"):
      return f"{greeting}, {name}!"
  
  lambda x: x * 2              # anonymous function
  *args, **kwargs               # variadic arguments
  
  def decorator(func):         # decorator pattern
      def wrapper(*a, **kw):
          return func(*a, **kw)
      return wrapper

CLASSES & OOP:
  class Animal:
      def __init__(self, name):
          self.name = name
      def speak(self): ...
  
  class Dog(Animal):           # inheritance
      def speak(self):
          return "Woof"
  
  @property                    # property decorator
  @classmethod                 # class method
  @staticmethod                # static method
  __str__, __repr__, __len__   # dunder methods
  __enter__, __exit__          # context manager

ERROR HANDLING:
  try:
      risky()
  except ValueError as e:
      print(e)
  except (TypeError, KeyError):
      ...
  else:
      ...   # runs if no exception
  finally:
      ...   # always runs

FILE I/O:
  with open("file.txt", "r") as f:
      data = f.read()
  with open("file.txt", "w") as f:
      f.write("text")
  import json
  json.dumps(obj)  / json.loads(s)
  import csv
  csv.reader(f) / csv.writer(f)

GENERATORS & ITERATORS:
  def gen():
      yield 1
      yield 2
  next(g)
  list(gen())

MODULES:
  import os, sys, re, math, datetime, pathlib
  from pathlib import Path
  from collections import defaultdict, Counter, deque
  from itertools import chain, product, combinations
  from functools import reduce, partial, lru_cache
  from typing import List, Dict, Optional, Union, Tuple

COMMON PATTERNS:
  sorted(lst, key=lambda x: x[1], reverse=True)
  enumerate(lst)
  zip(a, b)
  map(func, lst)
  filter(func, lst)
  any(lst) / all(lst)
  str.split() / str.join() / str.strip() / str.replace()
  list.append() / list.extend() / list.pop() / list.sort()
  dict.get(key, default) / dict.items() / dict.keys() / dict.values()
  set.union() / set.intersection() / set.difference()

PYTHON PACKAGES OVERVIEW:
  requests      — HTTP requests
  flask/fastapi — web frameworks
  sqlalchemy    — ORM / database
  pytest        — testing
  black/flake8  — formatting/linting
  pydantic      — data validation
  click         — CLI tools
  pillow        — image processing
  boto3         — AWS SDK
  celery        — task queues

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 2: JAVASCRIPT & TYPESCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
JavaScript runs in browsers and Node.js. TypeScript adds static types.

JS BASICS:
  let x = 10;  const PI = 3.14;  var (avoid)
  "string" / 'string' / `template ${x}`
  null, undefined, NaN, Infinity
  typeof x / instanceof

FUNCTIONS:
  function add(a, b) { return a + b; }
  const add = (a, b) => a + b;         // arrow function
  const add = (a, b) => { return a+b; }
  async function fetch() { await ... } // async/await
  function* gen() { yield 1; }         // generator

ARRAYS:
  arr.map(x => x*2)
  arr.filter(x => x > 0)
  arr.reduce((acc, x) => acc + x, 0)
  arr.find(x => x.id === 1)
  arr.forEach(x => ...)
  arr.some() / arr.every()
  arr.flat() / arr.flatMap()
  [...arr1, ...arr2]          // spread
  const [a, b] = arr          // destructuring

OBJECTS:
  const obj = { a: 1, b: 2 };
  const { a, b } = obj;       // destructuring
  const copy = { ...obj };    // spread copy
  Object.keys() / Object.values() / Object.entries()
  Object.assign(target, src)

CLASSES:
  class Animal {
    constructor(name) { this.name = name; }
    speak() { return `${this.name} speaks`; }
  }
  class Dog extends Animal {
    speak() { return "Woof"; }
  }

PROMISES & ASYNC:
  fetch(url)
    .then(res => res.json())
    .then(data => ...)
    .catch(err => ...)
  
  const data = await fetch(url).then(r => r.json());
  Promise.all([p1, p2, p3])
  Promise.race([p1, p2])

TYPESCRIPT ADDITIONS:
  let x: number = 5;
  let s: string = "hi";
  let arr: number[] = [1,2,3];
  let tup: [string, number] = ["a", 1];
  interface User { id: number; name: string; }
  type ID = string | number;
  enum Direction { Up, Down, Left, Right }
  function greet(name: string): string { ... }
  generics: function identity<T>(x: T): T { return x; }
  optional: name?: string
  readonly: readonly id: number

NODE.JS:
  const fs = require('fs');          // CommonJS
  import fs from 'fs';               // ESM
  fs.readFileSync / fs.writeFileSync
  path.join() / path.resolve()
  process.env.MY_VAR
  http.createServer() / express()
  npm init / npm install / npm run

FRAMEWORKS:
  React    — UI components, hooks (useState, useEffect, useContext)
  Vue      — reactive data, components, Composition API
  Angular  — full framework, TypeScript-first, RxJS
  Next.js  — React SSR/SSG
  Express  — minimal Node.js server
  NestJS   — structured Node.js backend

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3: JAVA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Java is statically typed, compiled to JVM bytecode.

BASICS:
  int x = 10;  double y = 3.14;  boolean b = true;
  String s = "hello";  char c = 'A';
  int[] arr = {1, 2, 3};
  int[][] matrix = new int[3][3];

CLASSES:
  public class Animal {
      private String name;
      public Animal(String name) { this.name = name; }
      public String getName() { return name; }
      public void speak() { System.out.println("..."); }
  }
  
  public class Dog extends Animal {
      public Dog(String name) { super(name); }
      @Override
      public void speak() { System.out.println("Woof"); }
  }

INTERFACES:
  public interface Drawable {
      void draw();
      default void clear() { ... }
  }
  public class Circle implements Drawable { ... }

COLLECTIONS:
  List<String> list = new ArrayList<>();
  Map<String, Integer> map = new HashMap<>();
  Set<Integer> set = new HashSet<>();
  Queue<String> q = new LinkedList<>();
  list.add() / list.get() / list.remove() / list.size()
  map.put() / map.get() / map.containsKey() / map.entrySet()

GENERICS:
  public <T> T identity(T x) { return x; }
  List<? extends Number> list

STREAMS (Java 8+):
  list.stream()
      .filter(x -> x > 0)
      .map(x -> x * 2)
      .collect(Collectors.toList())
  
  IntStream.range(0, 10).sum()
  stream.reduce(0, Integer::sum)

EXCEPTION HANDLING:
  try { ... }
  catch (IOException e) { ... }
  catch (Exception e) { ... }
  finally { ... }
  throw new IllegalArgumentException("msg");

CONCURRENCY:
  Thread t = new Thread(() -> { ... });
  ExecutorService pool = Executors.newFixedThreadPool(4);
  Future<Integer> f = pool.submit(callable);
  synchronized(this) { ... }
  volatile int counter;

SPRING FRAMEWORK:
  @SpringBootApplication
  @RestController / @Controller
  @GetMapping("/path") / @PostMapping
  @Autowired / @Component / @Service / @Repository
  @Entity / @Table / @Id (JPA)
  application.properties / application.yml

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 4: C & C++
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
C — systems programming, manual memory management.
C++ — C with OOP, templates, STL.

C BASICS:
  #include <stdio.h>
  #include <stdlib.h>
  #include <string.h>
  
  int main() {
      printf("Hello\\n");
      return 0;
  }
  
  int x = 10;
  int *ptr = &x;    // pointer
  *ptr = 20;        // dereference
  int arr[5] = {1,2,3,4,5};
  arr[0] / *(arr+0)   // array access
  
  malloc(size) / calloc(n, size) / realloc(ptr, size) / free(ptr)
  
  struct Point { int x; int y; };
  typedef struct { int x; int y; } Point;
  
  void swap(int *a, int *b) {
      int tmp = *a; *a = *b; *b = tmp;
  }

C++ BASICS:
  #include <iostream>
  #include <vector>
  #include <string>
  #include <map>
  #include <algorithm>
  using namespace std;
  
  cout << "Hello" << endl;
  cin >> x;
  
  // References
  int& ref = x;
  
  // Classes
  class Animal {
  private:
      string name;
  public:
      Animal(string n) : name(n) {}
      virtual void speak() { cout << "..." << endl; }
      virtual ~Animal() {}
  };
  
  class Dog : public Animal {
  public:
      Dog(string n) : Animal(n) {}
      void speak() override { cout << "Woof" << endl; }
  };
  
  // Templates
  template<typename T>
  T max_val(T a, T b) { return a > b ? a : b; }
  
  // Smart pointers
  unique_ptr<Animal> a = make_unique<Dog>("Rex");
  shared_ptr<Animal> b = make_shared<Dog>("Max");
  
  // STL
  vector<int> v = {1,2,3};
  v.push_back(4); v.pop_back();
  map<string, int> m; m["key"] = 1;
  sort(v.begin(), v.end());
  find(v.begin(), v.end(), 3);
  
  // Lambda
  auto add = [](int a, int b) { return a+b; };
  sort(v.begin(), v.end(), [](int a, int b){ return a > b; });
  
  // Move semantics
  string s = std::move(other_s);

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 5: C# (.NET)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
C# is a modern OOP language for .NET applications.

BASICS:
  int x = 10; double y = 3.14; bool b = true;
  string s = "hello"; char c = 'A';
  var inferred = 42;
  
  Console.WriteLine("Hello");
  Console.ReadLine();

CLASSES:
  public class Animal {
      public string Name { get; set; }
      public Animal(string name) { Name = name; }
      public virtual void Speak() { Console.WriteLine("..."); }
  }
  
  public class Dog : Animal {
      public Dog(string name) : base(name) { }
      public override void Speak() { Console.WriteLine("Woof"); }
  }

INTERFACES:
  public interface IDrawable {
      void Draw();
  }

LINQ:
  var evens = numbers.Where(x => x % 2 == 0)
                     .Select(x => x * x)
                     .OrderBy(x => x)
                     .ToList();
  
  var query = from n in numbers
              where n > 5
              select n * 2;

ASYNC/AWAIT:
  public async Task<string> FetchAsync(string url) {
      using var client = new HttpClient();
      return await client.GetStringAsync(url);
  }

COLLECTIONS:
  List<int> list = new List<int>();
  Dictionary<string, int> dict = new Dictionary<string, int>();
  HashSet<int> set = new HashSet<int>();
  Queue<string> queue = new Queue<string>();
  Stack<int> stack = new Stack<int>();

GENERICS:
  public T Identity<T>(T x) { return x; }
  public class Box<T> { public T Value { get; set; } }

DELEGATES & EVENTS:
  Action<int> print = x => Console.WriteLine(x);
  Func<int, int, int> add = (a, b) => a + b;
  Predicate<int> isEven = x => x % 2 == 0;
  event EventHandler OnChange;

EXCEPTION HANDLING:
  try { ... }
  catch (ArgumentException ex) { ... }
  catch (Exception ex) when (ex.Message.Contains("...")) { ... }
  finally { ... }
  throw new InvalidOperationException("msg");

ASP.NET CORE:
  [ApiController]
  [Route("api/[controller]")]
  public class UsersController : ControllerBase {
      [HttpGet("{id}")]
      public ActionResult<User> Get(int id) { ... }
      [HttpPost]
      public ActionResult<User> Post(User user) { ... }
  }

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 6: SWIFT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Swift is Apple's language for iOS/macOS/watchOS/tvOS.

BASICS:
  var x = 10; let PI = 3.14
  var s: String = "hello"
  var arr = [1, 2, 3]
  var dict = ["key": "value"]
  
  print("Hello, \\(name)!")   // string interpolation

OPTIONALS:
  var name: String? = nil
  if let name = name { print(name) }   // optional binding
  name ?? "default"                     // nil coalescing
  name!                                 // force unwrap (unsafe)
  guard let name = name else { return } // guard let

FUNCTIONS:
  func greet(name: String, greeting: String = "Hello") -> String {
      return "\\(greeting), \\(name)!"
  }
  func swap(_ a: inout Int, _ b: inout Int) { ... }

CLASSES & STRUCTS:
  class Animal {
      var name: String
      init(name: String) { self.name = name }
      func speak() -> String { return "..." }
  }
  
  struct Point {          // value type
      var x, y: Double
      mutating func move(dx: Double, dy: Double) {
          x += dx; y += dy
      }
  }

PROTOCOLS:
  protocol Drawable {
      func draw()
      var color: String { get }
  }
  
  extension Circle: Drawable { ... }

ENUMS:
  enum Direction { case north, south, east, west }
  enum Result<T> {
      case success(T)
      case failure(Error)
  }

CLOSURES:
  let double = { (x: Int) -> Int in return x * 2 }
  arr.map { $0 * 2 }
  arr.filter { $0 > 0 }
  arr.reduce(0, +)

ERROR HANDLING:
  enum AppError: Error { case notFound, unauthorized }
  func fetch() throws -> Data { throw AppError.notFound }
  do {
      let data = try fetch()
  } catch AppError.notFound {
      print("Not found")
  } catch { print(error) }

SWIFTUI:
  struct ContentView: View {
      @State var count = 0
      var body: some View {
          VStack {
              Text("Count: \\(count)")
              Button("Increment") { count += 1 }
          }
      }
  }

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 7: RUST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Rust is a systems language focused on safety and performance.

BASICS:
  let x: i32 = 5;       // immutable
  let mut y: f64 = 3.14; // mutable
  const MAX: u32 = 100;
  
  println!("{}", x);    // macro
  let s = String::from("hello");
  let slice = &s[0..3];

OWNERSHIP:
  let s1 = String::from("hello");
  let s2 = s1;           // s1 moved, no longer valid
  let s3 = s2.clone();   // explicit deep copy
  
  fn take(s: String) { ... }  // takes ownership
  fn borrow(s: &String) { ... } // borrows
  fn borrow_mut(s: &mut String) { ... } // mutable borrow
  
  Rules: one owner, many immutable refs OR one mutable ref.

STRUCTS:
  struct Point { x: f64, y: f64 }
  impl Point {
      fn new(x: f64, y: f64) -> Self { Point { x, y } }
      fn distance(&self) -> f64 { (self.x.powi(2)+self.y.powi(2)).sqrt() }
  }

ENUMS & PATTERN MATCHING:
  enum Shape { Circle(f64), Rectangle(f64, f64) }
  
  match shape {
      Shape::Circle(r) => PI * r * r,
      Shape::Rectangle(w, h) => w * h,
  }
  
  if let Some(x) = optional { ... }
  while let Some(x) = stack.pop() { ... }

TRAITS:
  trait Area { fn area(&self) -> f64; }
  impl Area for Circle { fn area(&self) -> f64 { PI * self.r * self.r } }
  fn print_area(shape: &impl Area) { println!("{}", shape.area()); }
  fn print_area<T: Area>(shape: &T) { ... }

ERROR HANDLING:
  Result<T, E>  /  Option<T>
  fn divide(a: f64, b: f64) -> Result<f64, String> {
      if b == 0.0 { Err("div by zero".to_string()) }
      else { Ok(a / b) }
  }
  let val = divide(10.0, 2.0)?;  // ? operator propagates error

COLLECTIONS:
  Vec<T> — dynamic array
  HashMap<K,V> — hash map
  HashSet<T> — hash set
  BTreeMap<K,V> — sorted map
  
  let v = vec![1, 2, 3];
  v.iter().map(|x| x*2).collect::<Vec<_>>();
  v.iter().filter(|&&x| x > 1).sum::<i32>();

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 8: GO (GOLANG)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Go is statically typed, compiled, with built-in concurrency.

BASICS:
  package main
  import "fmt"
  
  func main() {
      fmt.Println("Hello, World!")
  }
  
  var x int = 10
  y := 3.14          // short declaration
  const PI = 3.14159

FUNCTIONS:
  func add(a, b int) int { return a + b }
  func swap(a, b int) (int, int) { return b, a }  // multiple returns
  func divide(a, b float64) (float64, error) { ... }

STRUCTS & METHODS:
  type Point struct { X, Y float64 }
  
  func (p Point) Distance() float64 {
      return math.Sqrt(p.X*p.X + p.Y*p.Y)
  }
  func (p *Point) Scale(f float64) { p.X *= f; p.Y *= f }

INTERFACES:
  type Stringer interface { String() string }
  type Writer interface { Write([]byte) (int, error) }

GOROUTINES & CHANNELS:
  go func() { doWork() }()   // goroutine
  
  ch := make(chan int)
  go func() { ch <- 42 }()
  val := <-ch
  
  ch := make(chan int, 10)    // buffered channel
  
  select {
  case msg := <-ch1: ...
  case ch2 <- val: ...
  default: ...
  }

SLICES & MAPS:
  s := []int{1, 2, 3}
  s = append(s, 4)
  s2 := s[1:3]
  
  m := map[string]int{"a": 1, "b": 2}
  val, ok := m["key"]
  delete(m, "key")

ERROR HANDLING:
  func readFile(path string) ([]byte, error) {
      data, err := os.ReadFile(path)
      if err != nil { return nil, fmt.Errorf("read: %w", err) }
      return data, nil
  }

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 9: SQL & DATABASES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SQL is used to manage relational databases.

DDL (Data Definition Language):
  CREATE TABLE users (
      id   INT PRIMARY KEY AUTO_INCREMENT,
      name VARCHAR(100) NOT NULL,
      email VARCHAR(255) UNIQUE,
      age  INT CHECK (age >= 0),
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP
  );
  ALTER TABLE users ADD COLUMN phone VARCHAR(20);
  DROP TABLE users;
  CREATE INDEX idx_email ON users(email);

DML (Data Manipulation Language):
  INSERT INTO users (name, email) VALUES ('Alice', 'a@b.com');
  SELECT * FROM users WHERE age > 18 ORDER BY name LIMIT 10;
  UPDATE users SET age = 25 WHERE id = 1;
  DELETE FROM users WHERE id = 1;

JOINS:
  INNER JOIN — only matching rows
  LEFT JOIN  — all left rows + matching right
  RIGHT JOIN — all right rows + matching left
  FULL JOIN  — all rows from both
  
  SELECT u.name, o.total
  FROM users u
  INNER JOIN orders o ON u.id = o.user_id
  WHERE o.total > 100;

AGGREGATIONS:
  SELECT dept, COUNT(*), AVG(salary), MAX(salary)
  FROM employees
  GROUP BY dept
  HAVING AVG(salary) > 50000
  ORDER BY AVG(salary) DESC;

SUBQUERIES:
  SELECT * FROM users WHERE id IN (SELECT user_id FROM orders);
  SELECT *, (SELECT COUNT(*) FROM orders WHERE user_id = u.id) AS order_count
  FROM users u;

WINDOW FUNCTIONS:
  SELECT name, salary,
         RANK() OVER (PARTITION BY dept ORDER BY salary DESC),
         ROW_NUMBER() OVER (ORDER BY salary DESC),
         LAG(salary) OVER (ORDER BY hire_date)
  FROM employees;

TRANSACTIONS:
  BEGIN;
  UPDATE accounts SET balance = balance - 100 WHERE id = 1;
  UPDATE accounts SET balance = balance + 100 WHERE id = 2;
  COMMIT;  -- or ROLLBACK;

DATABASE TYPES:
  MySQL/MariaDB — popular open-source RDBMS
  PostgreSQL    — advanced open-source, supports JSON, arrays, full-text
  SQLite        — embedded, file-based, zero config
  SQL Server    — Microsoft enterprise
  Oracle        — enterprise, complex licensing
  MongoDB       — NoSQL, document-based (JSON/BSON)
  Redis         — in-memory key-value, caching, pub/sub
  Cassandra     — distributed NoSQL, wide-column
  Elasticsearch — full-text search, analytics

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 10: HTML & CSS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HTML structures web content; CSS styles it.

HTML STRUCTURE:
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Page Title</title>
      <link rel="stylesheet" href="style.css">
  </head>
  <body>
      <header><nav>...</nav></header>
      <main><article>...</article></main>
      <footer>...</footer>
      <script src="main.js"></script>
  </body>
  </html>

SEMANTIC TAGS:
  <header> <nav> <main> <article> <section> <aside> <footer>
  <h1>-<h6> <p> <a href=""> <img src="" alt=""> <ul><li> <ol>
  <table><tr><th><td> <form><input><button><select><textarea>
  <div> <span> <label> <figure> <figcaption>

CSS BASICS:
  selector { property: value; }
  
  /* Selectors */
  *          — all elements
  div        — element type
  .class     — class
  #id        — id
  a:hover    — pseudo-class
  div::before — pseudo-element
  div > p    — direct child
  div + p    — adjacent sibling
  [attr="v"] — attribute

CSS BOX MODEL:
  content → padding → border → margin
  box-sizing: border-box; (recommended)

LAYOUT — FLEXBOX:
  display: flex;
  flex-direction: row | column;
  justify-content: center | space-between | flex-start | flex-end;
  align-items: center | stretch | flex-start;
  flex-wrap: wrap;
  gap: 1rem;
  flex: 1; (grow/shrink/basis)

LAYOUT — GRID:
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: auto;
  grid-gap: 1rem;
  grid-column: 1 / 3;
  grid-row: 1 / 2;

RESPONSIVE DESIGN:
  @media (max-width: 768px) { ... }
  @media (prefers-color-scheme: dark) { ... }
  vw, vh, %, em, rem — relative units
  
CSS VARIABLES:
  :root { --primary: #007bff; --spacing: 1rem; }
  color: var(--primary);

ANIMATIONS:
  @keyframes slide { from { opacity:0 } to { opacity:1 } }
  animation: slide 0.3s ease-in-out;
  transition: all 0.2s ease;
  transform: translateX(10px) rotate(45deg) scale(1.2);

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 11: GIT & VERSION CONTROL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  git init                    # new repo
  git clone <url>             # clone repo
  git status                  # show changes
  git add .                   # stage all
  git add <file>              # stage file
  git commit -m "message"     # commit
  git push origin main        # push
  git pull origin main        # pull
  git fetch                   # fetch without merge
  
  git branch <name>           # create branch
  git checkout <branch>       # switch branch
  git checkout -b <branch>    # create + switch
  git merge <branch>          # merge
  git rebase <branch>         # rebase
  
  git log --oneline --graph   # visual log
  git diff HEAD~1             # diff
  git stash / git stash pop   # stash changes
  git reset --soft HEAD~1     # undo last commit (keep changes)
  git reset --hard HEAD~1     # undo last commit (discard changes)
  git revert <hash>           # safe undo (new commit)
  git cherry-pick <hash>      # apply specific commit
  
  .gitignore — list files/patterns to ignore
  git tag v1.0.0             # tag release

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 12: DATA STRUCTURES & ALGORITHMS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARRAYS: O(1) access, O(n) insert/delete mid
LINKED LIST: O(n) access, O(1) insert/delete at head
STACK: LIFO — push/pop O(1)
QUEUE: FIFO — enqueue/dequeue O(1)
HASH TABLE: O(1) avg get/set, O(n) worst
BINARY TREE: nodes with left/right children
BST: left < root < right, O(log n) search/insert avg
HEAP: complete binary tree, min-heap: parent <= children
GRAPH: vertices + edges (directed/undirected, weighted)
TRIE: prefix tree for string search

SORTING ALGORITHMS:
  Bubble Sort:    O(n²) time, O(1) space — simple, slow
  Selection Sort: O(n²) time, O(1) space
  Insertion Sort: O(n²) avg, O(n) best — good for small/nearly sorted
  Merge Sort:     O(n log n) time, O(n) space — stable
  Quick Sort:     O(n log n) avg, O(n²) worst, O(log n) space
  Heap Sort:      O(n log n) time, O(1) space
  Counting Sort:  O(n+k) — for integers in known range
  Radix Sort:     O(nk) — digit by digit

SEARCHING:
  Linear Search: O(n)
  Binary Search: O(log n) — requires sorted array
  BFS: level-by-level, uses queue, shortest path unweighted
  DFS: depth-first, uses stack/recursion

GRAPH ALGORITHMS:
  Dijkstra's:     shortest path, non-negative weights, O((V+E) log V)
  Bellman-Ford:   shortest path with negative weights, O(VE)
  Floyd-Warshall: all-pairs shortest path, O(V³)
  Prim's/Kruskal's: minimum spanning tree
  Topological Sort: DAG ordering (DFS or Kahn's BFS)

DYNAMIC PROGRAMMING:
  Memoization (top-down) vs Tabulation (bottom-up)
  Classic problems:
    Fibonacci, Knapsack 0/1, LCS, LIS, Coin Change,
    Edit Distance, Matrix Chain, Rod Cutting

BIG O NOTATION:
  O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 13: MACHINE LEARNING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ML TYPES:
  Supervised Learning   — labeled data, predict output
  Unsupervised Learning — no labels, find structure
  Reinforcement Learning — agent learns via reward/penalty
  Semi-supervised       — small labeled + large unlabeled

SUPERVISED ALGORITHMS:
  Linear Regression:       y = mx + b, minimize MSE
  Logistic Regression:     classification, sigmoid output
  Decision Tree:           splits by info gain / gini impurity
  Random Forest:           ensemble of decision trees (bagging)
  Gradient Boosting:       sequential trees (XGBoost, LightGBM, CatBoost)
  SVM:                     max-margin hyperplane, kernel trick
  KNN:                     k nearest neighbors vote
  Naive Bayes:             P(y|x) via Bayes theorem, assumes independence
  Neural Networks:         layers of weighted nodes + activation

UNSUPERVISED ALGORITHMS:
  K-Means:            assign to k centroids, minimize intra-cluster dist
  DBSCAN:             density-based, finds arbitrary shapes, handles noise
  Hierarchical:       agglomerative (bottom-up) or divisive (top-down)
  PCA:                dimensionality reduction, maximize variance
  t-SNE:              non-linear dim reduction for visualization
  Autoencoders:       encode→bottleneck→decode, anomaly detection

EVALUATION METRICS:
  Classification:
    Accuracy = (TP+TN)/(TP+TN+FP+FN)
    Precision = TP/(TP+FP)
    Recall = TP/(TP+FN)
    F1 = 2*(P*R)/(P+R)
    ROC-AUC — area under ROC curve
    Confusion Matrix
  Regression:
    MSE, RMSE, MAE, R², MAPE
  Clustering:
    Silhouette Score, Davies-Bouldin Index

BIAS-VARIANCE TRADEOFF:
  High Bias (underfitting)  — model too simple
  High Variance (overfitting) — model too complex
  Goal: minimize both via regularization, cross-validation

REGULARIZATION:
  L1 (Lasso) — sparse weights, feature selection
  L2 (Ridge) — small weights, prevents overfitting
  Elastic Net — combination of L1 + L2
  Dropout — randomly zero neurons during training
  Early Stopping — stop when val loss stops improving

CROSS-VALIDATION:
  K-Fold: split into k folds, train on k-1, test on 1
  Stratified K-Fold: preserves class distribution
  Leave-One-Out (LOO): k = n
  Train/Val/Test split: e.g. 70/15/15

FEATURE ENGINEERING:
  Normalization: (x - min)/(max - min) → [0,1]
  Standardization: (x - mean)/std → N(0,1)
  One-Hot Encoding: categorical → binary columns
  Label Encoding: category → integer
  Log Transform: handle skewed distributions
  Polynomial Features: x, x², x³, x₁x₂
  Handling missing: mean/median/mode imputation, KNN impute, drop

SCIKIT-LEARN WORKFLOW:
  from sklearn.model_selection import train_test_split, cross_val_score
  from sklearn.preprocessing import StandardScaler, LabelEncoder
  from sklearn.linear_model import LinearRegression, LogisticRegression
  from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
  from sklearn.svm import SVC
  from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
  from sklearn.pipeline import Pipeline
  
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
  scaler = StandardScaler()
  X_train = scaler.fit_transform(X_train)
  X_test = scaler.transform(X_test)
  model = RandomForestClassifier(n_estimators=100)
  model.fit(X_train, y_train)
  y_pred = model.predict(X_test)
  print(accuracy_score(y_test, y_pred))

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 14: DEEP LEARNING & NEURAL NETWORKS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FUNDAMENTALS:
  Neuron: weighted sum + bias + activation function
  Activation Functions:
    ReLU:     max(0,x) — most common hidden layer
    Sigmoid:  1/(1+e^-x) — binary output [0,1]
    Tanh:     (e^x-e^-x)/(e^x+e^-x) — [-1,1]
    Softmax:  multi-class probabilities (sum=1)
    Leaky ReLU: max(0.01x, x) — avoids dying ReLU

BACKPROPAGATION:
  Chain rule to compute gradients layer by layer
  Gradient Descent: θ = θ - α∇L
  SGD: one sample per update
  Mini-batch: small batch per update
  Optimizers: Adam (adaptive lr), RMSProp, Adagrad, Momentum

ARCHITECTURES:
  MLP (Fully Connected):     dense layers, tabular data
  CNN (Convolutional):       image recognition
    Conv2D → pooling → flatten → dense
    Filters detect edges, textures, shapes
  RNN (Recurrent):           sequences, text, time series
    Vanishing gradient problem
  LSTM:                      Long Short-Term Memory, gates (input/forget/output)
  GRU:                       Gated Recurrent Unit, simpler than LSTM
  Transformer:               self-attention mechanism, parallelizable
    BERT, GPT, T5, ViT
  GAN:                       Generator + Discriminator adversarial training
  Autoencoder:               Encoder + Decoder, compression/anomaly detection
  Diffusion Models:          iterative denoising (DALL-E, Stable Diffusion)

TENSORFLOW / KERAS:
  import tensorflow as tf
  from tensorflow import keras
  
  model = keras.Sequential([
      keras.layers.Dense(128, activation='relu', input_shape=(784,)),
      keras.layers.Dropout(0.2),
      keras.layers.Dense(64, activation='relu'),
      keras.layers.Dense(10, activation='softmax')
  ])
  model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
  model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)
  model.evaluate(X_test, y_test)
  model.save('model.h5') / model = keras.models.load_model('model.h5')
  
  # CNN
  model = keras.Sequential([
      keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
      keras.layers.MaxPooling2D(2,2),
      keras.layers.Conv2D(64, (3,3), activation='relu'),
      keras.layers.Flatten(),
      keras.layers.Dense(10, activation='softmax')
  ])

PYTORCH:
  import torch
  import torch.nn as nn
  import torch.optim as optim
  
  class Net(nn.Module):
      def __init__(self):
          super().__init__()
          self.fc1 = nn.Linear(784, 128)
          self.fc2 = nn.Linear(128, 10)
      
      def forward(self, x):
          x = torch.relu(self.fc1(x))
          x = self.fc2(x)
          return x
  
  model = Net()
  optimizer = optim.Adam(model.parameters(), lr=0.001)
  criterion = nn.CrossEntropyLoss()
  
  for epoch in range(10):
      for X, y in dataloader:
          optimizer.zero_grad()
          output = model(X)
          loss = criterion(output, y)
          loss.backward()
          optimizer.step()
  
  torch.save(model.state_dict(), 'model.pth')
  model.load_state_dict(torch.load('model.pth'))

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 15: NUMPY & PANDAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NUMPY:
  import numpy as np
  
  a = np.array([1, 2, 3])
  b = np.zeros((3,3)) / np.ones((3,3)) / np.eye(3) / np.random.rand(3,3)
  a.shape / a.dtype / a.ndim / a.size
  a.reshape(3,1) / a.T (transpose) / a.flatten()
  
  np.dot(a, b) / a @ b       # matrix multiply
  np.sum(a) / np.mean(a) / np.std(a) / np.max(a) / np.argmax(a)
  np.sort(a) / np.argsort(a)
  np.concatenate([a, b], axis=0)
  np.vstack([a, b]) / np.hstack([a, b])
  a[a > 2]                   # boolean indexing
  a[0:2, 1:3]               # slicing
  np.where(a > 0, a, 0)     # conditional
  np.linspace(0, 1, 100)    # evenly spaced
  np.arange(0, 10, 2)       # range

PANDAS:
  import pandas as pd
  
  df = pd.DataFrame({'a': [1,2,3], 'b': [4,5,6]})
  df = pd.read_csv('file.csv') / pd.read_excel() / pd.read_json()
  df.to_csv('out.csv', index=False)
  
  df.head(5) / df.tail() / df.info() / df.describe()
  df.shape / df.columns / df.dtypes / df.index
  df['col'] / df[['col1','col2']]
  df.loc[0, 'col'] / df.iloc[0, 1]
  df[df['age'] > 18]           # filter
  df.sort_values('col', ascending=False)
  df.drop_duplicates() / df.dropna() / df.fillna(0)
  df.rename(columns={'old':'new'})
  df['col'].apply(lambda x: x*2)
  df.groupby('dept')['salary'].mean()
  df.pivot_table(values='sales', index='region', columns='product', aggfunc='sum')
  pd.merge(df1, df2, on='id', how='inner')
  pd.concat([df1, df2], axis=0)
  df['col'].value_counts()
  df['col'].nunique()
  df.isnull().sum()
  pd.get_dummies(df['category'])   # one-hot encode

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 16: DATA VISUALIZATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MATPLOTLIB:
  import matplotlib.pyplot as plt
  
  plt.plot(x, y, 'b-o', label='line')
  plt.scatter(x, y, c='red', s=50)
  plt.bar(categories, values)
  plt.hist(data, bins=20)
  plt.pie(sizes, labels=labels)
  plt.xlabel('X') / plt.ylabel('Y') / plt.title('Title')
  plt.legend() / plt.grid(True)
  plt.savefig('plot.png', dpi=150, bbox_inches='tight')
  plt.show()
  
  fig, axes = plt.subplots(2, 2, figsize=(10, 8))
  axes[0,0].plot(x, y)

SEABORN:
  import seaborn as sns
  
  sns.histplot(df['col'], kde=True)
  sns.boxplot(x='category', y='value', data=df)
  sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
  sns.scatterplot(x='x', y='y', hue='category', data=df)
  sns.pairplot(df)
  sns.barplot(x='cat', y='val', data=df, ci=95)
  sns.set_theme(style='whitegrid')

PLOTLY (interactive):
  import plotly.express as px
  import plotly.graph_objects as go
  
  fig = px.scatter(df, x='col1', y='col2', color='category')
  fig = px.line(df, x='date', y='value')
  fig = px.bar(df, x='category', y='value')
  fig.show()

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 17: SYSTEM DESIGN & ARCHITECTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PATTERNS:
  MVC:         Model-View-Controller
  MVP:         Model-View-Presenter
  MVVM:        Model-View-ViewModel
  Repository:  data access abstraction
  Factory:     object creation
  Singleton:   single instance
  Observer:    publish-subscribe
  Strategy:    interchangeable algorithms
  Decorator:   add behavior dynamically

SOLID PRINCIPLES:
  S — Single Responsibility
  O — Open/Closed
  L — Liskov Substitution
  I — Interface Segregation
  D — Dependency Inversion

MICROSERVICES vs MONOLITH:
  Monolith: simple, easier to debug, hard to scale independently
  Microservices: independent deploy/scale, complex networking

REST API DESIGN:
  GET    /users          — list users
  POST   /users          — create user
  GET    /users/{id}     — get user
  PUT    /users/{id}     — replace user
  PATCH  /users/{id}     — update user
  DELETE /users/{id}     — delete user
  HTTP status: 200 OK, 201 Created, 400 Bad Request,
               401 Unauthorized, 403 Forbidden,
               404 Not Found, 500 Internal Server Error

CACHING:
  Redis, Memcached — in-memory caching
  Cache aside, write-through, write-behind
  CDN — static assets at edge
  Browser cache — Cache-Control headers

SCALING:
  Vertical: bigger machine
  Horizontal: more machines + load balancer
  Database: read replicas, sharding, partitioning
  Message queues: Kafka, RabbitMQ, SQS (async decoupling)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 18: DEVOPS & CLOUD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DOCKER:
  FROM python:3.11
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  COPY . .
  CMD ["python", "app.py"]
  
  docker build -t myapp .
  docker run -p 8080:80 myapp
  docker-compose up --build
  docker ps / docker logs / docker exec -it <id> bash

KUBERNETES:
  Pod: smallest deployable unit
  Deployment: manages pod replicas
  Service: exposes pods (ClusterIP, NodePort, LoadBalancer)
  Ingress: HTTP routing
  ConfigMap / Secret: configuration
  kubectl get pods / kubectl apply -f deploy.yaml
  kubectl logs <pod> / kubectl exec -it <pod> -- bash

CI/CD:
  GitHub Actions, Jenkins, GitLab CI, CircleCI
  Pipeline: build → test → lint → deploy
  
  # GitHub Actions example
  on: [push]
  jobs:
    test:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v3
        - run: pip install -r requirements.txt
        - run: pytest

CLOUD PROVIDERS:
  AWS:   EC2, S3, RDS, Lambda, ECS, EKS, CloudFront, SQS, SNS
  GCP:   Compute Engine, Cloud Storage, BigQuery, Cloud Run, GKE
  Azure: VMs, Blob Storage, Azure SQL, Functions, AKS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 19: SECURITY & BEST PRACTICES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMMON VULNERABILITIES:
  SQL Injection:       use parameterized queries / ORM
  XSS:                 sanitize inputs, Content-Security-Policy
  CSRF:                CSRF tokens, SameSite cookies
  IDOR:                check authorization per resource
  Path Traversal:      validate file paths
  Command Injection:   avoid shell=True, validate input

AUTHENTICATION:
  JWT (JSON Web Token): header.payload.signature, stateless
  OAuth 2.0:           authorization framework (Google/GitHub login)
  bcrypt/argon2:       password hashing (never store plaintext)
  2FA/MFA:             TOTP (Google Authenticator)

HTTPS & TLS:
  TLS 1.3 — current standard
  Let's Encrypt — free certificates
  HSTS — force HTTPS

PASSWORDS:
  import bcrypt
  hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
  bcrypt.checkpw(password.encode(), hashed)

ENVIRONMENT VARIABLES:
  Never hardcode secrets — use .env files + python-dotenv
  from dotenv import load_dotenv; import os
  load_dotenv(); API_KEY = os.getenv('API_KEY')

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 20: NLP & LLMs
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NLP FUNDAMENTALS:
  Tokenization:    split text into tokens (words/subwords/chars)
  Stemming:        reduce to root (running→run)
  Lemmatization:   dictionary form (better→good)
  POS Tagging:     noun, verb, adjective, etc.
  NER:             Named Entity Recognition (person, org, place)
  Stop Words:      common words filtered out (the, is, at)
  TF-IDF:          term frequency × inverse document frequency

TEXT REPRESENTATIONS:
  Bag of Words:    count matrix
  TF-IDF:          weighted term matrix
  Word2Vec:        dense vector, semantic similarity
  GloVe:           global vectors for word representation
  BERT Embeddings: contextual, from transformer

TRANSFORMER ARCHITECTURE:
  Input → Tokenization → Embedding → Positional Encoding
  → Multi-Head Self-Attention → Feed Forward → Output
  
  Self-Attention: Q, K, V matrices
  Attention(Q,K,V) = softmax(QK^T/√dk) × V

POPULAR LLMs:
  GPT-4/3.5 (OpenAI):         autoregressive, instruction-tuned
  Claude (Anthropic):          constitutional AI, safe
  Gemini (Google):             multimodal
  LLaMA (Meta):                open weights
  Mistral:                     efficient open source
  BERT (Google):               encoder, classification/QA
  T5:                          text-to-text transfer

FINE-TUNING:
  Full Fine-tuning:   update all weights (expensive)
  LoRA:               Low-Rank Adaptation, update small matrices
  QLoRA:              quantized LoRA, 4-bit precision
  PEFT:               Parameter Efficient Fine-Tuning
  RLHF:               Reinforcement Learning from Human Feedback

PROMPT ENGINEERING:
  Zero-shot:     direct question, no examples
  Few-shot:      provide 2-5 examples in prompt
  Chain-of-Thought: "Let's think step by step"
  ReAct:         Reasoning + Acting (tool use)
  System prompt: set AI persona and constraints
  Temperature:   0 = deterministic, 1 = creative
  Top-p:         nucleus sampling

HUGGING FACE:
  from transformers import pipeline, AutoTokenizer, AutoModel
  
  classifier = pipeline("sentiment-analysis")
  classifier("I love this product!")
  
  generator = pipeline("text-generation", model="gpt2")
  generator("Once upon a time", max_length=50)
  
  ner = pipeline("ner", grouped_entities=True)
  
  tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
  model = AutoModel.from_pretrained("bert-base-uncased")
  inputs = tokenizer("Hello world", return_tensors="pt")
  outputs = model(**inputs)

LANGCHAIN:
  from langchain.llms import OpenAI
  from langchain.chains import LLMChain
  from langchain.prompts import PromptTemplate
  from langchain.vectorstores import FAISS
  from langchain.embeddings import OpenAIEmbeddings
  
  # RAG pipeline
  embeddings = OpenAIEmbeddings()
  vectorstore = FAISS.from_documents(docs, embeddings)
  retriever = vectorstore.as_retriever()
  
  # Agents
  from langchain.agents import initialize_agent, Tool

OLLAMA (LOCAL LLMs):
  ollama pull llama3        # download model
  ollama run llama3         # interactive chat
  ollama serve              # start API server (port 11434)
  
  # Python API call
  import requests
  response = requests.post('http://localhost:11434/api/chat', json={
      "model": "llama3",
      "messages": [{"role": "user", "content": "Hello!"}],
      "stream": False
  })

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 21: RUBY & KOTLIN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RUBY:
  # Variables
  x = 10; name = "Alice"; arr = [1,2,3]; hash = {a: 1}
  
  # Methods
  def greet(name = "World")
    "Hello, #{name}!"
  end
  
  # Classes
  class Animal
    attr_accessor :name
    def initialize(name); @name = name; end
    def speak; "..."; end
  end
  
  # Blocks
  [1,2,3].each { |x| puts x }
  [1,2,3].map { |x| x * 2 }
  [1,2,3].select { |x| x > 1 }
  [1,2,3].reduce(0) { |sum, x| sum + x }
  
  # Rails (web framework)
  rails new myapp
  rails generate model User name:string email:string
  rails generate controller Users index show
  User.all / User.find(1) / User.where(age: 18..)
  User.create(name: "Alice") / user.save / user.destroy

KOTLIN:
  val x: Int = 10      // immutable
  var y: String = "hi" // mutable
  val list = listOf(1, 2, 3)
  val mutable = mutableListOf(1, 2, 3)
  val map = mapOf("a" to 1, "b" to 2)
  
  // Null safety
  var name: String? = null
  name?.length         // safe call
  name ?: "default"    // elvis operator
  name!!.length        // non-null assert
  
  // Functions
  fun greet(name: String, greeting: String = "Hello") = "$greeting, $name!"
  val square = { x: Int -> x * x }  // lambda
  
  // Data classes
  data class User(val id: Int, val name: String)
  
  // Extension functions
  fun String.isPalindrome() = this == this.reversed()
  
  // Coroutines
  import kotlinx.coroutines.*
  runBlocking {
      val result = async { fetchData() }
      println(result.await())
  }

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 22: SHELL / BASH SCRIPTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  #!/bin/bash
  
  # Variables
  NAME="Alice"
  echo "Hello, $NAME"
  
  # Input
  read -p "Enter name: " name
  
  # Conditionals
  if [ "$x" -gt 5 ]; then echo "big"; elif [ "$x" -eq 5 ]; then echo "5"; else echo "small"; fi
  [ -f file ] / [ -d dir ] / [ -z "$str" ] / [ "$a" == "$b" ]
  
  # Loops
  for i in {1..10}; do echo $i; done
  for file in *.txt; do cat "$file"; done
  while [ $count -lt 10 ]; do ((count++)); done
  
  # Functions
  greet() { echo "Hello, $1"; }
  greet "World"
  
  # Common commands
  ls -la / pwd / cd / mkdir -p / rm -rf / cp / mv
  cat / head / tail / grep / sed / awk / cut / sort / uniq / wc
  find . -name "*.py" -type f
  grep -r "pattern" .
  sed -i 's/old/new/g' file.txt
  awk '{print $1, $3}' file.txt
  chmod +x script.sh / chown user:group file
  ps aux / kill -9 PID / top / htop
  curl -X POST -H "Content-Type: application/json" -d '{"key":"val"}' http://api.com
  ssh user@host / scp file user@host:/path
  
══════════════════════════════════════════════════════════════════════
END OF PROGRAMMING KNOWLEDGE BASE
You can now confidently answer questions about any of the above
technologies, languages, frameworks, and concepts.
══════════════════════════════════════════════════════════════════════
"""


# ─────────────────────────────────────────────────────────────────────
# INTEGRATION CODE — paste into digi_valet_chat.py
# ─────────────────────────────────────────────────────────────────────

INTEGRATION_INSTRUCTIONS = """
HOW TO INTEGRATE INTO digi_valet_chat.py
═════════════════════════════════════════

STEP 1: Add this import at the top of digi_valet_chat.py
────────────────────────────────────────────────────────
from programming_knowledge_base import PROGRAMMING_KNOWLEDGE


STEP 2: Update build_system_prompt() — add ONE line
────────────────────────────────────────────────────
Find this function (around line 474):

    def build_system_prompt(tone, language, kb=None):
        base = BASE_PERSONALITY.get(tone, BASE_PERSONALITY["balanced"])
        addon = LANGUAGE_ADDONS.get(language, "")
        prompt = base + ("\\n" + addon if addon else "")
        if kb is not None and not kb.is_empty():
            prompt += "\\n\\n" + kb.system_prompt_block()
        return prompt

Replace it with:

    def build_system_prompt(tone, language, kb=None):
        base = BASE_PERSONALITY.get(tone, BASE_PERSONALITY["balanced"])
        addon = LANGUAGE_ADDONS.get(language, "")
        prompt = base + ("\\n" + addon if addon else "")
        if kb is not None and not kb.is_empty():
            prompt += "\\n\\n" + kb.system_prompt_block()
        # ── Inject programming knowledge base ──
        prompt += "\\n\\n" + PROGRAMMING_KNOWLEDGE
        return prompt


STEP 3: Done!
─────────────
Restart Digi Valet. It will now answer questions about:
  Python, JavaScript, TypeScript, Java, C, C++, C#, Swift,
  Rust, Go, Ruby, Kotlin, SQL, HTML/CSS, Bash, Git,
  Data Structures, Algorithms, Machine Learning, Deep Learning,
  NumPy, Pandas, TensorFlow, PyTorch, NLP, LLMs, and more.
"""


if __name__ == "__main__":
    print("Programming Knowledge Base loaded.")
    print(f"Knowledge base size: {len(PROGRAMMING_KNOWLEDGE):,} characters")
    print(INTEGRATION_INSTRUCTIONS)