Choices, a Python dialog library
================================

[choices]() is a quick little library for getting user input in Python in a dialog-like fashion. Here's a little example:

~~~
import choices

# Get a yes or no response (default is no)
confirm = choices.Binary('Are you sure you want to delete?', False).ask()
if confirm:
    deleteIt()

# Input an arbitrary value, check for correctness
howmany = choices.Input('How many pies?', int).ask()
print("You ordered {} pies".format(howmany))

# Choose from a set of options
entree = choices.Menu(['steak', 'potatoes', 'eggplant'])
~~~

[choices]() automatically displays the best UI available to the user: basic text console, curses, or GUI windows. (curses and GUI are in development!)
