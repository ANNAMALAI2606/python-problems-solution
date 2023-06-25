n=a=int(input('enter no. : '))
if a==1 or a<0:
    print("factorial is ",n)
else:
    #for loop
    b=1
    for i in range(2,n+1):
        b=b*i
    print("factorial of {0} is {1}.".format(n, b))
'''
#while loop
b=1
while a>0:
    b=b*a
    a=a-1
print("factorial of {0} is {1}.".format(n,b))
'''

'''
import math
print("factorial is ",math.factorial(a))
'''