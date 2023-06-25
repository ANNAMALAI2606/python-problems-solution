print(" print 10-30 number using for loop")
for i in range(10,31):
    print(i)

print("print six even num. using for loop")
for i in range(0,11,2):
    print(i)

print("print series 50,45,...,5,0. using for loop")
for i in range(50,-1,-5):
    print(i)

print("print first five naturl num. squares using for loop")
for i in range(1,6):
    print(i*i)

print("print table using for loop")
a=int(input("enter table num. : "))
for i in range(1,11):
    print(a*i)

print("print sum of first five odd natural numbers using for loop")
s=0
for i in range(1,10,2):
    s+=i
print(s)

print("print factorial of a number using for loop")
a=int(input('enter factorial num. : '))
f=1
for i in range(a):
    f=f*(a-i)
print(f)
