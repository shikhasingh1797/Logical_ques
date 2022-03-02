arr=[1,4,4,4,5,3]
g = {}
for i in arr:
    if i in g:
      g[i] +=1
    else:
      g[i] =1
print(max(g, key=g.get))