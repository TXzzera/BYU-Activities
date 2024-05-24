#Program: CSE 110 - W04 Prove - Word Puzzle
#Author: Bruno de Sousa Teixeira
print("Welcome to the Word Puzzle Game! ")
print("I have a secret word that you need to find out what it is!")

import random

secret_words = ("newsletter", "office", "garbage", "mortgage", "advice", "selfish", "happiness", "squirrel", "character", "jaguar" )
secret_word = random.choice(secret_words)
guess_count = 0
guess = ""
hint = (" _ ") *len(secret_word)
print(f"Your hint is{hint}")

while guess != secret_word:
  guess = input("What is your guess? ").lower()
  guess_count += 1 

  if secret_word == guess:
    print(f"Congratulations! The secret word was {secret_word}.")
    if guess_count == 1:
      print("You took just 1 guess! ")
    else:
      print(f"You took {guess_count} guesses. ")

  elif guess == "quit":
    print("Thank you for playing with us. Bye! ")
    break
  
  elif len(guess) != len(secret_word):
    print(f"Your guess must be {len(secret_word)} letters long. Try again")
    guess = input("What is your guess? ").lower()
    guess_count += 1
  
  else:
    print("Your guess was incorrect! ")
    print(f"Your hint is: {hint} ")
    for i, letter in enumerate(guess):
                if guess[i] == secret_word[i]:
                    print(letter.upper(), end = " ")
              
                elif letter in secret_word:
                    print(letter.lower(), end = "")

                else:
                    print(" _ ", end = " ")

   

    