p = int(input())
n = int(input())
r = int(input())
counter=1
counter1 = []

count1 = 0
f = 1
for i in range(p):
    if p>counter:
        if r==1:
            f = f+n
            counter = counter*(n*r)
            counter1.append(f)
            
        elif r>1:
            f = f*n
            counter = counter *(n*r)
            counter1.append(f)

if r==1:
    print(len(counter1)+1)
else:
    print(len(counter1)-1)


