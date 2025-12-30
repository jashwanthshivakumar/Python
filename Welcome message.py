# Program to read first and last name and print a greeting

# 1. Take user's first name and last name as input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# 2. Concatenate first name and last name into a full name
full_name = first_name + " " + last_name

# 3. Print a personalized greeting using the full name
print("Hello, " + full_name.lower() + "!, Welcome to Python program")
