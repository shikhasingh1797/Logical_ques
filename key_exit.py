num=int(input("Enter a num="))
a=[]
dic={1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}
for i in dic:
    a.append(i)
if num in a:
    print("EXIST")
else:
    print("NOT EXIST")
i=i+1
