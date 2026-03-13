

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])

# It is also possible to use the dict() constructor to make a dictionary.
thisdict_2 = dict(name = "John", age = 36, country = "Norway")
print(thisdict_2)

# +++++++++++++++++++++++++++++++++++ Access Dictionaries Items +++++++++++++++++++++++++++++++++++++++++

# You can access the items of a dictionary by referring to its key name, inside square brackets:
print(thisdict["brand"])

# There is also a method called get() that will give you the same result:
print(thisdict.get("model"))

# The keys() method will return a list of all the keys in the dictionary.
print(thisdict.keys())

# The values() method will return a list of all the values in the dictionary.
print(thisdict.values())

# The items() method will return each item in a dictionary, as tuples in a list.
print(thisdict.items())


# +++++++++++++++++++++++++++++++++++ Change Dictionaries Items +++++++++++++++++++++++++++++++++++++++++

# You can change the value of a specific item by referring to its key name:
thisdict["year"] = 2018

# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
thisdict.update({"year": 2020})

# +++++++++++++++++++++++++++++++++++ Add Dictionaries Items +++++++++++++++++++++++++++++++++++++++++

# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict["color"] = "red"
print(thisdict)

# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
# The argument must be a dictionary, or an iterable object with key:value pairs.

thisdict.update({"color": "pink"})
print(thisdict)

# +++++++++++++++++++++++++++++++++++ Remove Dictionaries Items +++++++++++++++++++++++++++++++++++++++++

# There are several methods to remove items from a dictionary:
# The pop() method removes the item with the specified key name:
thisdict.pop("model")
print(thisdict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict.popitem()
print(thisdict)

# The del keyword removes the item with the specified key name:
del thisdict["year"]
print(thisdict)

# The clear() method empties the dictionary:
thisdict.clear()
print(thisdict)