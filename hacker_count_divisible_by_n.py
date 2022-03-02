ar=[1, 3, 2, 6, 1, 2]
i=0
count=0
k=3
while i<len(ar):
    j=0
    while j<i:
        result=ar[i]+ar[j]
        if (result%k==0):
            count=count+1
        j=j+1
    i=i+1
print(count)
