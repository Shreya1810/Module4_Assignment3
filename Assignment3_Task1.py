# Module 4: Functions & Modules in Python
# Task 1: Calculate Factorial Using a Function
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")