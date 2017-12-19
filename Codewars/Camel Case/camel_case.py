#s == input string , n == conversion type
def toCamelCase(s,n):
    # good luck
    final = ''
    words=s.split(" ")
    if n == 1:
      final += words[0][0].lower()+words[0][1:]
      for i in words[1:]:
        i = i[0].upper()+i[1:]
        final += i;
      
    
    elif n == 2:
      for i in words[:len(words)-1]:
        i = i[:len(i)-1].lower() + i[len(i)-1].upper()
        final += i
      final += words[len(words)-1].lower()
    else:
      for i in words:
        i = i[0].upper() + i[1:len(i)-1] + i[len(i)-1].upper()
        final += i
      final = final[0].lower()+final[1:len(final)-1]+final[len(final)-1].lower()
    print(final)
    
toCamelCase("QyD hEDLAjOR faOHcF BalXhbbn mrjvuALA PVQ rYphNgHP mtkIbpv wbmADZI",3)
