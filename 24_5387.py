f = open("C:/Users/Alekc/Downloads/24-215.txt")
g = []
lit = "ABC"
num = "123"


# солнце светит негры пашут


def de(i, f, n):
    if (f[i] in lit and f[i + 1] in num):
        n += 1
        return de(i + 2, f, n)
    else:
        return n


k = f.readline()

for i in range(len(k) - 2):
    g.append(de(i, k, 0))

print(max(g))
