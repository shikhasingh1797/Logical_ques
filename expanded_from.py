num=input("Enter a num:")
a="0"
c=len(num)-1
i=0
sum=0
st=" "
while i<len(num):
    sum=num[i]+a*c
    st=st+sum+"+"
    c=c-1
    i=i+1
z=st[:-1]
print(z)