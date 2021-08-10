#Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

a="shikha"
i=0
b=[]
count=1
while i<len(a):
    if a[i] in b:
        count=count+1
        b.append(a[i])
        b.append(count)
    else:
        b.append(a[i])
        b.append(count)
    i=i+1
print(b)