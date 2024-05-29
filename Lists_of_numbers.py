list_of_numbers = []
number = -1

print("Enter a list of numbers, type 0 when finished. ")

while number != 0:
    number = int(input("Enter number: "))

    if number != 0:
       list_of_numbers.append(number)

#I will take the sum of these numbers of the list
sum = 0

for number in list_of_numbers:
  sum += number

print(f"The sum is: {sum}")

#Now, I want to know the average of these numbers
count = len(list_of_numbers)
average = sum/ count

print(f"The average is: {average}")

#For last, I want to know what is the largest number
largest = -1
for number in list_of_numbers:
  if number > largest:
    largest = number

print(f"The largest number is: {largest}")
   





