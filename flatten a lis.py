a=[[1,2,3],[4,5,6],[7,8]]
print([items for i in a for items in i])

print(sum(a,[]))


b=[]
length=len(a)

i=0
while i <length:
    j=0
    while j<len(a[i]):
        b.append(a[i][j])
        j+=1
    i+=1
print(b)

