a=[1,2,3,4,5,6,7,8,9,10]
d=[]
diff=0
i=9
while i>=0:
    diff=a[i]-a[i-1]
    i-=1
    d.append(diff)
    if i==0:
        break
print(d)







