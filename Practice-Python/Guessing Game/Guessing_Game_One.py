import random

num = random.randint(0,9)
n = 1;


while True:
  guess = input("Guess the number! Input your guess here: ")
  if int(guess) == num:
    print("You've guessed correctly! The number is "+ str(num) + ". You took " + str(n) + " guesses!")
    num = random.randint(0,9)
    n = 0;
    choice=input("Would you like to exit? (Type Exit) : ")
    if choice == "Exit":
      break;
  elif int(guess) > num:
    print("Too High!"+str(n))
  else:
    print("Too low!" +str(n))
  n += 1;
