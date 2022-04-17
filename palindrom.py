# name=[1,2,3,4,5]
# length=len(name)
# i=length-1
# while i>=0:
#     print(name[i])
#     i=i-1
# #if name==name1:
#  #   print("palindrom string")
# #else:
#  #   print("not palindrom")



name=[ 'n', 'i', 't', 'i', 'n' ]
name1=[]
length=len(name)
i=length-1
while i>=0:
    #print(name[i])
    name1.append(name[i])
    i=i-1
if name==name1:
    print("palindrom")
else:
    print("not palindrom")

