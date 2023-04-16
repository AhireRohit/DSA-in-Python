shoppingList = ["milk", "fruits", "veggies", "sugar", True, 45, 100]
print(shoppingList)

shoppingList[0] = "Doodh "            # updating
print(shoppingList)

shoppingList.insert(1, "APPLE")       # inserting
print(shoppingList)

shoppingList.append ("PINEAPPLE")     # appending --> adding element at end
print(shoppingList)

newList = [11, 12, 13, 14]
shoppingList.extend(newList)          # add list in list
print(shoppingList) 

shoppingList.pop(6)                   # delete last element   
print(shoppingList)

print(shoppingList[0:2])              # Slicing
    
shoppingList.remove("sugar")          # removes element
print(shoppingList) 