number = int(input("Please type a positive number: "))

while number < 0:
    print("Sorry, that is a negative number. Please try again.")
    number = int(input("Please type a positive number: "))

print(f"The number is: {number}")


answer = input("May I have a piece of candy? ")

while answer != "yes":
    answer = input("May I have a piece of candy? ")

print("Thank you. ")

people = ("Christopher", "Susan")
print()
for name in people:
    print(name)

index = 0
while index < len(people):
    print(people,{index})
    index += 1

print()

numbers = (0,1,2,3,4,5,6,7,8,9)
for number in numbers:
    print(number)

#or

numbers = range(10)
for number in range(10):
    print(number)

for i in range(100,200):
  print(i)

for i in range(100,200,10):
  print (i)

colors = ["red", "blue", "green", "yellow"]
print()
for color in colors:
    print(color)
print()
numbers = range(1,9)
for number in range(1,9):
    print(number)
print()
for i in range(2,21,2):
  print(i)
  dog_name = input("What is the name of your dog? ")
  letter_count = len(dog_name)

print(f"Your dog's name has {letter_count} letters")

word = "commitment"

favorite_letter = input("What is your favorite letter? ")

for letter in word:
    if letter.lower() == favorite_letter.lower():
      print(letter.upper(),end="")
    else:
      print(letter.lower(), end="")
print()

for letter in word:
   if letter.lower() == favorite_letter.lower():
      print("_", end="")
   else:
      print(letter.lower(), end="")
print()

animal = "dog"
while animal != "dog":
  print("a")
  animal = "cat"
  print("b")
print("c")

value = 20
while value < 20:
  value = value + 1 
print(value)

