people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

#the max variables
youngest_age = 1000
youngest_person = " "

#to iterate with each name and age, I put a for loop 
for line in people:
  parts = line.split()
  person = parts[0]
  age = int(parts[1])

  if age < youngest_age:
    youngest_age = age
    youngest_person = person

print(f"The youngest person is {youngest_age} years old. ")
print(f"The youngest person is: {youngest_person}. ")

    
  
  
  
  
    
