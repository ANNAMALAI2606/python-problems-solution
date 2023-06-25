a=[]
b=int(input("how many index you want in array : "))
for i in range(b):
    c=int(input("give {0} index element".format(i)))
    a.append(c)
print("array : ",a)
d=int(input("give 1st swaping position :"))
e=int(input("give 2rd swaping position :"))
a[d-1] , a[e-1] = a[e-1] , a[d-1]
print("swaped array",a)