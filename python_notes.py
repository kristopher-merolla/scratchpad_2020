#################################
## -- Notes on Python (Mac) -- ##
#################################

# Creating a python virtual environment
python3 -m venv py3Env 

## Activate the envitonment (cd py3Env)
source py3Env/bin/activate

## Exit the environment
deactivate

# Package management with pip

## Check what packages are installed
pip3 list

## Create a reqirements file for packages
pip3 freeze > requirements.txt

## Install a package
pip3 install {{package_name}}
## example: pip3 install Django==2.2.4

## Uninstall a package
pip3 uninstall {{package_name}}
## example: pip3 uninstall Django

## Display information on a package
pip3 show {{package_name}}
## example: pip3 show Django

## Search for a package by name
pip3 search Flask
## example: pip3 search Flask


# Python Shell Commands

## Activating Pyton Shell
python

## Exit the shell
exit()

## Make a new python file
touch {{file_name}}.py
## example: touch hello_world.py

## Executing python file
python {{file_mame}}.py
## example: python hello_world.py


# Printing in Python

## Print a string
print("string here! fancy")
first_name = "Kristohper"
print("my name is " + first_name)

### F-Strings (Literal String Interpolation)
#### Python 3.6 introduced f-strings for string interpolation
print(f"My name is {first_name}")

### Prior to f-strings use string.format()
favorite_number = 5
print("My name is {} and my favorite number is {}".format(first_name, favorite_number))

### Prior to format interpolation
hello_world = "Hello %s" % "World"
python_view = "I love Python %d" % 3 
print(hello_world, python_view)


# String Methods

## Python has a number of built-in methods for strings
https://docs.python.org/3/library/stdtypes.html

### Commonly used string methods
string.lower()
string.count(substr)
string.split(char)
string.find(substr)
string.isalnum()
string.endswith(substr)


# Python Syntax Basics

## Function Definitions and Calls
def add(x,y):
    z = x + y
    return z

def makeStuff(name='', time=0): # set default when declaring a param

new_num = add(4,5)
print(new_num)

## Classes
class EmptyClass:
    pass

## Conditionals and Loops
if x < 5:
    print("smaller")
elif x > 15:
    print("larger")
else:
    pass

count = 0
while count < 5:
    print("we're at ", count)
    count += 1
else:
    pass

for val in my_string:
    pass

for val in "string":
    if val == "i":
        break # exits inner-most loop
    print(val)

for val in "string":
    if val == "i":
        continue # goes back to start of loop
    print(val)

for x in range(0, 5, 1):
    pass

for x in range(0, 10):	# increment of +1 implied
    pass

for x in range(10):	# increment of +1, start at 0 implied
    pass

for x in new_dict:
    print(k)
    print(new_dict[k])

for key in new_dict.keys():
     print(key)

for val in new_dict.values():
     print(val)

for key, val in new_dict.items():
     print(key, " = ", val)


## Boolean
can_code = True
is_sleepy = False

## Numbers
favorite_number = 5

## Strings
name = "Kristopher Merolla"

## Tuble (immutable data type; can contain mixed data types)
pet = ("Morty","bull terrier",2,True)

## List
new_list = []
people = ["Brittany","Kristopher","Morty","Harper"]
people.append("Jon")
people.pop()
people.pop(1)

arr = [1,3,5,7]
arr[0], arr[1] = arr[1], arr[0] # swapping elements in a list

## Dictionary
new_dict = {}
new_employee = {'name':'Kristopher Merolla','position':'Full Stack Software Engineer'}

## Common Functions
type(val)
len('string')
str(42)
int("42")

