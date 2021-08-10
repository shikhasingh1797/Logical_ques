var=[[12,34,45],[56,67,78],[2,3,4]]
print("Original list=",var)
i=0
lis=[]
while i<len(var):
    j=0
    while j<len(var[i]):
        lis.append(var[i][j])
        j=j+1
    i=i+1
print("Flatten list=",lis)
k=0
n=len(lis)
while k<len(lis):
    l=0
    while l<n-1:
        if lis[k]<lis[l]:
            lis[k],lis[l]=lis[l],lis[k]
        l=l+1
    k=k+1
print("Ascending order=",lis)

n = len(lis)
lis.sort()
  
if n % 2 == 0:
    median1 = lis[n//2]
    median2 = lis[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = lis[n//2]
print("Median is: " + str(median))