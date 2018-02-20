#program for rock,paper, sci
import random
computer=None
compscore=0
score=0
print("start the game")
print("your score is",score)
print("the computer score is",compscore)
l=["rock","paper","sessior"]
print(computer)
while(score<=5 or compscore<=5):
    computer=random.choice(l)
    print("rock, paper,sessior")
    user=input("enter your choice")
    if computer==user:
        print("it's a tie")
        print("your score is",score)
        print("the computer score is",compscore)
    elif computer=="rock" and user=="paper":
        print("user wins")
        score+=1
        print("your score is",score)
        print("the computer score is",compscore)
    elif computer=="paper" and user=="rock":
        print("computer wins")
        compscore+=1
        print("your score is",score)
        print("the computer score is",compscore)
    elif computer=="paper" and user=="sessior":
        print("user wins")
        score+=1
        print("your score is",score)
        print("the computer score is",compscore)
    elif computer=="sessior" and user=="paper":
        print("computer wins")
        compscore+=1
        print("your score is",score)
        print("the computer score is",compscore)
    elif computer=="rock" and user=="sessior":
        print("computer wins")
        compscore+=1
        print("your score is",score)
        print("the computer score is",compscore)
    elif computer=="sessior" and user=="rock":
        print("user wins")
        score+=1
        print("your score is",score)
        print("the computer score is",compscore)
        break
while(score>5) :     
    print("game over")
    break

    
