num = int(input("Key in the number you want to emulate "))
n =1
numbers = []
while (n < num+ 1):
  if(num%n ==0):
    numbers.append(n);
  n+=1

print("The divisors of " + str(num) + " are [" +  ','.join(str(x) for x in numbers) +']')
  
