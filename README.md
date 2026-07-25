# Grade Calculator

A simple command-line Python program that calculates a student's total marks, average, percentage, grade, and pass/fail status across five subjects — with full input validation for names, marks, and menu choices, and support for tied highest/lowest scores.

## Features

- Calculates results for **Maths, Science, English, History, and Geography**
- Validates the student's **name**:
  - Must be entered in "First Last" format (at least two words)
  - Only letters allowed — no numbers or symbols
  - Automatically formatted to proper case (e.g., `john smith` → `John Smith`)
- Validates **marks** for every subject:
  - Must be a whole number
  - Must be between 0 and 100
  - No decimals, letters, or symbols allowed
- Computes:
  - Total marks (out of 500)
  - Average marks
  - Percentage
  - Highest and lowest scoring subject(s)
    - If two or more subjects are tied for the highest or lowest marks, **all tied subjects are shown together** (e.g., `92 (Maths, Geography)`)
- Assigns a **grade** based on percentage (see [Grading Criteria](#grading-criteria))
- Declares **Pass/Fail** status (pass mark: 36%)
- Prints a formatted **Student Report Card**
- Supports calculating results for **multiple students** in a single run
- Validates the **continue prompt**: only accepts `Y` or `N` (case-insensitive) — any other input is rejected and re-asked

## Requirements

- Python 3.x
- No external/third-party libraries needed (uses only Python's built-in functions)

## How to Run

1. Save the script as `grade_calculator.py`
2. Open a terminal in the same folder
3. Run:
   ```bash
   python grade_calculator.py
   ```

## Usage Flow

1. Enter the student's name (first and last name, letters only).
2. Enter marks for each of the 5 subjects (0–100, whole numbers only).
3. View the calculated total, average, percentage, grade, and pass/fail status.
4. View the formatted report card, including highest/lowest marks and subject(s).
5. Enter `Y` to calculate another student's result, or `N` to exit the program.

## Input Validation Rules

| Input | Rule | Examples of Invalid Input |
|-------|------|----------------------------|
| Name | Must contain a first and last name, letters only, cannot be empty | `John3`, `John`, `John_Smith`, `123`, (empty) |
| Marks (each subject) | Must be a whole number between 0 and 100 | `85.5`, `abc`, `-10`, `150`, `#90` |
| Continue prompt | Only `Y` or `N` accepted (case-insensitive) | `yes`, `no`, `3`, `maybe`, `!` |

## Grading Criteria

| Percentage | Grade | Remark |
|------------|-------|--------|
| 90% and above | A+ | Excellent score |
| 80% – 89% | A | Good score |
| 70% – 79% | B+ | Average score |
| 60% – 69% | B | Below average score |
| 50% – 59% | C | Poor score |
| Below 50% | D | Fail |

**Pass criteria:** Percentage of 36% or above is required to pass the exam.

## Sample Output

```
===================================================
          Welcome to the Grade Calculator
===================================================
Enter your name (First Last): john smith
Welcome John Smith
Please enter your marks for the following subjects out of 100:
Enter your marks for Maths: 92
Enter your marks for Science: 90
Enter your marks for English: 78
Enter your marks for History: 88
Enter your marks for Geography: 92

==================================================
           STUDENT REPORT CARD
==================================================
Student Name      : John Smith

Total Marks       : 440/500
Average Marks     : 88.00
Percentage        : 88.00%

Highest Marks     : 92 (Maths, Geography)
Lowest Marks      : 78 (English)
==================================================

Do you want to calculate another student's result? (Y/N):
```

## File Structure

```
grade_calculator.py   # Main program
README.md             # Project documentation
```

## Notes

- The program runs in an infinite loop until the user chooses `N` at the "calculate another student" prompt.
- All marks are validated before any calculations are performed, so calculations never fail due to bad input.
- Tied subjects (for both highest and lowest marks) are displayed together, separated by commas.
