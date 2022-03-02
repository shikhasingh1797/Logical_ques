list1=[1,2,3,4,5,6,7]
str1=""
list2=[]
str2=""
if (len(list1)%2==0):
    pass
else:
    str2=(str2+str(list1[-1]))
    list1.pop()
for i in  list1:
    str1=str1+str(i)
    if len(str1)==1:
        pass
    else:
        list2.append(str1)
        str1=""
if str2=="":
    pass
else:
    list2.append(str2)
print(list2)