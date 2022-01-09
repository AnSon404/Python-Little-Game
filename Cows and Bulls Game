from os import system
from random import randrange
system('clear')
answer = []
for i in range(4):
        answer.append(str(randrange(0,10)))
print("Welcome to Cows and Bulls Game!")
print("If guess correct in correct place, get a cow.")
print("If guess correct in wrong place, get a bull.")
print("answer:",answer)
print("Type of answer:",type(answer[0]))
def result(r,a):
        cow = 0
        bull = 0
        pcow = "cow"
        pbull = "bull"
        for i in range(4):
                if int(r[i])==int(a[i]):
                        cow+=1
                else:
                        if r[i] in a:
                                bull+=1
        if cow > 1:
                pcow = "cows"
        if bull > 1:
                pbull = "bulls"
        return "{} {}, {} {}".format(cow,pcow,bull,pbull)
print(type(answer))
lnum = []
count = 0
pcount = "time"
print(type(answer))
while lnum != answer:
        num = "na"
        while len(num)!=4:
                lnum = []
                num = input("Please guess a 4-digit number: ")
                if num == "quit":
                        exit()
                for i in num:
                        lnum.append(i)
        print(result(num,answer))
        count += 1
        if count > 1:
                pcount = "times"
        print("You have tried",count,pcount)
else:
        print("Congratulation! You guest the answer! Well Done!!!")
