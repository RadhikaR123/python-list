q= [
"How many continents are there?", # pehla question
"What is the capital of India?", # doosra question
"NG mei kaun se course padhaya jaata hai?" # teesra question
]

a= [
["Four", "Nine", "Seven", "Eight"],
["Chandigarh", "Bhopal", "Chennai", "Delhi"],
["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]

i=0
while i<=len(q):
    print("your que is :",q[i])
    j=0
    while j<=len(a):
        print("your options are :",a[j])
        print("selsect your option or 50-50 life-line")
        c=input("select your option")
        count=0
        if c=='nine' or c=='delhi' or c=='software engineer':
            print("your ans is correct :")
        elif c=='life line':
            k=0
            while k<2:
                count=count+1
                print("your remaining options are :",a[j][k])
                k+=1
            d=input("select answer from these options now :")
            if d=='nine' or d=='delhi' or d=='software engineering':
                print("congrats your answer is correct")
            else:
                print("sadly, your answer is wrong,,you are out of the game")
                break
            if count==1:
                print("sorry you already used the life line :")
        else:
            print("your ans is wrong")
            print("you are out of the game :")
            break
        j=j+1
    i=i+1
        





