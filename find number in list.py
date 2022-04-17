# a=[]
# num=int(input("enter list item that u want :"))
# size=len(a)
# for x in range(size):
#     element=int(input("enter list elements :"))
#     a.append(element)
# print(a)


a=[]
size=int(input("enter the size if list : "))
for i in range(size):
    element=int(input("enter list element : "))
    a.append(element)
print(a)
b=int(input("enter another num that u want to check in list : "))
i=0
while i<size:
    if b==a[i]:
        print(b,"is present in list ")
        break
    else:
        print(b,"is not in list ")
        # break
    i+=1
    