def firstkdigits(n, k):
    product = 1
    for i in range(n ):
        product *= n
    while ((product // pow(10, k)) != 0):
        product = product // 10     
    return product
n = 15
k = 4
print(firstkdigits(n, k))
 