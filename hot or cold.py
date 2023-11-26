import random as r
p_a=''
c=0
while p_a=='':
    cv=r.randint(1,101)
    
    while cv!=0:
        pv=int(input("Enter a guess(0 to 100):"))
        if pv==cv:
            print("Damn you got it. Your score is",20-c,"out of 20")
            cv=0
        else:
            c+=1
            if abs(pv-cv)<2:
                print("hottest")
            elif abs(pv-cv)<5:
                print("really hott")
            elif abs(pv-cv)<10:
                print("hotter")
            elif abs(pv-cv)<20:
                print("warmer")
            elif abs(pv-cv)<50:
                print("warm")
            elif abs(pv-cv)<60:
                print("colde")
            elif abs(pv-cv)<70:
                print("colder")
            elif abs(pv-cv)<80:
                print("really cold")
            elif abs(pv-cv)<90:
                print("coldestt")
    p_a=input("play again? (hit enter to continue):")
        

