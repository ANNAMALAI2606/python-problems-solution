d=int(input('enter list length : '))
a=[]
for j in range(d):
    c=int(input('enter list {0} index element : '.format(j)))
    a.append(c)
print('list : ',a)
b=0
e=len(a)
for i in range(e):
    b+=a[i]
#for i,c in enumerate(a):
#    b+=c
print('sum of array is ',b)
# sum(list)