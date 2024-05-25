#The task it's that I need to create a list with the names of the friend's user.


friends = []
name = 0

#When the user put "end", the program runs out.
while name != "end":
  name = input ("Type the name of a friend: ")

#When the user put "end", the "end" will not show in the list of friends
  if name != "end":
    friends.append (name)
  
print()
print ("Your friends are: ")

for friend in friends:
  print(friend)

