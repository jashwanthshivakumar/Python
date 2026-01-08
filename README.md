# Simple Python Practice Programs

This repository contains two Python programs:

1. An even or odd number checker that determines whether a user-entered integer is even or odd.
2. A program that calculates the sum of integers from 1 to 50 using a `for` loop.

---

## 1. Even or Odd Checker Program

### File

`Intergerinput.py`

### Description

This program:

* Prompts the user to enter an **integer**.
* Determines whether the entered number is **even or odd**.
* Displays the result using a clear and descriptive message.

### How It Works

1. The program uses `input()` to read a number from the user.
2. The input is converted to an integer using `int()`.
3. The program uses the modulo operator `%` to check divisibility by 2:

   * If `number % 2 == 0`, the number is even.
   * Otherwise, the number is odd.
4. The result is printed in sentence form.

### Example Interaction

```text
Enter an integer: 7
7 is an odd number.
```

```text
Enter an integer: 10
10 is an even number.
```

---

## 2. Sum of Numbers Program

### File

`for_loop_addition.py`

### Description

This program:

* Uses a `for` loop to iterate through numbers from **1 to 50**.
* Calculates the sum of all integers in this range.
* Displays the final result.

### How It Works

1. A variable named `total_sum` is initialized to 0.
2. The program uses `for i in range(1, 51)` to loop from 1 to 50.
3. Each number is added to `total_sum` using the `+=` operator.
4. After the loop completes, the final sum is printed.

The expected result is:

```
50 × 51 ÷ 2 = 1275
```

### Example Output

```text
The sum of integers from 1 to 50 is: 1275
```

---

## Learning Objectives

These programs demonstrate the following Python concepts:

* User input using `input()`
* Data type conversion with `int()`
* Conditional statements (`if-else`)
* For loops with `range()`
* Modulo operator (`%`) for even and odd checking
* Accumulating values using the `+=` operator

---
