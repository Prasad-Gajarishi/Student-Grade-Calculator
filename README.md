# Grade Calculator

A simple command-line Python program that calculates a student's total marks, average, percentage, grade, and pass/fail status across five subjects — with input validation for names, marks, and menu choices.

## Features

- Calculates results for **Maths, Science, English, History, and Geography**
- Validates the student's **name** (must be in "First Last" format, letters only — no numbers or symbols)
- Validates **marks** (must be a whole number between 0 and 100 — no decimals, letters, or symbols)
- Computes:
  - Total marks (out of 500)
  - Average marks
  - Percentage
  - Highest and lowest scoring subjects
- Assigns a **grade** based on percentage:
  | Percentage | Grade |
  |------------|-------|
  | 90% and above | A+ |
  | 80% – 89% | A |
  | 70% – 79% | B+ |
  | 60% – 69% | B |
  | 50% – 59% | C |
  | Below 50% | D |
- Declares **Pass/Fail** status (pass mark: 36%)
- Prints a formatted **Student Report Card**
- Lets you calculate results for **multiple students** in one run, with a strict **Y/N** prompt to continue or exit

## Requirements

- Python 3.x (no external libraries needed)

## How to Run

```bash
python grade_calculator.py
```

## Usage Flow

1. Enter the student's name (first and last name, letters only).
2. Enter marks for each subject (0–100, whole numbers only).
3. View the calculated total, average, percentage, grade, and pass/fail status.
4. View the formatted report card.
5. Enter `Y` to calculate another student's result, or `N` to exit.

## Input Validation Rules

| Input | Rule | Example of Invalid Input |
|-------|------|---------------------------|
| Name | Must contain first and last name, letters only | `John3`, `John`, `John_Smith`, (empty) |
| Marks | Whole number between 0 and 100 | `85.5`, `abc`, `-10`, `150`, `#90` |
| Continue prompt | Only `Y` or `N` (case-insensitive) accepted | `yes`, `3`, `maybe` |

## Sample Output

```
===================================================
          Welcome to the Grade Calculator
===================================================
Enter your name (First Last): john smith
Welcome John Smith
Please enter your marks for the following subjects out of 100:
Enter your marks for Maths: 85
Enter your marks for Science: 90
Enter your marks for English: 78
Enter your marks for History: 88
Enter your marks for Geography: 92

==================================================
           STUDENT REPORT CARD
==================================================
Student Name      : John Smith

Total Marks       : 433/500
Average Marks     : 86.60
Percentage        : 86.60%

Highest Marks     : 92 (Geography)
Lowest Marks      : 78 (English)
==================================================

Do you want to calculate another student's result? (Y/N):
```

## File Structure

```
grade_calculator.py   # Main program
README.md             # Project documentation
```
