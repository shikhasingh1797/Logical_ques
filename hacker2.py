ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# isme har element ke pair count kro aur print kro agar pair nhi banta hai to use chhod do
i=0
dic={}
while i<len(ar):
    j=0
    count=0
    while j<len(ar):
        if ar[i]==ar[j]:
            count=count+1
        j=j+1
    dic[ar[i]]=count
    i=i+1
lis=[]
total=0
for i in dic:
    if dic[i]>1:
        lis.append(dic[i]//2)
i=0
while i<len(lis):
    total=total+lis[i]
    i=i+1
print(total)