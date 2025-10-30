# ----------------------------------------
# Name: Abdinoor M
# Program: WarehouseSummary.py
# ----------------------------------------
# Purpose: To create a warehouse shipping summary using lists/functions
# ----------------------------------------
import random

def show_inventory(inventory):
#Purpose: prints a list of the inventory, and each of their positions  
    print("\nWarehouse Inventory today:")
    for i in range (len(inventory_list)):
        print(str(i)+".",inventory_list[i])

# Current problem: The list is counting every letter/space/comma etc. rather than each phrase in my len count.
# This is a problem as I need to call upon the positions for each  
# Not sure how to fix this, maybe my list format is off?
# Fixed, initially thought I was taking user input
# Had to make a list outside of function first to use as a test
# Then use a for loop in my function to go through and print the items in my list

def place_orders(inventory):
#Purpose: Assigns a random number to each item in the initial list (inventory_list)
    random_num = random.randint(-3*len(inventory_list),3*len(inventory_list))
    print("\nGenerating" ,len(inventory_list) ,"crate orders (any number from", str(-3*len(inventory_list)),"to", str(3*len(inventory_list)) +"):")
    shipments = []
    for i in range(len(inventory_list)):
        new_number = random.randint(-3*len(inventory_list),3*len(inventory_list))
        shipments.append(new_number)
    print(shipments)
    return shipments



def display_changes(inventory,shipments):
#Purpose: Gives each item in the inventory_list a specific order number, determines the quantity of the item and its status (inbound or outgoing)      
    print("\nToday's Crate Shipments: ")
    for i in range(len(shipments)):
        if shipments[i] < 0:
            print("->", shipments[i]*-1, "crates of",inventory[i],"outgoing")
        elif shipments[i] >= 0:
            print("->", shipments[i], "crates of",inventory[i],"inbound")        

def calc_net_change(shipments):
#Purpose: Calculates the net change of the shipments and prints this number
    net_change = shipments[0] + shipments[1] + shipments[2] + shipments[3]
    print("\nThe net change of crates in the warehouse is " +str(net_change))

inventory_list = ["Water","Milk", "Honey","Juice"]

def warehouse_activities(inventory):
#Purpose: Calls all 4 helper functions created
    show_inventory(inventory)
    shipments = place_orders(inventory)
    display_changes(inventory, shipments, )
    calc_net_change(shipments)
                
warehouse_activities(inventory_list)
