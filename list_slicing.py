#List Slicing
#Important note: must use "[:]" to create a copy

amazon_cart = [
    "notebook",
    "sunglasses",
    "toys",
    "grapes"
]

amazon_cart[0] = "laptop"
new_cart = amazon_cart[:]
new_cart[0] = "gum"
print(new_cart)
print(amazon_cart)