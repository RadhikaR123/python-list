a=["radhika","rajoriya","vidhi","kareena","nayak","kumar"]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):                      #we can also use "random.shuffle(a[i])" fun here
        b=a[i][0:2]
        c=a[i][2:len(a[i])]
        e=c+b
        j+=1
    print(e)
    i+=1






# list1=list(("radhika","reena"))    #this is how the list constructor works
# print(list1)