from os import system
from time import sleep
system('clear')
print("\nWelcome to Rock Paper Scissors GAME!! \nJust two players in this game!\n")
sleep(1)
def battle(x,y):
        def p(a):
                return "Player {} wins!!!".format(a)
        if x==y:
                return "Draw!!"
        elif (x=="r" and y=="s") or (x=="s" and y=="p") or (x=="p" and y=="r"):
                return p(1)
        else:
                return p(2)
def valid(z):
        if z!="r" and z!="p" and z!="s":
                return False
        else:
                return True
i = "y"
while i == "y":
        n = "*"*20+"\n    not valid!!!\n"+"*"*20
        def p(q):
                return "Player {} please choose one(r or p or s): ".format(q)
        a = input(p(1))
        while valid(a)==False:
                print(n)
                a = input(p(1))
        b = input(p(2))
        while valid(b)==False:
                print(n)
                b = input(p(2))
        print(battle(a,b))
        i = input("Do you want to play again?(y/n) ")
        while i!="y" and i!="n":
                print(n)
                i = input("Do you want to play again?(y/n) ")
