# Conditionals and iteration
x = int(input("Enter an integer: "))
if x % 2 == 0:
    print(x, "is an even number")
else:
    print(x, "is an odd number")

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = sum(filter(lambda x: x % 2 == 0, lst))
print("Sum of even numbers in the list:", even_sum)

# Type casting
x = input("Enter a string: ")
y = int(x)
print("Integer value of the string:", y)

x = input("Enter a float: ")
y = int(float(x))
print("Integer value of the float:", y)

# Exceptions
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print("Result of division:", x / y)
except ZeroDivisionError:
    print("Cannot divide by zero")

try:
    x = input("Enter a string: ")
    y = int(x)
    print("Integer value of the string:", y)
except ValueError:
    print("Invalid input")

# Functions, builtin functions
lst = [1, 2, 3, 4, 5]
print("Maximum value in the list:", max(lst))

x = input("Enter a string: ")
print("Length of the string:", len(x))

# Lambda functions
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_lst = list(filter(lambda x: x % 2 == 0, lst))
print("List of even numbers:", even_lst)