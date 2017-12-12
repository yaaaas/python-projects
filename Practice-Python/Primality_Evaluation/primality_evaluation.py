import sys
import random

#Method 1 : Using a loop to evaluate whether the number is a prime
def isPrime2(number):
  if number == 2 or number == 3 or number == 1:
    print(str(number) + " is a prime!")
  else:
    for i in range(1,int(number)):
      if number% i == 0:
        print(str(number) + " is not a prime!")
        sys.exit();
        break;
        
    print(str(number) + " is a prime!")
    
#Method 2 : Using Fermat's Little Theoreom to evaluate primes using a probabilistic approach. 
def isPrime():
  num = int(input("Please enter your integer to be evaluated: "))
  evaluate = random.randint(0,num)
  if num == 2 or num == 3 or num == 1:
    print(str(num) + " is a prime!")
  elif ((evaluate**num) - evaluate ) % num == 0:
    print(str(num) + " is a prime!")
  else:
    print(str(num) + " is not a prime!")
  
isPrime2(int(input("Please enter the number to be evaluated: ")))
isPrime()
