import collections
def primeFactors(n):
    n = int(n)
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    k = 0
    factors = []
    while n!= 1:
      if n % primes[k] == 0:
        factors.append(primes[k])
        n = n//primes[k]
      elif n % primes[k] != 0:
        k+=1
    uniq = collections.OrderedDict.fromkeys(factors)
    
    print(uniq)
    final = ''
    for i in uniq:
      count = factors.count(i)
      if count == 1:
        final += "(" + str(i)+")"
      else:
        final += "(" + str(i)+"**"+str(factors.count(i))+")"
      
      
      
    print(final)
        
primeFactors(int(input)))
        
