p=[50,40,23,70,56,12,5,10,7,29,28]
length=len(p)
sum=0
count=0
i=0
while i<length:
    if 20<=p[i]<=30:
        count=count+1
        sum=sum+p[i]
    i=i+1
print("number between 20 to 30 is ", count)
print("their sum is ", sum)



