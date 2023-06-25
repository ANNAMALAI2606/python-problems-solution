a=[]
b=int(input("how many index you want in array : "))
for i in range(b):
    c=int(input("give {0} index element".format(i)))
    a.append(c)
print("array : ",a)
a[0] , a[-1] = a[-1] , a[0]
print("swaped array",a)