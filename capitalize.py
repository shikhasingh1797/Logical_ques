s="shikha singh mahi singh"
s=s.split()
i=0
b=""
print(len(s))
while i<len(s):
    b=b+s[i]
    c=b.capitalize()
    print(c+" ",end="")
    b=""
    i=i+1