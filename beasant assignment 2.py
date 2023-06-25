print("1. find common elements in two list using sets")
a,b=[10,45,34,20,11],[20,25,11,14,45,65]
c=[i for i in a if i in b]
print("common elements are : ",set(c)),print()

print("2. print square of ele. of set using for loop")
a,b = list({2,4,6,8,10}),[]
for i in a:
    b.append(i*i)
print("square : ",set(b)),print()

print("3. swap two tuples\na=(100,200,300)\nb=('sai','kiran','hari')\n")
a,b = (100,200,300),('sai','kiran','hari')
a,b=b,a
print('after swap\n a=',a,'\n b=',b),print()

print('4. print even index element in tuple')
a=('sai','kiran','yash','laxmi',67,12,90,87,'jai')
print('even index elements :',a[::2]),print()

print('5. prime numbers between 1-50')
a=[]
for i in range(1,50):
    if i==0 or i==1:
        continue
    else:
        for j in range(2,int(i/2)+1):
            if i%j==0:
                break
        else:
            a.append(i)
print("the prime numbers are ",a)
