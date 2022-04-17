a=[2,-7,5,-64,-14]
count=0
count1=0
i=0
while i<len(a):
    if a[i]<0:
        count=count+1
        #print("negative",count)
    else:
        count1+=1
        #print("positive are ;",count1)
    i=i+1
print("positive are :",count1)
print("negative are :",count)

