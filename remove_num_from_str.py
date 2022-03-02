string="I am 18 years old"
list1=[]
for i in string:
    if not i.isdigit():
        list1.append(i)
result="".join(list1)
print(result)