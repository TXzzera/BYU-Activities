child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of a adult's meal? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))
artistic_couvert = int(children + adults) * 1.50
print(f"Artistic Couvert: {artistic_couvert}")
print()
subtotal = (child_meal * children + adult_meal * adults) + artistic_couvert
print(f"Subtotal: {subtotal}")
print()
tax_rate = float(input("What is the sales tax rate? "))
print(f"Sales Tax: {subtotal * tax_rate / 100}")
sales_tax = subtotal * tax_rate / 100
total = subtotal + sales_tax
print(f"Total: {total}")
print()
payment_amount = float(input("What is the payment amount? "))
print(f"Change: {payment_amount - total:.2f}")

#I just added the artistic couvert to have fun in the restaurant!\