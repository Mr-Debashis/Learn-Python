

# A function is a block of code which only runs when it is called.
# A function can return data as a result.
# A function helps avoiding code repetition.

# In Python, a function is defined using the def keyword, followed by a function name and parentheses:
def my_function(parameater):
  print("Hello from a function")

my_function('hello')


#### Return Keyword:----
# Functions can send data back to the code that called them using the return statement.
# When a function reaches a return statement, it stops executing and sends the result back:

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

#### Pass Keyword:----
# Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:

def my_function():
  pass



# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

#### Parameters vs Arguments
# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the actual value that is sent to the function when it is called.

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument