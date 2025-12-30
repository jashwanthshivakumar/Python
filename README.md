# Python

Here is a sample `README.md` you can use:

```markdown
# Simple Python Practice Programs

This repository contains two beginner-friendly Python programs:

1. A basic calculator that performs arithmetic operations on two numbers.
2. A name-based greeting program that reads the user's first and last name and prints a personalized message.

---

## 1. Basic Calculator Program

### File
`Calculator.py` (example name)

### Description
This program:

- Prompts the user to enter **two numbers**.
- Performs the following basic arithmetic operations on the numbers:
  - Addition
  - Subtraction
  - Multiplication
  - Division (with a check to avoid division by zero)
- Displays the result of each operation on the screen.

### How It Works
1. The program uses `input()` to read two values from the user.
2. The inputs are converted to `float` so decimal values are allowed.
3. It calculates:
   - `addition = num1 + num2`
   - `subtraction = num1 - num2`
   - `multiplication = num1 * num2`
   - `division = num1 / num2` (only if the second number is not zero)
4. The results are printed with clear labels for each operation.

### Example Interaction
```text
Enter the first number: 10
Enter the second number: 5

Results:
Addition:  15.0
Subtraction:  5.0
Multiplication:  50.0
Division:  2.0
```

If the second number is `0`, the program will print a message like:
```text
Division:  Undefined (cannot divide by zero)
```

---

## 2. Name Greeting Program

### File
`Welcome message.py` (example name)

### Description
This program:

- Prompts the user to enter their **first name** and **last name**.
- Concatenates the first and last name to form the **full name**.
- Prints a **personalized greeting** using the full name.

### How It Works
1. The program uses `input()` to ask for the first name and last name separately.
2. It concatenates them with a space in between:
   - `full_name = first_name + " " + last_name`
3. It prints a greeting message in the following format:
   - `hello john deer, welcome to python programe`
4. The program converts the full name to lowercase before printing to match the expected sample output.

### Example Interaction
```text
Enter your first name: John
Enter your last name: Deer
hello john deer, welcome to python programe
```

---

## How to Run the Programs

1. Make sure Python is installed on your system.
2. Save each program in its own `.py` file, for example:
   - `calculator.py`
   - `greeting.py`
3. Open a terminal or command prompt in the directory where the files are saved.
4. Run each program with:
   - `python Calculator.py`
   - `python Welcome message.py`
```
