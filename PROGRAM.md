# Program

Each day: the topic to learn, the project, the goal that must work, and an optional stretch goal.
Learn the topic first (docs, a tutorial, the REPL), then build the project without looking at a solution.

## Block 1: Foundations (days 1–20)

Write small, correct programs with the core language: types, control flow, collections, functions, files and errors.

### Day 1 · 20 Oct 2026 · Greeting Card
- **Learn:** Setup, REPL, print/input
- **Goal:** Install Python 3.12, create a venv, ask the user's name and birth year, print a formatted card with their age.
- **Stretch:** Add an ASCII-art border that fits the longest line.

### Day 2 · 21 Oct 2026 · Tip Calculator
- **Learn:** Variables, numbers, f-strings
- **Goal:** Bill, tip percentage and number of people → amount per person, rounded to 2 decimals.
- **Stretch:** Support splitting unevenly by percentages.

### Day 3 · 22 Oct 2026 · Text Statistics
- **Learn:** Strings and string methods
- **Goal:** Read a paragraph and print characters, words, sentences, vowels and the longest word.
- **Stretch:** Read the text from a file given as an argument.

### Day 4 · 23 Oct 2026 · BMI and Grade Calculator
- **Learn:** Conditionals
- **Goal:** BMI category from weight/height, letter grade from a score; reject invalid ranges.
- **Stretch:** Turn both into a menu-driven program.

### Day 5 · 24 Oct 2026 · Number Patterns
- **Learn:** Loops: for, while, range
- **Goal:** Multiplication table, FizzBuzz and a pyramid of numbers chosen from a menu.
- **Stretch:** Let the user pick the FizzBuzz words and divisors.

### Day 6 · 25 Oct 2026 · Number Guessing Game
- **Learn:** random, while loops
- **Goal:** Computer picks 1–100, player guesses with higher/lower hints; count attempts.
- **Stretch:** Difficulty levels and a best-score record in memory.

### Day 7 · 26 Oct 2026 · Shopping List
- **Learn:** Lists
- **Goal:** Add, remove, list and clear items with a text menu; no duplicates.
- **Stretch:** Quantities and sorting by name.

### Day 8 · 27 Oct 2026 · Rock Paper Scissors
- **Learn:** Tuples, unpacking, slicing
- **Goal:** Best of 5 against the computer, rules stored as tuples, score shown each round.
- **Stretch:** Add Lizard–Spock.

### Day 9 · 28 Oct 2026 · Phone Book
- **Learn:** Dictionaries
- **Goal:** Add, search (partial match), update and delete contacts.
- **Stretch:** Multiple numbers per contact.

### Day 10 · 29 Oct 2026 · Text Comparer
- **Learn:** Sets
- **Goal:** Common, unique and total distinct words of two texts.
- **Stretch:** Ignore a list of stop words.

### Day 11 · 30 Oct 2026 · Unit Converter
- **Learn:** Functions, parameters, return
- **Goal:** Length, weight and temperature conversions, one function per conversion.
- **Stretch:** A conversion table printed for a range of values.

### Day 12 · 31 Oct 2026 · Calculator with History
- **Learn:** Scope, *args, **kwargs
- **Goal:** Calculator that keeps the last 10 operations and can repeat one.
- **Stretch:** Variadic `total(*numbers)` and `stats(**options)` helpers.

### Day 13 · 01 Nov 2026 · Score Cleaner
- **Learn:** Comprehensions
- **Goal:** From raw `name:score` strings build clean lists/dicts with comprehensions only; drop invalid rows.
- **Stretch:** Group names by grade with a dict comprehension.

### Day 14 · 02 Nov 2026 · Caesar and Vigenère Cipher
- **Learn:** String manipulation
- **Goal:** Encode/decode with a shift; keep case and punctuation.
- **Stretch:** Brute-force decode a Caesar text.

### Day 15 · 03 Nov 2026 · Password Generator
- **Learn:** Modules and the standard library
- **Goal:** Your own `passwords.py` module using `secrets`; length and character set options.
- **Stretch:** Passphrase mode from a word list.

### Day 16 · 04 Nov 2026 · Safe Calculator
- **Learn:** Exceptions: try/except/finally
- **Goal:** Expression calculator that never crashes: bad input, division by zero, overflow handled.
- **Stretch:** Custom error messages per exception type.

### Day 17 · 05 Nov 2026 · Daily Journal
- **Learn:** Reading and writing text files
- **Goal:** Write today's entry to a dated file, list and read past entries.
- **Stretch:** Search all entries for a word.

### Day 18 · 06 Nov 2026 · Countdown and Age
- **Learn:** datetime and time
- **Goal:** Days/hours to a chosen date, age in days, weekday you were born.
- **Stretch:** Live countdown that updates every second.

### Day 19 · 07 Nov 2026 · Quiz Game
- **Learn:** Nested data structures
- **Goal:** Questions as a list of dicts (question, options, answer, category); score per category.
- **Stretch:** Shuffle questions and options.

### Day 20 · 08 Nov 2026 · Hangman
- **Learn:** Milestone: Foundations
- **Goal:** Word list from a file, ASCII gallows, used letters, win/lose, play again.
- **Stretch:** Categories and a hint that costs a life.

## Block 2: Files, OOP & Testing (days 21–40)

Structure code with classes and modules, persist data, build real CLIs and prove behaviour with pytest.

### Day 21 · 09 Nov 2026 · File Organizer
- **Learn:** pathlib and os
- **Goal:** Move files of a folder into subfolders by extension; dry-run mode first.
- **Stretch:** Undo the last run from a log.

### Day 22 · 10 Nov 2026 · Expense Tracker
- **Learn:** csv module
- **Goal:** Add expenses to a CSV, monthly total and total per category.
- **Stretch:** Export a filtered CSV.

### Day 23 · 11 Nov 2026 · Todo App with JSON
- **Learn:** json module
- **Goal:** Todos with id, title, done, created; persisted in JSON.
- **Stretch:** Due dates and overdue list.

### Day 24 · 12 Nov 2026 · Todo CLI
- **Learn:** argparse
- **Goal:** Turn day 23 into `todo add/list/done/remove` subcommands with help texts.
- **Stretch:** `--json` output flag.

### Day 25 · 13 Nov 2026 · Bank Account
- **Learn:** Classes and objects
- **Goal:** `Account` with deposit, withdraw, balance, transaction list; refuse overdraft.
- **Stretch:** Monthly statement printout.

### Day 26 · 14 Nov 2026 · Shapes
- **Learn:** Inheritance and polymorphism
- **Goal:** `Shape` base with `area()`/`perimeter()`; circle, rectangle, triangle; sort by area.
- **Stretch:** Abstract base class with `abc`.

### Day 27 · 15 Nov 2026 · Money Class
- **Learn:** Dunder methods
- **Goal:** `Money(amount, currency)` with `+`, `-`, `==`, `<`, `repr`, `str`; mixing currencies raises.
- **Stretch:** Exchange-rate aware addition.

### Day 28 · 16 Nov 2026 · Library Manager
- **Learn:** dataclasses
- **Goal:** Books and members as dataclasses; borrow/return rules, due dates.
- **Stretch:** Frozen dataclasses and `field(default_factory=...)`.

### Day 29 · 17 Nov 2026 · Smart Thermostat
- **Learn:** Properties and encapsulation
- **Goal:** Temperature with validated setter, Celsius/Fahrenheit properties, modes.
- **Stretch:** Schedule by hour.

### Day 30 · 18 Nov 2026 · Inventory System
- **Learn:** Custom exceptions
- **Goal:** Stock in/out with `OutOfStockError`, `UnknownItemError`; clear messages.
- **Stretch:** Low-stock report.

### Day 31 · 19 Nov 2026 · Tested Bank Account
- **Learn:** pytest basics
- **Goal:** Write pytest tests for day 25 (happy path, overdraft, history); fix any bug you find.
- **Stretch:** Fixtures and `pytest.raises`.

### Day 32 · 20 Nov 2026 · String Calculator Kata
- **Learn:** Test-driven development
- **Goal:** Write the test first for each rule of the String Calculator kata, then the code.
- **Stretch:** Parametrized tests.

### Day 33 · 21 Nov 2026 · Log Reader
- **Learn:** Iterators and generators
- **Goal:** Generator that streams a large log file and yields parsed records; filter by level.
- **Stretch:** Custom iterator class for a countdown.

### Day 34 · 22 Nov 2026 · Timer and Retry
- **Learn:** Decorators
- **Goal:** `@timer`, `@retry(times=3)` and `@cache` decorators applied to slow/flaky functions.
- **Stretch:** Decorator with arguments and `functools.wraps`.

### Day 35 · 23 Nov 2026 · Resource Helpers
- **Learn:** Context managers
- **Goal:** `Timer` context manager, temporary directory helper, `contextlib.contextmanager` version.
- **Stretch:** Suppress and log specific exceptions.

### Day 36 · 24 Nov 2026 · Backup Script
- **Learn:** logging
- **Goal:** Copy a folder to a dated backup with logging to console and file, levels configurable.
- **Stretch:** Rotating log files.

### Day 37 · 25 Nov 2026 · Contact Extractor
- **Learn:** Regular expressions
- **Goal:** Extract emails, phone numbers and URLs from a text file; validate formats.
- **Stretch:** Mask the found data in the output.

### Day 38 · 26 Nov 2026 · Word Frequency Analyzer
- **Learn:** collections
- **Goal:** `Counter`, `defaultdict`, `deque`: top words, words by first letter, last N lines.
- **Stretch:** Bigram counts.

### Day 39 · 27 Nov 2026 · Typed Contact Book
- **Learn:** Type hints and mypy
- **Goal:** Rewrite day 9 with full type hints, run mypy clean.
- **Stretch:** `TypedDict` / `Protocol`.

### Day 40 · 28 Nov 2026 · Personal Finance CLI
- **Learn:** Milestone: OOP & Testing
- **Goal:** Accounts, transactions, categories; JSON storage; argparse CLI; reports; pytest suite.
- **Stretch:** CSV import from your bank export.

## Block 3: Automation, Web & APIs (days 41–60)

Talk to the outside world: HTTP APIs, scraping, files of every kind, databases, concurrency and bots.

### Day 41 · 29 Nov 2026 · Weather CLI
- **Learn:** HTTP with requests
- **Goal:** City → current weather and 3-day forecast from Open-Meteo (no key).
- **Stretch:** Cache responses for 10 minutes.

### Day 42 · 30 Nov 2026 · GitHub Profile Stats
- **Learn:** Working with JSON APIs
- **Goal:** User's repos, stars, top languages via GitHub REST API; handle pagination.
- **Stretch:** Optional token from env var for higher limits.

### Day 43 · 01 Dec 2026 · Currency Converter
- **Learn:** Environment variables and config
- **Goal:** Live rates from an API, defaults from a `.env`/config file, offline fallback.
- **Stretch:** Rate history for a week.

### Day 44 · 02 Dec 2026 · Quote Scraper
- **Learn:** Web scraping with BeautifulSoup
- **Goal:** Scrape all pages of quotes.toscrape.com to JSON (text, author, tags).
- **Stretch:** Author detail pages.

### Day 45 · 03 Dec 2026 · Book Price Tracker
- **Learn:** Polite scraping
- **Goal:** books.toscrape.com: prices and ratings to CSV with delays, headers and robots.txt check.
- **Stretch:** Detect price changes between runs.

### Day 46 · 04 Dec 2026 · Uptime Monitor
- **Learn:** Scheduling
- **Goal:** Check a list of URLs every N minutes, log status codes and response times.
- **Stretch:** Alert after 3 consecutive failures.

### Day 47 · 05 Dec 2026 · Reminder Mailer
- **Learn:** Sending email
- **Goal:** Send yourself a daily summary email with smtplib (credentials from env).
- **Stretch:** HTML email with a table.

### Day 48 · 06 Dec 2026 · Bulk Image Tool
- **Learn:** Images with Pillow
- **Goal:** Resize, convert and watermark all images in a folder.
- **Stretch:** Generate thumbnails contact sheet.

### Day 49 · 07 Dec 2026 · PDF Toolkit
- **Learn:** PDF files
- **Goal:** Merge, split and extract text from PDFs (pypdf).
- **Stretch:** Add page numbers.

### Day 50 · 08 Dec 2026 · Excel Report
- **Learn:** Excel files
- **Goal:** Generate a formatted Excel report from day 22's CSV with openpyxl, including totals.
- **Stretch:** Add a chart sheet.

### Day 51 · 09 Dec 2026 · Project Archiver
- **Learn:** subprocess and shutil
- **Goal:** Zip a project without venv/cache, run `git log` via subprocess and include a summary.
- **Stretch:** Exclude rules from `.gitignore`.

### Day 52 · 10 Dec 2026 · Concurrent Downloader
- **Learn:** Threading
- **Goal:** Download a list of files with a thread pool; progress and timing vs sequential.
- **Stretch:** Resume partial downloads.

### Day 53 · 11 Dec 2026 · Async Link Checker
- **Learn:** asyncio
- **Goal:** Crawl one site's links asynchronously (httpx/aiohttp) and report broken ones.
- **Stretch:** Limit concurrency with a semaphore.

### Day 54 · 12 Dec 2026 · Notes App
- **Learn:** sqlite3
- **Goal:** Notes with tags in SQLite: add, search, edit, delete; parameterized queries.
- **Stretch:** Full-text search (FTS5).

### Day 55 · 13 Dec 2026 · Movie Watchlist
- **Learn:** SQL relations
- **Goal:** Movies, people, watch history tables with joins; top lists.
- **Stretch:** Import from a CSV.

### Day 56 · 14 Dec 2026 · Telegram Notifier Bot
- **Learn:** Building a bot
- **Goal:** Bot that answers `/weather` and `/quote` using your earlier code (Bot API over HTTP).
- **Stretch:** Inline keyboard buttons.

### Day 57 · 15 Dec 2026 · Terminal Dashboard
- **Learn:** Rich terminal UIs
- **Goal:** Rich/Typer dashboard showing weather, todos and GitHub stats from earlier days.
- **Stretch:** Live refresh layout.

### Day 58 · 16 Dec 2026 · My Utils Package
- **Learn:** Packaging
- **Goal:** Collect helpers from earlier days into an installable package with `pyproject.toml`.
- **Stretch:** Console script entry point.

### Day 59 · 17 Dec 2026 · Batch Renamer
- **Learn:** Config files and CLIs
- **Goal:** Rename files by rules from a TOML config (`tomllib`), preview before applying.
- **Stretch:** Undo file.

### Day 60 · 18 Dec 2026 · Price Tracker Bot
- **Learn:** Milestone: Automation
- **Goal:** Scrape prices on a schedule, store history in SQLite, notify on Telegram when a price drops.
- **Stretch:** Weekly chart sent as image.

## Block 4: Data & Machine Learning (days 61–80)

Load, clean, analyse and visualise real data, then train and evaluate first models.

### Day 61 · 19 Dec 2026 · Dice Simulator
- **Learn:** Jupyter and NumPy basics
- **Goal:** Simulate 100k dice rolls with NumPy, compare to theory.
- **Stretch:** Two-dice sum distribution.

### Day 62 · 20 Dec 2026 · Grade Matrix
- **Learn:** NumPy arrays
- **Goal:** Students × exams matrix: averages, best per exam, normalization.
- **Stretch:** Broadcasting for curve grading.

### Day 63 · 21 Dec 2026 · Titanic Explorer
- **Learn:** pandas Series and DataFrame
- **Goal:** Load the Titanic CSV, inspect, select, filter and sort.
- **Stretch:** Survival rate by class and sex.

### Day 64 · 22 Dec 2026 · Messy Data Cleanup
- **Learn:** Data cleaning
- **Goal:** Fix types, missing values, duplicates and inconsistent text in a messy CSV.
- **Stretch:** A reusable `clean()` pipeline function.

### Day 65 · 23 Dec 2026 · Sales Report
- **Learn:** groupby and aggregation
- **Goal:** Monthly and per-product sales summaries from a sample dataset.
- **Stretch:** Pivot tables.

### Day 66 · 24 Dec 2026 · Movie Ratings
- **Learn:** Merging datasets
- **Goal:** Join movies and ratings (MovieLens small), top movies with minimum votes.
- **Stretch:** Genre breakdown.

### Day 67 · 25 Dec 2026 · Weather History
- **Learn:** Time series
- **Goal:** Daily weather of your city for 5 years (Open-Meteo archive): trends, rolling means.
- **Stretch:** Hottest week each year.

### Day 68 · 26 Dec 2026 · Expense Charts
- **Learn:** matplotlib
- **Goal:** Line, bar and pie charts of your day 22 expenses.
- **Stretch:** Save a multi-chart PDF.

### Day 69 · 27 Dec 2026 · Plotly Dashboard
- **Learn:** Interactive charts
- **Goal:** Interactive charts for the weather history data.
- **Stretch:** Dropdown to switch cities.

### Day 70 · 28 Dec 2026 · Earthquake Map
- **Learn:** Maps
- **Goal:** Latest earthquakes (USGS/AFAD API) on a folium map sized by magnitude.
- **Stretch:** Filter by date range.

### Day 71 · 29 Dec 2026 · Wikipedia Tables
- **Learn:** pandas.read_html and scraping to data
- **Goal:** Turn a Wikipedia table (e.g. Turkish cities population) into a clean DataFrame and chart.
- **Stretch:** Merge two tables.

### Day 72 · 30 Dec 2026 · Correlation Explorer
- **Learn:** Statistics basics
- **Goal:** Mean, median, std, correlation matrix and a heatmap for a dataset.
- **Stretch:** Simple hypothesis test with scipy.

### Day 73 · 31 Dec 2026 · Data App
- **Learn:** Streamlit
- **Goal:** Streamlit app to upload a CSV and explore it with filters and charts.
- **Stretch:** Download filtered data.

### Day 74 · 01 Jan 2027 · House Price Predictor
- **Learn:** scikit-learn: regression
- **Goal:** Linear regression on a housing dataset; train/test split; MAE/RMSE.
- **Stretch:** Feature scaling and comparison.

### Day 75 · 02 Jan 2027 · Titanic Survival
- **Learn:** Classification
- **Goal:** Logistic regression and decision tree; accuracy and confusion matrix.
- **Stretch:** Cross-validation.

### Day 76 · 03 Jan 2027 · Model Comparison
- **Learn:** Model evaluation
- **Goal:** Compare 3+ models on one dataset with a clean report.
- **Stretch:** Grid search.

### Day 77 · 04 Jan 2027 · Review Sentiment
- **Learn:** Text processing
- **Goal:** Bag-of-words sentiment classifier on a review dataset.
- **Stretch:** TF-IDF and top words per class.

### Day 78 · 05 Jan 2027 · Customer Segments
- **Learn:** Clustering
- **Goal:** K-means on a customer dataset, choose k, describe each segment.
- **Stretch:** PCA plot.

### Day 79 · 06 Jan 2027 · Prediction App
- **Learn:** Saving models
- **Goal:** Save a trained model (joblib) and serve predictions in a Streamlit form.
- **Stretch:** Input validation and explanation text.

### Day 80 · 07 Jan 2027 · Turkey Earthquakes Report
- **Learn:** Milestone: Data
- **Goal:** Collect → clean → analyse → visualise earthquake data; publish a Streamlit report.
- **Stretch:** Monthly automated refresh.

## Block 5: Web Apps, AI & Capstone (days 81–100)

Ship web apps and APIs, work with local LLMs, build games and finish with your own capstone.

### Day 81 · 08 Jan 2027 · Personal Homepage
- **Learn:** Flask basics
- **Goal:** Flask app with routes, templates and static files.
- **Stretch:** Dark mode toggle.

### Day 82 · 09 Jan 2027 · Guestbook
- **Learn:** Templates and forms
- **Goal:** Form with validation and flash messages; entries stored in SQLite.
- **Stretch:** Pagination.

### Day 83 · 10 Jan 2027 · Mini Blog
- **Learn:** ORM
- **Goal:** Flask + SQLAlchemy: posts, tags, create/edit/delete.
- **Stretch:** Markdown posts.

### Day 84 · 11 Jan 2027 · Todo REST API
- **Learn:** FastAPI basics
- **Goal:** CRUD endpoints for todos, automatic docs.
- **Stretch:** Filtering and sorting query params.

### Day 85 · 12 Jan 2027 · Book API
- **Learn:** Pydantic validation
- **Goal:** Validated models, error responses, nested schemas.
- **Stretch:** Settings with pydantic-settings.

### Day 86 · 13 Jan 2027 · Notes API with Login
- **Learn:** Authentication
- **Goal:** User signup/login with hashed passwords and JWT; private notes.
- **Stretch:** Refresh tokens.

### Day 87 · 14 Jan 2027 · API Test Suite
- **Learn:** Testing APIs
- **Goal:** pytest + TestClient tests for day 84/86 APIs.
- **Stretch:** Coverage report.

### Day 88 · 15 Jan 2027 · Dockerized API
- **Learn:** Docker
- **Goal:** Dockerfile and compose for the notes API with a database.
- **Stretch:** Multi-stage build.

### Day 89 · 16 Jan 2027 · Deploy the API
- **Learn:** Deployment
- **Goal:** Deploy one API to a free host or your own server with HTTPS.
- **Stretch:** Health check and uptime monitor from day 46.

### Day 90 · 17 Jan 2027 · Local Chat CLI
- **Learn:** Local LLMs with Ollama
- **Goal:** Chat with a local model through Ollama's HTTP API, streaming output, history.
- **Stretch:** System prompt presets.

### Day 91 · 18 Jan 2027 · Text Summarizer
- **Learn:** Prompting and structured output
- **Goal:** Summarize files into JSON (title, summary, keywords) and validate it.
- **Stretch:** Batch a whole folder.

### Day 92 · 19 Jan 2027 · Ask My Notes
- **Learn:** Embeddings and RAG
- **Goal:** Embed your notes, retrieve relevant chunks and answer questions with sources.
- **Stretch:** Re-index only changed files.

### Day 93 · 20 Jan 2027 · Mini Agent
- **Learn:** Tool calling
- **Goal:** LLM that can call your weather and calculator functions to answer questions.
- **Stretch:** Step log of each tool call.

### Day 94 · 21 Jan 2027 · Real-time Chat
- **Learn:** WebSockets
- **Goal:** FastAPI WebSocket chat room with usernames.
- **Stretch:** Message history in SQLite.

### Day 95 · 22 Jan 2027 · Job Runner
- **Learn:** Background jobs
- **Goal:** Queue long tasks (e.g. day 48 image jobs) and report progress.
- **Stretch:** Retry failed jobs.

### Day 96 · 23 Jan 2027 · Snake
- **Learn:** pygame basics
- **Goal:** Snake with growing tail, score and game over.
- **Stretch:** Speed increases with score.

### Day 97 · 24 Jan 2027 · Breakout
- **Learn:** pygame game loop
- **Goal:** Paddle, ball, bricks, lives and levels.
- **Stretch:** Power-ups.

### Day 98 · 25 Jan 2027 · Capstone (part 1)
- **Learn:** Capstone: plan and build
- **Goal:** Pick a project that solves your own problem; write the plan and build the core.

### Day 99 · 26 Jan 2027 · Capstone (part 2)
- **Learn:** Capstone: finish and test
- **Goal:** Finish, test and document the capstone.
- **Stretch:** Deploy it.

### Day 100 · 27 Jan 2027 · Challenge Showcase
- **Learn:** Showcase
- **Goal:** Generate `projects.json` from the day folders and publish the list on gorkemnet.com/challenges/python.
- **Stretch:** Screenshots or terminal recordings per project.
