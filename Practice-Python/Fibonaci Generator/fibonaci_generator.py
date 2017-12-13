length = int(input("Enter the number of fibonaci numbers you wish to generate: "))

first = 0;
second = 1;

print(second, end = ',')

for i in range(0,length-1):
  first,second = second, first+second
  if i == (length-2):
    print(second, end = '\n')
  else:
    print(second, end = ',')
