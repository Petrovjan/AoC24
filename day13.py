raw = open("day13.txt").read().split("\n\n")
data = [x.split("\n") for x in raw]
print(data)
price = 0
for i in range(len(data)):
    n = int(data[i][0][data[i][0].index(": ")+4:data[i][0].index(",")])
    m = int(data[i][1][data[i][1].index(": ")+4:data[i][1].index(",")])
    o = int(data[i][0][data[i][0].index(", ")+4:])
    p = int(data[i][1][data[i][1].index(", ")+4:])
    x = int(data[i][2][data[i][2].index("X=")+2:data[i][2].index(",")]) + 10000000000000
    y = int(data[i][2][data[i][2].index("Y=")+2:]) + 10000000000000

    B = (y*n - o*x)/(p*n - o*m)
    A = (x - m*B)/n
    if A.is_integer() and B.is_integer():
        price += (3*A + B)
print(int(price))