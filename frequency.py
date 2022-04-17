# c = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# d=[]
# e=[]
# count=0


# i=0
# while i<len(c):
#     j=0
#     while j<len(c):
#         if c[i]==c[j]:
#             count=count+1
#         j=j+1
#     print(c[i],count)
#     d.append([c[i],count])
#     count=count-count
#     i=i+1
# k=0
# while k<len(d):
#     if d[k] not in e:
#         e.append(d[k])
#     k=k+1

# print(e)




c = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
d=[]
e=[]
count=0
i=0
while i<len(c):
    j=0
    while j<len(c):
        if c[i]==c[j]:
            count=count+1
        j=j+1
    print(c[i],count)
    d.append([c[i],count])
    count=count-count
    i=i+1
k=0
while k<len(d):
    if d[k] not in e:
        e.append(d[k])
    k=k+1

print(e)

