shoppingList = ["milk", "fruits", "veggies", "sugar", True, 45, 100]
print(shoppingList)

if "sugar" in shoppingList:
    print(shoppingList.index("sugar"))
else:
    print("Does not exist")