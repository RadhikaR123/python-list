a=[]
size=int(input("enter the size if list : "))
for i in range(size):
    element=int(input("enter list element : "))
    a.append(element)
    print(a)
length=len(a)
sum=0
i=0
while i<length:
    sum=sum+a[i]
    i=i+1
print("sum of all elements : ",sum)

