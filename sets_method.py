# SET METHODS CHEAT SHEET
# A set stores UNIQUE values and has NO fixed order.

numbers = {1, 2, 3}

numbers.add(4)              # Add one item
numbers.update([5, 6])      # Add multiple items

numbers.remove(2)           # Remove item; error if missing
numbers.discard(10)         # Remove item; no error if missing
numbers.pop()               # Remove a random/arbitrary item
numbers.clear()             # Remove all items

a = {1, 2, 3}
b = {3, 4, 5}

a.union(b)                  # All unique items: {1, 2, 3, 4, 5}
a.intersection(b)           # Common items: {3}
a.difference(b)             # Items only in a: {1, 2}
a.symmetric_difference(b)   # Items in one set, but not both

a.issubset(b)               # Are all items in a inside b?
a.issuperset(b)             # Does a contain all items from b?
a.isdisjoint(b)             # Do they have no common items?

# Operators:
# a | b  = union
# a & b  = intersection
# a - b  = difference
# a ^ b  = symmetric difference