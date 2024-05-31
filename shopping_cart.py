#This program will ask for the user what he wants from the shopping list, 
#the items prices and will give to him some options to interact with this
#shopping cart.

print("Welcome to the Shopping Cart Program! ")

total = []
price = 0
item = None
cart = []

while True:

  print("""
Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit""")

  choice = input("Please enter an action: ")

  if choice == "1":
    item = input("What item would you like to add? ")
    cart.append(item)

    price = float(input(f"What is the price of '{item}'? "))
    total.append(price)

    print(f"'{item}' has been added to the cart")
    
  elif choice == "2":

    if not cart:
      print("The cart is empty, please add some item. ")
    else:
      print ("The contents of the shopping cart are: ")
      for i in range(len(cart)):
        item = cart[i]
        price = total[i]
        print(f"{i+1}.{item} - ${price}")

  elif choice == "3":
    
    if cart:
        
      try: 
        remove = int(input("Which item would you like to remove? "))
        removed_item = cart.pop(remove-1)
        price_removed = total.pop(remove-1)
        print("Item removed")

      except ValueError:
        print("That is not a valid choice. Enter a valid number")

    else: 
      print("The cart is already empty! ")
  
  elif choice == "4":

    sum = 0
    for price in total:
      sum += price
    print(f"The total price of the items in the shopping cart is ${sum} ")

  elif choice == "5":
    print("Thank you. Goodbye!")
    break
    
  else:
    print("That is not a valid choice, please take a number into 1-5. ")
