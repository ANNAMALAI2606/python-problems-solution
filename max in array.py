d=int(input('enter list length : '))
a=[]
for i in range(d):
    c=int(input('enter list {0} index element : '.format(i)))
    a.append(c)
print('list : ',a)
print("maximum value in list",max(a))