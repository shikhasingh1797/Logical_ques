user=int(input("enter a num="))
a=[1,2,3,4,5,6]
i=0
c=[]
while i<len(a):
    d=[]
    j=0
    while j<user:
        d.append(a[i])
        j=j+1
        i=i+1
    c.append(d)  
print(c)