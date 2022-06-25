a = int(input("Enter age : "))



if(a in range(0,11)):
    print("Child")
elif(a in range(11,21)):
    print("Teen")
elif(a in range(60,119)):
    print("Senior citizen")
elif(a<0):
    print("Invalid age")
elif(a>119):
    print("ghost")
else:
    print("Adult")
