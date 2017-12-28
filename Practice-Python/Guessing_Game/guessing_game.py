#Declaring Constants
h = "h"
l = "l"
y = "y"

#Computer guessing
end = int(input("What is the highest range that you want to play at: "))
start = 0
guesses = 1

while True:
  mid = int(start+(end-start)/2)
  print("start: " + str(start))
  print("End: " + str(end))
  print("The new guess is " + str(mid))
  guess = input("Did I guess it correctly? ( h, l ,y ) :" )
  if guess == y:
    print("Got you! I knew the answer was "+ str(mid))
    break
  elif guess == h:
    end = mid
    print("start: ")
  elif guess == l:
    start = mid
  guesses += 1

print("I took " + str(guesses) + " guesses to guess your number! Eat that!")
