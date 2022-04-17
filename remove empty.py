a=[5,6,[],3,[],[],9]
i=0
while i<len(a):
    if a[i]==[]:
        a.remove(a[i])
    i=i+1
print(a)
