#That's a program to do a little shopping list

shopping_list = []
item = None
print("Please enter the items of the shopping list: ")


while item != "quit":
    item = input("Item: ")    

    if item != "quit":
      shopping_list.append (item)

print("\nThe shopping list is: ")

for item in shopping_list:
   print(item)

print("\nThe shopping list with indexes is: ")

for i in range(len(shopping_list)):
   item = shopping_list[i]
   print(f"{i}. {item}")

print()

index = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

shopping_list[index] = new_item

print()

print("\nThe shopping list with indexes is: ")
for i in range(len(shopping_list)):
   item = shopping_list[i]
   print(f"{i}. {item}")

  