def create_phone_number(n):
    #your code here : (123) 456-7890
    areacode = "(" +''.join(str(x) for x in n[0:3]) +')'
    number = ''.join(str(x) for x in n[3:7]) + "-" + ''.join(str(x) for x in n[7:])
    number = areacode + " " + number
    print(number)
    
    
    
create_phone_number(list(input("please enter the numbers to be converted:")))
