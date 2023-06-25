a=[]
b=int(input("how many index you want in array : "))
for i in range(b):
    c=int(input("give {0} index element".format(i)))
    a.append(c)
print("array : ",a)
d=len(a)
e=1
for i in range(d):
    e*=a[i]
n=int(input("enter n : "))
f=e%n
print("the remainder is ",int(f))