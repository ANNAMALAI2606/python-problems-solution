a=[]
b=int(input("how many index you want in array : "))
for i in range(b):
    c=input("give {0} index element".format(i))
    a.append(c)
print("array : ",a)
d=int(input("enter how many place you want to rotate : "))
e=a[d:]
f=a[:d]
g=e+f
print("the rotated array is ",g)