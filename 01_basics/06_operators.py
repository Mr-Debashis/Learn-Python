# Operators are used to perform operations on variables and values. There are several types of operators exsits in python


# ++++++++++++++++++++++++++++++++++++++ Arithmetic Operators ++++++++++++++++++++++++++++++++++++++++++++

# Arithmetic operators are used with numeric values to perform common mathematical operations:
#      +	Addition	
#      -	Subtraction	
#      *	Multiplication
#      /	Division (returns a float value)
#      %	Modulus	
#      **	Exponentiation
#      //	Floor division (returns a integer value)
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)


# ++++++++++++++++++++++++++++++++++++++ Assignment Operators ++++++++++++++++++++++++++++++++++++++++++++

# Assignment operators are used to assign values to variables:
#       =	    x = 5	    x = 5	
#       +=	    x += 3	    x = x + 3	
#       -=	    x -= 3	    x = x - 3	
#       *=	    x *= 3	    x = x * 3	
#       /=	    x /= 3	    x = x / 3	
#       %=	    x %= 3	    x = x % 3	
#       //=	    x //= 3	    x = x // 3	
#       **=	    x **= 3	    x = x ** 3	
#       &=	    x &= 3	    x = x & 3	
#       |=	    x |= 3	    x = x | 3	
#       ^=	    x ^= 3	    x = x ^ 3	
#       >>=	    x >>= 3	    x = x >> 3	
#       <<=	    x <<= 3	    x = x << 3	


# ++++++++++++++++++++++++++++++++++++++ Comparison Operators ++++++++++++++++++++++++++++++++++++++++++++

# Comparison operators are used to compare two values:
#       ==	    Equal
#       !=	    Not equal
#       >	    Greater than
#       <	    Less than
#       >=	    Greater than or equal to
#       <=	    Less than or equal to

# Comparison operators return True or False based on the comparison:

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


# ++++++++++++++++++++++++++++++++++++++ Logical Operators ++++++++++++++++++++++++++++++++++++++++++++

# Logical operators are used to combine conditional statements:
#       and 	Returns True if both statements are true
#       or	    Returns True if one of the statements is true
#       not	    Reverse the result, returns False if the result is true

x = 5

print(x > 0 and x < 10)
print(x < 5 or x > 10)
print(not(x > 3 and x < 10))




# ++++++++++++++++++++++++++++++++++++++ Identity Operators ++++++++++++++++++++++++++++++++++++++++++++

# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
#       is 	        Returns True if both variables are the same object
#       is not	    Returns True if both variables are not the same object

# The is operator returns True if both variables point to the same object:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

# The is not operator returns True if both variables do not point to the same object:

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)


## Difference Between is and ==
#       is      - Checks if both variables point to the same object in memory
#       ==      - Checks if the values of both variables are equal


#++++++++++++++++++++++++++++++++++++++ Membership Operators ++++++++++++++++++++++++++++++++++++++++++++

# Membership operators are used to test if a sequence is presented in an object:
#       in 	        Returns True if a sequence with the specified value is present in the object
#       not in	    Returns True if a sequence with the specified value is not present in the object

# Check if "banana" is present in a list:
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

# Check if "pineapple" is NOT present in a list:
print("pineapple" not in fruits)


# The membership operators also work with strings:
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)


#++++++++++++++++++++++++++++++++++++++ Bitwise Operators ++++++++++++++++++++++++++++++++++++++++++++

# Bitwise operators are used to compare (binary) numbers:
#   & 	AND	Sets each bit to 1 if both bits are 1	
#   |	OR	Sets each bit to 1 if one of two bits is 1	
#   ^	XOR	Sets each bit to 1 if only one of two bits is 1	
#   ~	NOT	Inverts all the bits	
#   <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
#   >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
