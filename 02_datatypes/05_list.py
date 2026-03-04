
# Lists are used to store multiple items in a single variable.
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# List is declered by using []

# list id Mutable or Changeble

# We can create a list in two way:

thislist = ["apple", "banana", "cherry", "apple", "cherry"] # Way-1
thislist = list(("apple", "banana", "cherry")) # Way-2 note the double round-brackets
print(thislist)


# +++++++++++++++++++++++++++++++++++ Access List Items +++++++++++++++++++++++++++++++++++++++++

# List items are indexed and you can access them by referring to the index number:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])

# Negative indexing means start from the end. -1 refers to the last item, -2 refers to the second last item etc.
print(thislist[-1])

# You can specify a range of indexes by specifying where to start and where to end the range.
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

# +++++++++++++++++++++++++++++++++++ Change List Items +++++++++++++++++++++++++++++++++++++++++

# To change the value of a specific item, refer to the index number:
thislist[1] = "blackcurrant"
print(thislist)

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist[1:3] = ["blackcurrant", "watermelon"]

# +++++++++++++++++++++++++++++++++++ Add List Items +++++++++++++++++++++++++++++++++++++++++

# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
thislist.insert(2, "watermelon")

# To add an item to the end of the list, use the append() method:
thislist.append("orange")

# +++++++++++++++++++++++++++++++++++ Remove List Items +++++++++++++++++++++++++++++++++++++++++

# The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# The pop() method removes the specified index.
thislist.pop(1)

# The del keyword also removes the specified index:
del thislist[0]

# The del keyword can also delete the list completely.
del thislist

# The clear() method empties the list.
thislist.clear()

# +++++++++++++++++++++++++++++++++++ Sort Lists +++++++++++++++++++++++++++++++++++++++++

# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# To sort descending, use the keyword argument reverse = True:
thislist.sort(reverse = True)

# +++++++++++++++++++++++++++++++++++ Copy Lists +++++++++++++++++++++++++++++++++++++++++

# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# You can use the built-in List method copy() to copy a list.
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# +++++++++++++++++++++++++++++++++++ Remove List Items +++++++++++++++++++++++++++++++++++++++++

# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Or you can use the extend() method, where the purpose is to add elements from one list to another list:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)