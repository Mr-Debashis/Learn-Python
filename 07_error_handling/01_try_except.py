
# The *try block lets you test a block of code for errors.
# The *except block lets you handle the error.
# The *else block lets you execute code when there is no error.
# The *finally block lets you execute code, regardless of the result of the try- and except blocks.



# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:

try:
  print(x)   # here we got an error with try except
except:
  print("An exception occurred")

# Since the try block raises an error, the except block will be executed.
# Without the try block, the program will crash and raise an error:


## You can use the else keyword to define a block of code to be executed if no errors were raised:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")



## The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")