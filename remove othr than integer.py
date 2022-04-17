a=[34.67 , 12 , -94.89 , 'python' , 0 , 'c#']
b=[]
for j in a:
    if type(j)==int:
        a.remove(j)
    print(a)