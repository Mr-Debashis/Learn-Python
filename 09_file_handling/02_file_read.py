

# To open the demo.txt file, use the built-in open() function.
# The open() function returns a file object, which has a read() method for reading the content of the file:


myfile = open(r"C:\Users\D\Downloads\Learn-Python\09_file_handling\demo.txt")
print(myfile.read())

# It is a good practice to always close the file when you are done with it.
# If you are not using the with statement, you must write a close statement in order to close the file:
myfile.close()


# You can also use the with statement when opening a file:

with open(r"C:\Users\D\Downloads\Learn-Python\09_file_handling\demo.txt") as f:
  print(f.read())
  print(f.read(4))
  print(f.readline())