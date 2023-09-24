def dice():

    import random
    mindice=1
    maxdice=6
    again='y'
    while again=='yes' or again=='y' or again=='Y':
        print("rolling the dice")
        print("results are")
        print(random.randint(mindice,maxdice))
        again=input("wanna play again??")
    print("byee")
dice()
