f = open("C:/Users/Alekc/Downloads/24-222.txt")
print(f.readline().find("A"))

def niger(sres, strn,k):
    a = sres.find("A")
    strn2 = sres[:a+1]
    if strn == "" or strn == strn2:
        k += 1
        return niger(sres[a+1:], strn2,k)
    else:
        return k

