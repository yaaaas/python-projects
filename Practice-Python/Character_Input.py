#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

while True:
  print("Please Enter your age", end = '')
  age = input()
  if(age.isdigit()):
    break;

age= int(age)
phrase = ''
if age < 50:
  phrase = "That's a long way more!"
else:
  phrase = "That's quite soon lel"
  
print("You will be 100 in " + str((100-int(age))) + " years. That will be in " + str(2117-age) + " ! " + phrase)
