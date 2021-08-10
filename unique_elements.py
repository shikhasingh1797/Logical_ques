list1=[1,2,3,3,3,3,4,5]
i=0
list2=[]
i=0
while i<len(list1):
    if list1[i] not in list2:
        list2.append(list1[i])
    i=i+1
print(list2)