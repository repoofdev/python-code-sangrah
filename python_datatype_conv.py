# -*- coding: utf-8 -*-

# Int
number_of_apples = 5
print("There are", number_of_apples, "apples in the basket")
print(type(number_of_apples))

#Float
apple_price = 0.99
print("Apple price:", apple_price, "Euros")
print("Type of apple_price variable:", type(apple_price))

# String Examples
greeting = "Hello, Python learners!"
course_name = 'Python Course!'
print(greeting)
print("Course:", course_name)

# Boolean/bool
is_student = True
is_weekend = False
print("Is student:", is_student)
print("Is it the weekend:", is_weekend)
print(type(is_student))

# Math Operations
# Two numbers
num1 = 15
num2 = 4
# Operations
sum_result = num1 + num2
difference_result = num1 - num2
division_result = num1 / num2
integer_division_result = num1 // num2 # Floor division (divides and rounds down to nearest integer
exponentiation_result = num1 ** num2
modulo_result = num1 % num2

# Displaying the results
print("Addition of", num1, "and", num2, "=", sum_result)
print("Subtraction of", num1, "from", num2, "=", difference_result)
print("Division of", num1, "by", num2, "=", division_result)
print("Integer division of", num1, "by", num2, "=", integer_division_result)
print("Exponentiation of", num1, "to the power of", num2, "=", exponentiation_result)
print("Modulo of", num1, "by", num2, "=", modulo_result)


# Implicit type conversion
num_int = 6 # Integer type
num_float = 1.5 # Float type
# Python automatically converts num_int to a float
total = num_int + num_float
print("Total:", total)
print("Type of total:", type(total))

# Explicit type conversion
# These variables are ``strings`` representing ``numbers``
salary_str = "1000"
tax_str = "200"
# Converting ``str`` variables to ``int``
salary_int = int(salary_str)
tax_int = int(tax_str)
# Now we can perform the subtraction with ``int`` variables
net_income = salary_int - tax_int
print("Net income: ", net_income)
