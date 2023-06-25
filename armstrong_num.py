n=a=int(input('enter no. : '))
b=0
c=len(str(a))
while a!=0:
    r=a%10
    b+=(r**c)
    a=a//10
if n==b:
    print("the given number is armstrong number")
else:
    print("the given number is not a armstrong number")

'''
armstrong number eg.,153,1634
'''