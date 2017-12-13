a = [1,2,3,2,1,5,6,5,5,5]
x = []

def loopremoval(ab):
  for i in range(len(ab)):
    if ab[i] not in x:
      x.append(ab[i])
  print(x)
  
def setremoval(ab):
  return list(set(ab))
  
print(setremoval(a))

