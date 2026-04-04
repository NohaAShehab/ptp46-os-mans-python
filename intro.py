'this is the first string without ref in script --> add documentation of the script __  -> python store __doc__'
import sys

name = 'ahmed'
age  = 22
track = 'python'

# this comment
"this a string "  # this string is treated like a comment

print(__doc__)


bio = ("My name is Noha"
       "I works at iti")
print(bio)

# I need to define multi-line string ??


bio = ("My name is Noha\n"
       "I works at iti")
print(bio)

# wrap your string between  ''' qoutes , """
bio2 = """My name is Noha
I works at iti
I lives in Mansoura"""
print(bio2)


# if = "10"  # SyntaxError: invalid syntax
# print = "iti"

# print("hello")  # TypeError: 'str' object is not callable

if name == "Noha" :
    print('Hi')
else:
    print("Bye")



print(type(name))  # <class 'str'>

"""
    All datatypes in python are classes 
    all variables you create are object from classes 

    all classes in python, implicitly inherits from class object 
"""

print(isinstance(name, str))

print(isinstance(name, object))


# type casting ? --> change type ===> runtime
year = '2026'
print(type(year))

# convert it to int ?
year = int(year)
print(type(year))


""" """
name = "Noha"
print(type(name))
#
# name = int(name)# ValueError: invalid literal for int() with base 10: 'Noha'
# print(type(name))

name= ''
# print(int(name))

print(sys.getsizeof(name))
num  = 10
print(sys.getsizeof(num))