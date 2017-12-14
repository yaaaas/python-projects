import random
num = random.randint(1000,9999)
guesses = 0;

while guesses < 8:
  guess = int(input("Please input your guess!"))
  print("Your guess was " + str(guess))
  #breakdown num
  composite = list(str(num))
  guessbreak = list(str(guess))
  cow = 0;
  
  for i in range(0,4):
    if composite[i] == guessbreak[i]:
      cow += 1;
  print("Cows: " + str(cow) +", Bulls: "+ str(4-cow) )
  guesses += 1;
  
  if cow == 4:
    break;
    
  

print("The correct answer was "+str(num)+ ". You took " + str(guesses) + " guesses")
