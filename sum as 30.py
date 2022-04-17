number = 30

n = [10, 11, 12, 13, 14, 17, 18, 19]
n1=[]
sum=0

i=0
while i<len(n):
    j=0
    while j<len(n):
        sum=n[i]+n[j]
        if sum==30:
            n1.append([n[i],n[j]])
        j=j+1
    i=i+1
print(n1)
