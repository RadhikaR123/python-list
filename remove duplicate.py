a=[]
size=int(input("enter the size if list : "))
for i in range(size):
    element=int(input("enter list element : "))
    a.append(element)
print(a)
length=len(a)
unique=[]
duplicate=[]
i=0
while i<length:
    if a[i] not in unique:
        unique.append(a[i])
    else:
        duplicate.append(a[i])
    i=i+1
print('unique =',unique)
print('duplicate = ',duplicate)

        

