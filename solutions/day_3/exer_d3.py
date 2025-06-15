# Exercises day 3

# 1.
age = 25
print(f"Age variable: {age}\nData type: {type(age)}\n")

# 2.
height = 178.20
print(f"Height variable: {height}\nData type: {type(height)}\n")

# 3.
complex_number = 4 + 3j
print(f"Complex_number variable: {complex_number}\nData type: {type(complex_number)}\n")

# 4.
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area_of_a_triangle = (base * height)/2
print(f"The area of the triangle is {area_of_a_triangle:.2f}\n")

# 5.
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
print(f"The perimeter of the triangle is {side_a + side_b + side_c}\n")

# 6.
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"The area of the rectangle is {area}")
print(f"The perimeter of the rectangle is {perimeter}\n")

# 7.
import math

pi = math.pi
radius = float(input("Enter the radius of a circle: "))
circle_area = pi * radius ** 2
circle_circunference = 2 * pi * radius

print(f"Area of the circle: {circle_area:.2f}")
print(f"Circunference of the circle: {circle_circunference:.2f}\n")

# 8.
## The function is f(x) = y = 2x - 2 
## x = (y-2)/2 
## f(0) = y = -2; y = 0 -> 0 = 2x - 2 -> x = 2/2 = 1 
## y' = 2, so, that has to be the slope of the function

import random

## I'm going to provide three options to do this: 

### Lambda function: 
print("Testing the lambda function option: \n")
f_x = lambda x: 2 * x - 2 
f_y = lambda y: (y + 2) / 2

x_intercept_point = (f_y(0), 0)
y_intercept_point = (0, f_x(0))

arbitrary_domain_point = random.randint(0, 10000)
slope = (f_x(arbitrary_domain_point) - f_x(0))/(arbitrary_domain_point - 0)

print(f"Intercept in the x-axis: {x_intercept_point}")
print(f"Intercept in the y-axis: {y_intercept_point}")
print(f"Slope: {slope}\n")

### Classic function:
print("Testing the classic function option: \n")
def ff_x(x):
      return 2 * x - 2 

def ff_y(y):
      return (2 + y)/2

x_intercept_point = (ff_y(0), 0)
y_intercept_point = (0, ff_x(0))

arbitrary_domain_point = random.randint(0, 10000)

slope = (ff_x(arbitrary_domain_point) - ff_x(0))/(arbitrary_domain_point - 0)

print(f"Intercept in the x-axis: {x_intercept_point}")
print(f"Intercept in the y-axis: {y_intercept_point}")
print(f"Slope: {slope}\n")

### Using the SymPy library option, version 1:
print("Testing the SymPy library, version 1: \n")
from sympy import symbols, Eq, solve, diff

x, y = symbols('x y')

equation = Eq(y, 2 * x - 2)

x_intercept = solve(equation.subs(x, 0), y) # El resultado se almacena como una lista...
y_intercept = solve(equation.subs(y, 0), x)

x_intercept_point = (y_intercept[0], 0) # ... es por ello que tengo que acceder al elemento con un índice (en este caso, el primer elemento en 0 y no hay otro porque no es una ecuación con varias soluciones).
y_intercept_point = (0, x_intercept[0]) 

slope = diff(equation.rhs, x) # ¡Importante! Con "rhs" (right hand side) extraigo la parte derecha de la ecuación. Esto me permite derivar 2x-2.

print(f"Intercept int the x-axis: {x_intercept_point}")
print(f"Intercept int the y-axis: {y_intercept_point}")
print(f"Slope: {slope}\n")


### Using the SymPy library option, version 2:
print("Testing the SymPy library, version 2: \n")
from sympy import symbols, diff

x = symbols('x')

y = 2 * x - 2

x_intercept_point = (solve(y, x)[0], 0) # Equivale a resolver 2x - 2 = 0
y_intercept_point = (0, y.subs(x, 0))

slope = diff(y, x)

print(f"Intercept int the x-axis: {x_intercept_point}")
print(f"Intercept int the y-axis: {y_intercept_point}")
print(f"Slope: {slope}\n")

# 9.
point_a = (2, 2)
point_b = (6, 10)

slope_two_points_given = (point_b[1] - point_a[1]) / (point_b[0] - point_a[0])
euclidian_distance = math.sqrt((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2)

print(f"The slope between the points is: {slope_two_points_given}")
print(f"The euclidian distance of the points is: {euclidian_distance:.2f}\n")

# 10.
print(f"In task 8 the slope is {slope} and in task 9 is {slope_two_points_given}")

if slope > slope_two_points_given:
    print("The slope in task 8 is greater than the slope in task 9.")
elif slope < slope_two_points_given:
    print("The slope in task 9 is greater than the slope in thask 8.")
else:
    print("The slope in the two tasks are equal.")

print("\n")

# 11.
y = x ** 2 + 6 * x + 9

roots = solve(y, x, dict=True)

print(f"The roots of the function y = x² + 6x + 9: {roots}\n")

from sympy import factor
factored_y = factor(y)

print(f"Alternatively, we can factorize the expression y = x² + 6x + 9 --> y = {factored_y}")
print("... and obtain the image of the function in a given range of values.\n")

for domain_value in range(-10, 10):
    print(f"With x = {domain_value} --> y = {y.subs(x, domain_value)}")

print("\n")

# 12.
python_length = len("python")
dragon_length = len("dragon")

falsy_comparison = python_length != dragon_length

print(f"Is the length of 'Python' not equal to the length of 'dragon'? {falsy_comparison}\n")

# 13.
if 'on' in 'python' and 'on' in 'dragon':
    print("'on' is in both 'Python' and 'dragon'.\n")

# 14.
## Modifiqué un poco la consigna para ponerle un poco más de onda.
jargon = 'jargon' not in 'I hope this course is not full of jargon.'

if not jargon:
    print("You're safe")
else:
    print("Oh no...")

print("\n")

# 15.
this_is_not_the_truth = "on" not in "python" and "on" not in "dragon"

if this_is_not_the_truth:
    print("Ok, whatever...")
else:
    print("Did I just saw Shutter Island?")

print("\n")

# 16.
python_length = len("python")

print(f"Python length: {python_length}")
print(type(python_length))

python_length_as_float = float(python_length)

print(f"Python length: {python_length_as_float}")
print(type(python_length_as_float))

python_length_as_float_as_string = str(python_length_as_float)

print(f"Python length: {python_length_as_float_as_string}")
print(type(python_length_as_float_as_string))

print("\n")

# 17.
parity_checker = float(input("Enter a number so we can check if it is even or no: "))

if parity_checker % 2 == 0:
    print("Is even!!🥹")
else:
    print("Is not 😬")

print("\n")

# 18.
print(f"Floor division of 7 by 3: {7//3}")
print(f"Integer converted value of 2.7: {int(2.7)}\n")

# 19.
print(f"Data type of '10': {type('10')}")
print(f"Data type of 10: {type(10)}\n")

# 20.
if not int(float('9.8')) == 10:
    print("int(float('9.8')) is not equal to 10.")
else:
    print("int(float('9.8')) is equal to 10.")

print("\n")

# 21.
hours_of_work = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
weekly_earning = hours_of_work * rate_per_hour

print(f"Your weekly earning is: {weekly_earning:.4f}\n")

# 22.
years_lived = int(input("Enter the years you have lived: "))
seconds_in_a_year = 31536000

print(f"You have lived for {seconds_in_a_year * years_lived} seconds.\n")

# 23.
for n in range(1, 6):
    print(f"{n} {n**0} {n**1} {n**2} {n**3}")
