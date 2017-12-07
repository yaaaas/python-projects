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

sentence = "You will be 100 in " + str((100-int(age))) + " years. That will be in " + str(2117-age) + " ! " + phrase
print(sentence, end = "\n\n")

print("Multiply this Phrase!! Key in the number of times to do so : ", end = " ")
multiple = int(input())
print((sentence + "\n")*multiple)
