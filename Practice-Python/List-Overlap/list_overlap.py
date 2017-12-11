from random import randint

a = []
b = []

for i in range(int(input("please input length of array a: "))):
  a.append(randint(0, 9))
  
for j in range(int(input("please input length of array b: "))):
  b.append(randint(0, 9))

combination = list(set(b).intersection(set(a)))
print("Array A is: ", end = '')
print(a)

print("Array B is: ", end = '')
print(b)
combination.sort()
print(combination)
