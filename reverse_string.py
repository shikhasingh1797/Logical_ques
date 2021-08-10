str="1234abcd"
count=len(str)
i=0
rev=""
while count>0:
    rev=rev+str[count-1]
    count=count-1
print("Reverse string=",rev)