f = 10000
count = 0
for i in range(f):
    x =i^2
    u = str(i)
    u = list(u)
    v = str(x)
    t = list(v)
    if t[-2:]==u[0:2]:
        print(u[0:1])
        count+=1
print(count)