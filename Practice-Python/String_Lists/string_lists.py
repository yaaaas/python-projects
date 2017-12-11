string = input("please input the string to be compared: ")

print("The Original string is: " + string)

if (string.replace("\\s","").lower() == (string.replace("\\s","").lower()[::-1])):
  print("This is a palindrome! When reversed, it forms "+ string.replace("\\s","").lower()[::-1])
else:
  print("this is not a palindrome!")
