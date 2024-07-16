# Menu list for restaurent
menu ={
    'Pav Bhaji': 100,
    'Misal': 70,
    'Masala Dosa': 80,
    'Rava Dosa': 100,
    'Idli': 70,
    'Ice Cream': 50, 
    'Pohe': 30,
    'Lassi': 20,
    'Tea': 10,
    'Pulao Rice': 80, 
    'Water Bottle': 20,
}

#Greet
print("Welcome to Narayani Home Kitchen Restaurent")
print("-------- Menu --------")

print("Pav Bhaji: 100\nMisal: 70\nMasala Dosa: 80\nRava Dosa: 100\nIdli: 70\nIce Cream: 50\nPohe: 30\nLassi: 20\nTea: 10\nPulao Rice: 80\nWater Bottle: 20")
print("----------------------")

order_total=0

item_1=input("Please enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order list")
else:
    print(f"Sorry but your preferred {item_1} is not available right now")
    
another_order =input("Do you want to add any another item? (Yes/No)")    
if another_order== "Yes":
    item_2=input("Please enter the name of item you want to add = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order list")
    else:
        print(f"Sorry but your preferred {item_1} is not available right now") 
        
print("-------- Thank You for the order --------\n")      
print(f"Your total amount payable is {order_total}\n")    
print("-------- Thank You Visit Again --------")
      
