import ShoppingListEL

def ListFoodEL(self):
    List = []
    Orders = int(input("How many items will you order today?"))
    while Orders < 1:
        print("Number of items must be at least 1.")
        Orders = int(input("How many items will you order today?"))
    
    x = 1
    while x <= Orders:
        print(f'Item #{x}-')
        foodName = input(("Enter food:"))
        List.append(foodName)
        foodAmount = (int("Enter amount of pounds:"))
        List.append(foodAmount)
        x =+ 1

    return List

def DisplayListEL(self, Name, Amount, Price, Total):
    return

def totalCostEL(self):
    while x <= orders:
        totalcost = foodcost 
        totalcost =+ foodcost
    return totalcost

def MainEL(self):
    ...
    


