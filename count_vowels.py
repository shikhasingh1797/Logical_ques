# var a  = ["my name is durga", "my hobby is playing cricket"]
# Out put ( 13, 23)
# Out put {[vowel:5] , [vowel: 6]}

list1= ["my name is durga", "my hobby is playing cricket"]
i=0
a=[]
b=[]
while i<len(list1[0]):
    if list1[0][i]==" ":
        pass
    else:
        a.append(list1[0][i])
    i=i+1
j=0
#print(a)
len1=len(a)
while j<len(list1[1]):
    if list1[1][j]==" ":
        pass
    else:
        b.append(list1[1][j])
    j=j+1
#print(b)
len2=len(b)
print(len1,len2)
k=0
count=0
while k<len(a):
    if a[k]=="a" or a[k]=="e" or a[k]=="i" or a[k]=="i" or a[k]=="u":
        count=count+1
    k=k+1
#print(count)
l=0
count1=0
while l<len(b):
    if b[l]=="a" or b[l]=="e" or b[l]=="i" or b[l]=="o" or b[l]=="u":
        count1=count1+1
    l=l+1
#print(count,count1) 
empty=[]
empty1=[]
empty.append(count)
empty1.append(count1)
#print(empty)
empty.insert(0,"vowel")
empty1.insert(0,"vowel")
#print(empty,empty1)
dic={}
dic2={}
dic["vowel"]=count
dic2["vowel"]=count1
print(dic,dic2)