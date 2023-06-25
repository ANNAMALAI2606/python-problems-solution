a=input("enter ASCII charecter : ")
for i in range(255):
    if a==chr(i):
        print("the {0} ASCII charector order is {1}. ".format(a,ord(a)))
'''
#print all ASCII Values
#ASCII 255 
#A-Z = 65-90
#a-z = 97-122
#  = 32
a=int(input("enter limit : "))
for i in range(a):
    print("{0} {1}".format(i,chr(i)))
'''