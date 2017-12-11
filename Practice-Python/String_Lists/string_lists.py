string = input("please input the string to be compared: ")

print("The Original string is: " + string)

if (string.replace("\\s","") == (string.replace("\\s","")[::-1])):
  print("This is a palindrome! When reversed, it forms "+ string[::-1])
else:
  print("this is not a palindrome!")
