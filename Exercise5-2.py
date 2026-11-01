# Tests for equality and inequality with strings
car = 'Toyota'

print(car == 'Toyota')
print(car != 'Honda')

# Tests using the lower() method
name = 'RAYA'

print(name.lower() == 'raya')
print(name.lower() == 'JUNA')

# Numerical tests
number = 20

print(number == 20)
print(number != 20)
print(number > 10)
print(number < 10)
print(number >= 20)
print(number <= 15)

# Tests using and and or
age = 18

print(age > 15 and age < 20)
print(age < 10 and age > 5)

print(age == 18 or age == 20)
print(age == 10 or age == 12)

# Test whether an item is in a list
fruits = ['apple', 'banana', 'orange']

print('apple' in fruits)
print('mango' in fruits)

# Test whether an item is not in a list
print('mango' not in fruits)
print('banana' not in fruits)