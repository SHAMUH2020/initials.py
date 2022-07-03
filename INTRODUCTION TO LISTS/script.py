""" What is a List?
In programming, it is common to want to work with collections of data. In Python, a list is one of the many built-
in data structures that allows us to work with a collection of data in sequential order.

Remove the # in front of the definition of the list broken_heights. If you run this code, you’ll get an error in your terminal:

SyntaxError: invalid syntax
Add commas (,) to broken_heights so that it runs without errors."""

heights = [61, 70, 67, 64, 65]

# broken_heights = [65 71 59 62]

# The correct line of code is:
broken_heights = [65, 71, 59, 62]

""" What can a List contain?
Lists can contain more than just numbers."""

ints_and_strings = [1, 2, 3, "four", "five", "six"]
sam_height_and_testscore = ["Sam", 67, 85.5, True]

""" Empty Lists
A list doesn’t have to contain anything."""
my_empty_list = []

""" List Methods
As we start exploring lists further in the next exercises, we will encounter the concept of a method.
In Python, for any specific data-type ( strings, booleans, lists, etc. ) 
there is built-in functionality that we can use to create, manipulate, and even delete our data. We call this built-in functionality a method.
For lists, methods will follow the form of list_name.method(). Some methods will require an input value that will go between the parenthesis of the method ( )."""

example_list = [1, 2, 3, 4]

#Using Append
example_list.append(5)
print(example_list)

#Using Remove
example_list.remove(5)
print(example_list)

""" Growing a List: Append
We can add a single element to a list using the .append() Python method."""
# Example 2 Using Append
orders = ["daisies", "periwinkle"]
print(orders)
orders.append("tulips")
orders.append("roses")
print(orders)

# Growing a List: Plus (+)
# When we want to add multiple items to a list, we can use + to combine two lists (this is also known as concatenation).
orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:
new_orders = ["lilac", "iris"]
print(orders + new_orders)
orders_combined = orders + new_orders

# broken_prices = [5, 3, 4, 5, 4] + 4 
""" Remove the # and whitespace in front of the list broken_prices. 
If you run this code, you’ll get an error:  TypeError: can only concatenate list (not "int") to list 
Fix the command by inserting brackets ([ and ]) so that it will run without errors. """

# The correct line of code is: 
broken_prices = [5, 3, 4, 5, 4] + [4]

""" Accessing List Elements We are interviewing candidates for a job. We will call each candidate in order, represented by a Python list"""

employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]

employee_four = (employees[3])
print(employees[8]) # Selecting an element that does not exist produces an IndexError.

# The correct line of code is:
print(employees[6]

# Accessing List Elements: Negative Index 
# What if we want to select the last element of a list?
# We can use the index -1 to select the last item of a list, even when we don’t know how many elements are in a list.

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

last_element = shopping_list[-1]
index5_element = shopping_list[5]
print(last_element, index5_element)

# Modifying List Elements
# Lets modify the garden waitlist
garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]

garden_waitlist[1] = "Calla"
print(garden_waitlist)

garden_waitlist[-1] = "Alex"
print(garden_waitlist)
      
# Shrinking a List: Remove
# We can remove elements in a list using the .remove() Python method.
      



