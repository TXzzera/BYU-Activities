#In this program I will write three different functions and ask for user to write a messsage.
#After that, the message will appear in three different layouts.

def display_regular(user_message):
    print(user_message)

def display_uppercase(user_message):
    print(user_message.upper())

def display_lowercase(user_message):
    print(user_message.lower())

print()

user_message = input("What is your message? ")
display_regular(user_message)
display_uppercase(user_message)
display_lowercase(user_message)



