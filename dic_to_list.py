# dic= {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# for i in dic.keys():
#     print(i,end=" ")
# print()
# a=dic.values()
lis=list(a)
i=0
b=[]
c=[]
d=[]
while i<len(lis):
    b.append(lis[i][0])
    c.append(lis[i][1])
    d.append(lis[i][2])
    i=i+1
print(*b)
print(*c)
print(*d)