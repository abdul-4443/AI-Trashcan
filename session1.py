
"""
Data Types &amp; Typecasting
Write a Python program that:
Declares a variable x = 15.7.
Converts x to an integer and a string, then prints all three values with appropriate labels.
"""
x = 15.7
i = int(x)
s = str(x)
print("x is a ", type(x), x)
print("x is a ", type(i), i)
print("x is a ", type(s), s)

"""
Math and Comparison Operators
Ask the user to input two numbers.
Compute and display their sum
"""

def takeInputInFloat():
    while True:
        a = input("Enter a number: ")
        try:
            num = float(a)
            return num
        except ValueError:
            print("Enter a valid number! Either an integer or a float")

num1 = takeInputInFloat()
num2 = takeInputInFloat()

print(num1 + num2)


"""
Ask the user to input their age and whether they are a student (True/False).
Use and, or, and not to check:
If the person is between 18 and 60 and is a student.
If the person is not a student or is younger than 18.

Print the result of each condition.
"""

def takeAge():
    while True:
        a = input("Enter your age: ")
        try:
            age = int(a)
            return age
        except ValueError:
            print("Enter a valid age in numerical value!")
          
s = input("You are a Student?(Y/N)").lower()
isStudent = (s == 'y' or s == 'Y' or s == 'true' or s == 't')
age = takeAge()
if age >= 18 and age <= 60 and isStudent:
    print("The user is between 18 and 60 and is a student")
elif not isStudent and age < 18 and age >= 0:
    print("The user is younger than 18 and is not a student")
else:
    print("The user doesn't have one of the two characteristics")


"""
Ifelifelse Statement
Write a program that takes a student’s marks (out of 100) and prints the grade:
90–100 → &quot;A&quot;
80–89 → &quot;B&quot;
70–79 → &quot;C&quot;
60–69 → &quot;D&quot;
Below 60 → &quot;F&quot;
Use if, elif, and else.
"""

marks = takeInputInFloat()
if marks >= 90 and marks <= 100:
    print("You got A grade")
elif marks >= 80:
    print("You got B grade")
elif marks >= 70:
    print("You got C grade")
elif marks >= 60:
    print("You got D grade")
elif marks < 60:
    print("You got F grade")
else:
    print("You entered invalid marks")


"""
While Loop with break
Write a program that keeps asking the user to enter numbers until they type 0.
If the user enters a negative number, print &quot;Negative numbers are not allowed.&quot; and exit
the loop immediately using break.
"""

def function1():
    while True:
        a = input("Enter a number: ")
        try:
            num = float(a)
            if num == 0:
                print("User entered 0")
                break
            if num < 0:
                print("Negative numbers are not allowed")
                break
            if num > 0:
                raise ValueError("User entered a postive number")
        except ValueError as e:
            print(e)

function1()


"""
For Loop with range()
Use a for loop with range() to print the multiplication table of 7 from 1 to 10 (i.e., 7 × 1,
7 × 2, ..., 7 × 10).
"""

for i in range(1, 11):
    print("7 * ", i, " = ", 7*i, " ")


"""
For Loop with range() arguments
Use for and range(start, stop, step) to:
Print all odd numbers from 1 to 15.
Print all even numbers from 20 down to 2 (in descending order).
"""
print("Odds: ")
for i in range(1, 16, 2):
    print(i, " ")
print("Evens: ")
for i in range(20, 1, -2):
    print(i, " ")


"""
Custom Function (No Return)
Define a function called greet_user(name, age) that:
Prints &quot;Hello, &lt;name&gt;! You are &lt;age&gt; years old.&quot;
Call the function with sample values from the user input.
"""
def takeName():
    while True:
        name = input("Enter your name: ")
        try:
            n = str(name)
            return n
        except ValueError:
            print("Invalid input! Try again.")

def greet_user(name, age):
    print("Hello, ", name, "! You are ", age, " years old.")

a = takeAge()
n = takeName()
greet_user(n, a)


"""
Custom Function with Return
Define a function calculate_area(length, width) that returns the area of a rectangle.
Ask the user to input length and width.
Call the function and print the result.
"""
def takeIntegerPos():
    while True:
        a = input("Enter a positive number: ")
        try:
            num = int(a)
            num = abs(num)
            return num
        except ValueError:
            print("Invalid! Try again")

print("Width")

width = takeIntegerPos()

print("Height")
height = takeIntegerPos()

print("Area = ", width * height)