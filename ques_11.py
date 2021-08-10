list1=["1","2","3","4","5","6"]
#output=[12,34,56]
st=""
for i in list1:
    st=st+i
c=[]
k=0
while k<len(st):
    d=[]
    j=0
    while j<2:
        d.append(st[k])
        j=j+1
        k=k+1
    c.append(d)
str=""
a=[]
for i in c[0]:
    str=str+i
a.append(str)
str1=""
for i in c[1]:
    str1=str1+i
a.append(str1)
str2=""
for i in c[2]:
    str2=str2+i
a.append(str2)
print(*a)








