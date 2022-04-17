a=[]
size=int(input("enter the size if list : "))
for i in range(size):
    element=int(input("enter list element : "))
    a.append(element)
    print(a)
length=len(a)
rem=0
sum=0
i=0
while i<length:
    if a[i]>0:
        rem=a[i]%10
        a[i]=a[i]//10
        sum=a[i]*10
        a[i]=a[i]//10
    i=i+1
    print(sum,'+',rem)





