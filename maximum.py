n=int(input("enter the no. of element : "))
l=[]
j=1
for i in range(1,n+1):
    a=int(input("enter the {0} element : ".format(j)))
    j+=1
    l.append(a)
print("list : ",l)
print("the maximum no. in list is ",max(l))