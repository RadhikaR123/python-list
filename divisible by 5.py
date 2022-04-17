a=[]
size=int(input("enter the size if list : "))
for i in range(size):
    element=int(input("enter list element : "))
    a.append(element)
    print(a)
length=len(a)
a2=[]
i=0
while i<length:
    if a[i]%5==0:
        print("element divisible by 5 are : " ,a[i])
    i=i+1