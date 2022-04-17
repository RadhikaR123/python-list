marks = [

    [78, 76, 94, 86, 88],

    [91, 71, 98, 65, 76],

    [95, 45, 78, 52, 49]
]

sum=0
average=0
k=1
i=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        sum=sum+marks[i][j]
        average=sum//5
        j=j+1
    print(sum)
    print("average of year",k,'is',average)
    k=k+1
    sum-=sum
    i=i+1


