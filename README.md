1. Even or Odd Checker Program
File
Intergerinput.py

Description
This program:

Prompts the user to enter an integer.

Uses if-else statement to check whether the number is even or odd

Displays the result with clear messaging

How It Works
The program uses input() to read a number from the user

Converts the input to int using int()

Uses the modulo operator % to check if the number is divisible by 2:

If number % 2 == 0: prints "even"

Else: prints "odd"

Displays result like: 7 is an odd number.

Example Interaction
text
Enter an integer: 7
7 is an odd number.

Enter an integer: 10
10 is an even number.
2. Sum of Numbers Program
File
for_loop_addition.py (or sum_1_to_50.py)

Description
This program:

Uses a for loop to iterate over numbers from 1 to 50

Calculates the sum of all integers in this range

Displays the final sum (1275)

How It Works
Initializes total_sum = 0

Uses for i in range(1, 51): to iterate from 1 to 50

Accumulates the sum with total_sum += i in each iteration

Prints the final result using the formula 
50
×
51
2
=
1275
2
50×51
 =1275

Example Interaction
text
The sum of integers from 1 to 50 is: 1275
How to Run the Programs
Make sure Python is installed on your system.

Intergerinput.py

for_loop_addition.py

Open a terminal or command prompt in the directory where the files are saved.

Run each program with:

bash
python Intergerinput.py
python for_loop_addition.py
Learning Objectives
User input with input() and type conversion

Conditional statements (if-else)

For loops with range()

Modulo operator (%) for even/odd checking

Variable accumulation pattern with +=
