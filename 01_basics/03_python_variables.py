# Variables are containers for storing data values.
# Python has no command for declaring a variable. A variable is created the moment you first assign a value to it.

x = 5
y = "John"

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
a = 4       # x is of type int
b = "Debashis" # x is now of type str


# You can get the data type of a variable with the type() function.

print(type(x))
print(type(y))

# Variable names are case-sensitive.

NAME = "Rahul"
name = "Denashis"

print(name)
print(NAME)


# ++++++++++++++++++++++++++++++++++ Variable Names ++++++++++++++++++++++++++++++++++++++++++++++++++

# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"