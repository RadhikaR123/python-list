p=[50,40,23,70,56,12,5,10,7,29,28]
length=len(p)
min=p[0]
i=1
while i<length:
    if p[i]<min:
        min=p[i]
    i=i+1
print("minimum number is : ",min)
