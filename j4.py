a = input()
b=input()

c = list(a)
d=list(b)
counter = 0
for i in range(len(d)):
    s = d.pop(0)
    d.insert(len(d),s)
    for x in range(len(d)):
        if c[x:len(d)]==d[x:len(d)]:
            counter+=1
        else:
            pass

if counter>0:
    print("yes")
else:
    print("no")
'''
012
ABA
BAA
AAB
ABA

'''