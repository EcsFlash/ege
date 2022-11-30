f = open("C:/Users/Alekc/Downloads/24-230.txt")
b = f.readline()
g = []
for a in range(len(b)):
    if a + 13 < len(b):
        if b[a] == "K" and b[a+1] == "K" and b[a+13] == "K" and b[a+14] == "K" and b[a+2:a+13][:2] == "43" and b[a+2:a+13][9:] == "34" and b[a+2:a+13][4:6] == "78":
            g.append(b[a+2:a+13])

n  = 1
for i in max(g):
   if int(i) % 2 != 0:
       n = n * int(i)

print(n)