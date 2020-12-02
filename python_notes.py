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

#################################

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

#################################

# Printing in Python

## Print a string
print("string here! fancy")
first_name = "Kristohper"
print("my name is " + first_name)

# Printing can be strung together with commas as well
print("my name is",first_name)

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

#################################

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

#################################

# Python Syntax Basics

## Function Definitions and Calls
def add(x,y):
    z = x + y
    return z

def makeStuff(name='', time=0): # set default when declaring a param

new_num = add(4,5)
print(new_num)

def funInFunction(arg, *args): # the asterisk is called the splat operator
    print(arg," and ",*args) # *args appear as a tuple

def anotherFunction(*args,**kwargs): # arguments and key-word arguments
    print(*args)

## Classes
class User:
    def __init__(self):
        self.name = "Kristopher" # classes have attributes
        self.role = "Software Engineer"

person = User() # to make a new instance of the class
print(person.name,person.role) # attributes accessed

class User:
    def __init__(self, name, role, status): # called when object is constructed
        self.name = name
        self.role = role
        self.status = status
        self.account_balance = 0

    def deposit_funds(self, amount): # classes have methods
        self.account_balance += amount

candidate = User("Kristopher","Software Engineer","Hired")
print(candidate.name)
candidate.deposit_funds(500) # print(candidate.account_balance) -> 500

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

## Tuples
new_tuple = (1,'cat',15,21) # immutable

## Dictionary
new_dict = {} # very fast lookups
new_employee = {'name':'Kristopher Merolla','position':'Full Stack Software Engineer'}

## Set
x = set() # very fast lookups
y = {5,4,2,2,6}

## Common Functions
type(val)
len('string')
str(42)
int("42")

#################################

# Modules

## Python standard library of modules: https://docs.python.org/3.9/library/index.html

## Modules are Python files (.py) containing a set of functions, used in code via the 'import' command
import moduleNameHere

### Example -> urllib.request module enables reading of request data from a URL
import urllib.request
response = urllib.request.urlopen("http://www.google.com")
html = response.read()
print(html)

## Modules can be created and imported into other Python files as needed
### Example -> create a file like "calcs.py" and import it into user
import calcs # import the path, if in same directory write this way
print(calcs.rate(5,10,15,20))

#################################

# Packages

# A package is a collection of modules and are similarly imported (two ways)
import my_mods.test_mod
from my_mods import test_mod

## Example hierarchy
my_project
     |_____ python_stuff.py
     |_____ my_mods
               |_____ __init__.py # init can be used to restrict what mods are available
               |_____ test_mod.py
               |_____ another_mod.py
               |_____ final_mod.py

#################################

# Test Driven Development (TDD)

## Python Test cases methods: https://docs.python.org/3.9/library/unittest.html#test-cases

## Unlike the traditional development cycle of design -> build -> test -> repeat,
## TDD has the writing of a test to fail before then writing code to pass the test,
## code can then be refactored as needed to improve overall functionality

## Python testing framework
import unittest # import the python testing framework

def isEven(n): ## Example function isEven which is tested
    if n % 2 == 0:
       return True
    else:
       return False

class IsEvenTests(unittest.TestCase): ## Unit test (test_even.py)
    # each method in this class is a test to be run
    def testTwo(self):
        self.assertEqual(isEven(2), True)
        # another way to write above is
        self.assertTrue(isEven(2))
    def testThree(self):
        self.assertEqual(isEven(3), False)
        # another way to write above is
        self.assertFalse(isEven(3))
    # any task you want run before any method above is executed, put them in the setUp method
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main() # this runs our tests

