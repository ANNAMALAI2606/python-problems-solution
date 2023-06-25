n = int(input("how many numbers you want to add:"))
j=0
k=0
for i in range(n):
    j = j + 1

    a= int(input("enter {0} number".format(j)))
    k=k+a
    if i==n-1:
        print("total is :",k)
