def popsicles(x,y):
    if(y%x==0):
        print("Give Away.")
    else:
        print("Eat them yourself.")
sib = int(input("Enter number of siblings : "))
pop = int(input("Enter number of popsicles : "))
popsicles(sib,pop)