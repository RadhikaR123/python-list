# a=[]
# a1=[]
# size=int(input("enter list size : "))
# for i in range(size):
#     val=int(input("enter list element : "))
#     a.append(val)
#     print(a)





a=[1,2,3,4,5]
length=len(a)
a1=[]
i=0
while i<length:
    a[i]=a[i]*a[i]
    a1.append(a[i])
    i=i+1
print(a1)


    
    