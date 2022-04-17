a = [

    [8, 3, 4],

    [1, 5, 9],

    [6, 7, 2]

]


if a[0][0]+a[0][1]+a[0][2]==a[1][0]+a[1][1]+a[1][2]==a[2][0]+a[2][1]+a[2][2]:
    if a[0][0]+a[1][0]+a[2][0]==a[0][1]+a[1][1]+a[2][1]==a[0][2]+a[1][2]+a[2][2]:
        if a[0][0]+a[1][1]+a[2][2]:
            print("this is a magic square :")
        else:
            print("diagonal sum is not equal")
    else:
        print("colums sum is not equal")
else:
    print("rows sum is not equal")
