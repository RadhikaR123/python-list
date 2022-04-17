a=[]
size=int(input("enter the size if list : "))
for i in range(size):
    element=int(input("enter list element : "))
    a.append(element)
    print(a)
even=[]
odd=[]
length=len(a)
for i in a:
    if i%2==0:
        even.append(i)
        print("even element :",even)
    else:
        odd.append(i)
        print("odd element :",odd)
    