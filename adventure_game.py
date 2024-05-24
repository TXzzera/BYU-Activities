#This game will be called "Castle's Rush"
print("Welcome to Castle's Rush! ")
print("You have decisions to make and according to your choices, you will have different paths and consequences! ")
print("You are in a valley and need to reach in the top, where is the castle that you have to be to survive." )
print("But your time is short, arrive there at 7PM. Now it's 6PM. If you don't be fast, you will die to the beasts of the mountains! ")
choice = input("You can reach in the castle in a CAR or in a MOTORBIKE, what do you want? ").lower()
if choice == "car":
  choice_2 = input("The fuel is half full. Complete the gas tank NOW or LATER? ").lower()
  if choice_2 == "now":
    choice_3 = input("There are two paths: the FIRST is short, but have some obstacles. The SECOND is longer, but is a clear road. What do you choose? ").lower()
    if choice_3 == "first":
      print("Hmm, the car can't pass trough these obstacles. You need to return. You spend 5 minutes until here, requires more 5 minutes to return and the other path will take 40 minutes to arrive in the final destine. Go fast and you will get it! ")
    elif choice_3 == "second":
      print("Great, the GPS shows that you will be at the top of the mountain in 40 minutes, if everything is going to be ok. Congratulations!")
    else:
      print("That's not a valid choice. Please, come back and try again. ")
  if choice_2 == "later":
    choice_3 = input("There are two paths: the FIRST is short, but have some obstacles. The SECOND is longer, but is a clear road. What do you choose? ").lower()
    if choice_3 == "first":
      print("Hmm, the car can't pass trough these obstacles.You need to return, You spend 5 minutes until here, requires more 5 minutes to return and you should refuel the car and turn on it again. It will take more 10 minutes and the other path take 40 minutes. You lose! ")
    elif choice_3 == "second":
      print("Ok,the GPS was showing that you would take just 40 minutes. But you need to refuel the car, so now you will spend 50 minutes to reach. Go fast and you will get it! ")
    else:
      print("That's not a valid choice. Please, come back and try again. ")
if choice == "motorbike":
  choice_2 = input("The fuel is full. But it would be good to carry a gas tank to refuel the motorbike. Will you take the gas tank: YES or NO? ").lower()
  if choice_2 == "yes":
    choice_3 = input("There are two paths: the FIRST is short, but have some obstacles and it's more dangerous to a motorbike. The SECOND is longer, but is a clear road. What do you choose? ").lower()
    if choice_3 == "first":
      print("Well, you suffer a little accident because you were trying to not let the gas tank falls on the floor. But you got up and continued your trip. You just spend 30 minutes and reached in the top of the mountain. Congratulations! ")
    elif choice_3 == "second":
      print("This path take 30 minutes, but you need to refuel your motorbike in the middle of the way and turn on it again. It will take more 15 minutes. Go fast and you still can get it!")
    else:
      print("That's not a valid choice. Please, come back and try again.")
  if choice_2 == "no":
    choice_3 = input("There are two paths: the FIRST is short, but have some obstacles and it's more dangerous to a motorbike. The SECOND is longer, but is a clear road. What do you choose? ").lower()
    if choice_3 == "first":
      print("Very good, you were so fast and reach on the top of the mountain in 15 minutes. Congratulations! ")
    elif choice_3 == "second":
      print("You take 30 minutes in this path. But in the middle of the way, the fuel is over. So you spend 15 minutes, need to spend more 15 minutes to return and more 15 to turn on the motorbike to enter in the path again. You lose! ")