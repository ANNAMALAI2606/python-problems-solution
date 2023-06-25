s=int(input("enter starting number : "))
e=int(input("enter ending number : "))
a=[]
for i in range(s,e):
    if i==0 or i==1:
        continue
    else:
        for j in range(2,int(i/2)+1):
            if i%j==0:
                break
        else:
            a.append(i)
print("the prime numbers are ",a)