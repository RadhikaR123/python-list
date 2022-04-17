a=[2,3,4,5,2,6,3,2]
number=int(input("enter the number to find frequency"))
count=0
i=0
while i<len(a):
    if a[i]==number:
        count=count+1
    i=i+1
print("frequency of :",number,"is",count)