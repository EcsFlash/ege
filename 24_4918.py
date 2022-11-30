f = open("C:/Users/Alekc/Downloads/24-191.txt")
g = []
k = f.readline()
#k = "ACCCCCFCCCCCCCB"
for i in range(1,14):
    for j in range(len(k)):
        if j + i + 1 < len(k):
            #print(k[j],k[j+i+1])
            if k[j] == "A" and k[j+i+1] == "B":
                if("F" in k[j:j+i+2] and k[j:j+i+2].count("A") == 1 and k[j:j+i+2].count("B") == 1):
                    g.append(len(k[j:j+i+2]))
print(g)
print(len(g))