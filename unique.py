arr1 = [5, 3, 4, 3,10, 4,10,9]
i=0
arr2=[]
while i<len(arr1):
    count=0
    j=0
    while j<len(arr1):
        if arr1[j]==arr1[i]:
            count=count+1
        j=j+1
    if count==1:
        arr2.append(arr1[i])
    i=i+1
print(arr2)