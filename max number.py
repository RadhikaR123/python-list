p=[50,40,23,70,56,12,5,10,7,29,28]
length=len(p)
#print(min(p))
max=p[0]
i=0
while i<length:
    if p[i]>max:
        max=p[i]
    i=i+1
print("maximum = ",max)