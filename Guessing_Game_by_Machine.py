from os import system
from time import sleep
from random import randrange
system('clear')
print("Welcome to Guessing Game two!!")
sleep(0.5)
print("Please think a number between 0 to 100. Don't tell the system what is it.")
print("This system will guess a number, and you should tell the system the number is lower or higher to your actual number.")
print("If the system guess too high, you should type \'high\'.")
print("If the system guess too low, you should type \'low\'.")
print("Please pick a number and ready to start!!")
sleep(1)
print("Remember, you should be honest to play this game :P")
sleep(1)
lst = []
for i in range(0,101):
        lst.append(i)
l=0
h=101
tip="no"
t=0
pt="time"
while tip != "yes":
        t+=1
        if tip.isnumeric()==True:
                if int(tip)>l and int(tip)<h:
                        r = int(tip)
                else:
                        r = randrange(l,h)
        else:
                r = randrange(l,h)
        print("Is the number is",r,"?")
        tip = input("If it is type \'yes\'. If it is too high, type \'high\'. If it is too low, type \'low\'. ")
        if tip == "high":
                h = r
        elif tip == "low":
                l = r+1
        elif tip == "yes":
                if t>1:
                        pt="times"
                print("The machine guesses",t,pt,"to figure out your number :D\nThanks for playing!")
                break
        else:
                t-=1
                if t>1:
                        pt="times"
                print("Wrong input!! That let machine to guess again. Now the machine guessed",t,pt)
