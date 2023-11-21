import random as r
l=["rock","paper","scissors"]
cc=l[r.randint(0,2)]
s=0
p_a="yes"
while p_a=="yes":
    cc=l[r.randint(0,2)]
    print("Your choice")
    pc=input("rock paper scissors:").lower()
    print("computer's choice:",cc)
    if cc==pc:
        print("tie")
    elif cc=="scissors":
        if pc=="paper":
            print("you loose")
        
        elif pc=="rock":
            print("you win")
            s+=1
    elif cc=="paper":
        if pc=="rock":
            print("you loose")
        elif pc=="scissors":
            print("you win")
            s+=1
    elif cc=="rock":
        if pc=="scissors":
            print("you loose")
        
        elif pc=="paper":
            print("you win")
            s+=1
    p_a=input("do you want to play again?:")
print("your score is:",s)


