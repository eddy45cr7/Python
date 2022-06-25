inp = input("Enter the text : ")
l = []
im = inp.split()
for i in im:
    leng = len(i)
    word = ""
    for j in range(leng):
        z = i[j]
        y = ord(z)
        x = y+32
        w = chr(x)
        word += w
    l.append(word)
    
print("In smaller case : ",end = "")
for k in l:
    print(k,end=" ")