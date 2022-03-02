l1_5=[1,2,3,4,5
    ,6,7,8,9,0
    ,2,5,8,3,9
    ,9,5,3,2,7
    ,3,4,7,5,8]
d={}
for i in range(len(l1_5)):
    if i in l1_5:
        d[i]=l1_5.count(i)
print(d)
