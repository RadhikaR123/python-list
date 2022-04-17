a=[[0],[1,3],[5,7,6,7,8],[9,11],[13,15,17]]
b=[]
count=0
length=len(a)
i=0
while i<length:
    max=len(a[i])
    j=1
    while j<length:
        if max<len(a[j]):
            max=len(a[j])
            # b.append(a[j])
        j+=1
    # print(max)
    i=i+1
print("maximum length of list is :",max)
print(b)
    
    
