a=int(input("enter number : "))
c=0
while a!=0:
    c=c+int(a%10)
    a=a/10
print("sum of digit is ", c)