# list=[1,2,3,4,5]
# list1=[]
# length=len(list)
# x=0
# i=length-1
# while i>=0:
#     list1.append(list[i])
#     i=i-1
# print(list1)






# list=[1,2,3,4,5]
# list1=[]
# length=len(list)
# x=list[0]
# i=1
# while i<length:
#     list[i-1]=list[i]    
#     i=i+1
# list[length-1]=x
# print(list)



a=[]
size=int(input("enter size of the list"))
for i in range(size):
    value=int(input("enter list values :"))
    a.append(value)
print(a)
b=[]
# first=a[0]
# i=0
# j=1
# while i<size:
#     a[i]=a[size-j]
#     j=j+1
#     i=i+1
# a[size-1]=first
# print(a)

b.append(a[size-1])
i=0
while i<size-1:
    b.append(a[i])
    i+=1
print(b)

