
items_list = []
removed_items = []

# Task 1: Write a function that lets the user add items to a list.
def add_shopping_cart(items):
    for item in items:
        print(f"Item(s) added to cart - - - - - {item}. ")
        items_list.append(item)
        

add_shopping_cart([])


# Task 2: Include a function to remove items from the list.
def remove_shopping_cart(item_to_remove):
    print(f"""
Item(s) removed from cart - - - - - {item_to_remove}.""")
    items_list.remove(item_to_remove)

remove_shopping_cart()




# Task 3: Add a function that prints out the entire list in a formatted way.
def final_cart():
    for i in items_list:
        print(f"""
Check out cart list - - - - - {i}.""")

final_cart()