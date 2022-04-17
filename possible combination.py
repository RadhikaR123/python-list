a=[1,2,3]
b=[]

i=0
while i<len(a):
    j=0
    while j<len(a):
        k=0
        while k<len(a):
            b.append([a[i],a[j],a[k]])
            #print(a[i],a[j],a[k])
            k+=1
        j+=1
    i+=1
print(b)

