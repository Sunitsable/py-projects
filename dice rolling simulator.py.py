import random

min=1
max=6

print("Please roll the dice")
score=0

#infinite loop
while(True):
    print("the dice is rolling")
    number=random.randint(min,max)
    print(number)
    if number==6:
        print("your score increased by one")
        score=score+1
        print(score)
    else:
        print("roll the dice again")
        break