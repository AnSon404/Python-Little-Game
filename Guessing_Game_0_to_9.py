from random import randrange
from os import system
from time import sleep
system('clear')
print("Welcome to Guessing Game One!!")
print("By the way, you can type \'exit\' to quit! Thanks.\n")
r = randrange(1,10)
c = 0
clist = [1,9]
while c != r:
        c = input("Now range is from {} to {}! Please guess a number: ".format(clist[0],clist[-1]))
        if c.isnumeric():
                if int(c) > 9 or int(c) < 1:
                        print("Wrong input...")
                elif int(c) > r:
                        clist.append(c)
                        print("Guessed too high!")
                elif int(c) < r:
                        clist.insert(0,c)
                        print("Guessed too low!")
                else:
                        print("Great work!! Guess right!!!")
                        print("So you have guessed {} times to get the right answer XD\n".format(len(clist)-2))
                        break
        else:
                if c == "exit":
                        break
                else:
                        print("Wrong input...")
~                                                 
