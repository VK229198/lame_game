import random as r
p_a=''
c=0
print("Rules:\n1. The aim of the game is to guess the randomly generated number\n2. Pick a number between 1 and 100\n3. Coldestt=your guess is 90 away from the right answer\n4. Really cold=your guess is 80 away from the right answer\n5. Colder=your guess is 70 away from the right answer\n6. Colde=your guess is 60 away from the right answer\n7. Your guess is 50 away from the right answer\n8. Warm=your guess is 50 away from the right answer\n9. Warmer=your guess is 20 away from the right answer\n10. Hotter=your guess is 10 away from the right answer\n11. Really hott=your guess is 5 away from the right answer\n12. Hottest=less than 2 away from the answer")
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
        

