print("Please input a number: ", end = '')
num = input()
print("Please enter a number to divide " + num + " by: ", end = '')
check = int(input())
if check == '':
  check = 1

print("")

if int(num)%2 ==0:
  if int(num)%4 ==0:
    print(num + " is a multiple of 4 and an even number!")
  else:
    print(num +" is a even number!")
else:
  print(num + " is an odd number!")
  

  
if int(num) % check == 0:
  print(num + " is also divisible by "+ str(check))
else:
  print(num + " is not divisible by " + str(check))
