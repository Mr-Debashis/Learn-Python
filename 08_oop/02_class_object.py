
# A Class is like an object constructor, or a "blueprint" for creating objects.

# To create a class, use the keyword *class:

class Demo:
  x = 5

# Now we can use the class named Demo to create objects:
# Create an object named p1, and print the value of x:

p1 = Demo()
print(p1.x)


# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class Person:
  pass