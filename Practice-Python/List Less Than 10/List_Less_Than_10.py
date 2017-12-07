while True:
  criteria = input("Please input the criteria to sort the final list by(Leave this blank if you want to use the default setting of 5): ")
  if(criteria.isdigit()):
    break;
  if criteria == '':
    criteria = 5
    break;

num = list(filter(lambda x: x < int(criteria), list(map(int, input("Please input the chosen elements in the list: ").split()))))

print("The Final List of numbers is " + "[ " + ' , '.join(str(v) for v in num) + ' ]')

