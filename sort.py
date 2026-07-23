# sort method and function

basket = ['a', 'x', 'b', 'c', 'd', 'f', 'e']
print(sorted(basket))
print(basket)

basket.sort()
print(basket)

""" basically, the "sorted" is creating a copy of the "basket", 
while "sort" is changing the basket
"""

# copy method

new_basket = basket.copy()
new_basket = new_basket.sort
print(new_basket)

#reverse method (to reverse the order of list)

basket.sort()
basket.reverse()
print(basket)



