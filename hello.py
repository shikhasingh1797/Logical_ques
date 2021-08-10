a="hello"
c=2
i=0
count=0
while i<len(a):
    if a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u":
        b=c*i
        print(b,end="")
    else:
        print(a[i],end="")
    i=i+1
