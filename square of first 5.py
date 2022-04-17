a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sq=[]
sq1=[]
i=0
while i<5:
    sq.append(a[i]*a[i])
    i+=1
print(sq)
j=19
while j>=15:
    sq.append(a[j]*a[j])
    j-=1
print("final list : ",sq)