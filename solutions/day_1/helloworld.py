# Exercises - Day 1

# Exercises level 1:
## The level 1 exercises are meant to be completed through the Python interactive shell.

# Exercises level 2:
## 1.
import sys
import platform

## Opción 1: Utilizando la librería sys
print(f'Versión de Python: {sys.version}')
print(f'Versión de Python: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}')

## Opción 2: Utlizando la librería platform
print(f'Versión de Python: {platform.python_version()}')

## 2.
print('Addition:', 3+4)
print('Subtraction:', 3-4)
print('Multiplication:', 3*4)
print('Modulus:', 3%4)
print('Division:', 3/4)
print('Exponential:', 3**4)
print('Floor division operator:', 3//4)

## 3.
message = input('Enter the following data in one line separated by spaces:\n* Your name.\n* Your family name.\n* Your country.\n')
data1, data2, data3 = message.split()
print('Your name is', data1)
print('Your family name is', data2)
print('Your country is', data3)
print('''I'm enjoying 30 days of Python''')

## 4.
print(f'Data type of 10: {type(10)}')
print(f'Data type of 9.8: {type(9.8)}')
print(f'Data type of 3.14: {type(3.14)}')
print(f'Data type of 4-4j: {type(4-4j)}')
print(f"Data type of ['Asabeneh', 'Python', 'Findland']: {type(['Asabeneh', 'Python', 'Findland'])}")
print(f'Data type of data1: {type(data1)}')
print(f'Data type of data2: {type(data2)}')
print(f'Data type of data3: {type(data3)}')

# Exercises level 3:
print(f"Example of integer: {254}")
print(f"Example of float: {2.71}")
print(f"Example of complex: {3+4j}")
print(f"Example of string: {'River Plate'}")
print(f"Example of boolean: {True}")
print(f"Example of list: {['River Plate', 9.12, True]}")
print(f"Example of tuple: {(9, 18, 12)}")
print(f"Example of set: {{9, 18, 12}}")
print(f"Example of dictionary: {{(9, 12, 18): 'Cagó Boca', 3: True}}")

print("\nPequeño ejemplo de cómo utlizar un diccionario: ")
true_tuple = {(9, 12, 18): 'Cagó Boca', 3: True}
print(true_tuple[(9, 12, 18)])
print("\n")

import math

first_point = (2, 3)
second_point = (10, 8)
euclidian_distance = math.sqrt((second_point[0] - first_point[0])**2 + (second_point[1] - first_point[1])**2)

print(f"The Euclidian Distance between the point {first_point} and {second_point} is {euclidian_distance:.2f}")
