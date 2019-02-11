import random
global num, got
num = random.randint(1,101)
got = False
for i in range(1,8):
    print("guess a num between 1 and 100 chief (I know its a dead meme but please deal with it)")
    g = int(input())
    if g == num:
        print("you got it chief")
        got = True
        break
    if g < num:
        print("higher chief")
    if g > num:
        print("too high chief")
if got:
    print("this is it chief")
else:
    print("this aint it chief")