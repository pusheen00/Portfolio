grocerylist = []
food = []
items = []

grocerylist.append(food)
grocerylist.append(items)

want = input("Do you want to add or delete an item to your list?")
while want != "no":
    if want == "add":
        more = input("Add an item to your food or items list?")
        if more == "food":
            thing = input("What food would you like to add?")
            food.append([thing])
            print(grocerylist)
        elif more == "item":
            thing = input ("What item would you like to add?")
            items.append([thing])
            print(grocerylist)
        want = input("Do you want to add or delete an item to your list?")
    elif want == "delete":
        more = input("Delete an item to your food or items list")
        if more == "food":
            thing = input("What food would you like to remove from your list?")
            food.remove([thing])
            print(grocerylist)
        elif more == "item":
            thing = input("What item would you like to delete from your list")
            items.remove([thing])
            print(grocerylist)
        want = input("Do you want to add or delete an item to your list?")
else:
    print("Things in your food list", food)
    print("Things in your items list", items)
    print("Things in your grocery list", grocerylist)
    print("Happy Shopping!")
