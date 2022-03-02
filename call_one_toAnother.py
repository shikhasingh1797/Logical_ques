def add(a,b):
    def s():
        d=a+b
        return d
    return s()
print(add(3,5))