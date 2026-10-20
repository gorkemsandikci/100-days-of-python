# Day #001 - Greeting Card

## What it does
A simple CLI application that asks for the user's name and birth year, calculates their current age, and prints a formatted greeting card to the terminal.

## How to run
```bash
python main.py
```

## What I learned
- `input()` always returns a string; used `int()` to convert before doing math
- `f-strings` are cleaner than string concatenation with `+`
- Used `datetime` to get the current year instead of hardcoding it
- Used `max()` with `len()` to find the longest line width
- Used `ljust()` to pad `lines` to the same length
- Added a stretch goal: built an `ASCII-art` border using a for loop

## What was hard
- Not knowing whether to use `time` or `datetime` to get the current year
## Stretch goals
- [x] Add an ASCII-art border that dynamically fits the longest line.
