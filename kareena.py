so=0
se=0
i=0
while i<38:
    if i%2==0:
        se=se+i
    else:
        so=so+i
    i=i+1
print("sum of all elev",se)
rint("sum of all odd",so)



reason = input("enter your reason:")
if (reason=="go to outside"):
    print("Ask to priyanka")
elif (reason=="go to home"):
    print("ask to nilam")
    permission = input("whom you take permission:")
    if (permission=="outside"):
        print("ask to nilam")
    elif (permission=="home"):
        print("ask to shalini")
        condition = input("what is the condition:")
        if (condition=="senior students"):
            print("come to campus 7.00pm before")
        elif (condition=="junior students"):
            print("come to campus 6.00pm before")
            else:
                print("you can't go ")
                else:
                    print("you are not allowed")
                    else:
                        print("ask to nayak bayya")
        
    