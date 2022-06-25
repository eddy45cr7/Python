comm = int(input("Enter Number Of Committee Members : "))
seni = int(input("Enter Number of Seniors : "))
juni = int(input("Enter Number of Juniors : "))

tot_peep = comm + seni + juni
tot_budg = (comm*1000) + (seni*750) + (juni*400)
if(tot_peep>=50):
    pub_give = tot_peep * 550
else:
    pub_give = (tot_peep*550) + 5000
aft_PuGi = (tot_budg - pub_give) + 1750

fin_budg = aft_PuGi - 4100

print("Number of members : ",tot_peep)
print("Total Budget : ",tot_budg)
print("Giving to Pub : ",pub_give)
print("Remaining : ",aft_PuGi)
print("after Miscellenious expenses : ",fin_budg)
if(fin_budg>0):
    print("Profit!!")
elif(fin_budg==0):
    print("Perfectly Balanced.")
else:
    print("Loss!!")