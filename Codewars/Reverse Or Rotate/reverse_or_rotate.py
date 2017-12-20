import math
def revrot(strng, sz):
  # your code
  final = ''
  for i in range(0,len(strng)+1,sz):
    if i + sz > len(strng):
      break;
    portion = strng[i:i+sz]
    y = 0
    for x in portion:
      y += math.pow(int(x),3)
    if y%2 == 0:
      portion = portion[::-1]
    else:
      portion = portion[1:len(portion)] + portion[0]
    
    final+= portion
  print(final)

