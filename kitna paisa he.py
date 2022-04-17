a= [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
count=0
count1=0
count3=0

i=0
while i<len(a):
    if a[i]>=10000000:
        count=count+1
    elif 100000<=a[i]<=9999999:
            count1+=1
    else:
        count3=count3+1
    i=i+1

    
print("crorepati : ",count)
print("lakhpati :",count1)
print("dilwale :",count3)