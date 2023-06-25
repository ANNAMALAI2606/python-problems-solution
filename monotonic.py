a=[]
b=int(input("how many index you want in array : "))
for i in range(b):
    c=int(input("give {0} index element".format(i)))
    a.append(c)
print("array : ",a)
d=len(a)
e=1
f=1
for i in range(d-1):
    if a[i]<a[i+1]:
        e+=1
    elif a[i]>a[i+1]:
        f+=1
if e==d or f==d:
    print("the given array is monotonic")
else:
    print("the given array is not a monotonic")