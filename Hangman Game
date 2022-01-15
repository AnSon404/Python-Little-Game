#should save a file from http://norvig.com/ngrams/sowpods.txt called sowpods.txt
from random import choice
with open('sowpods.txt','r') as s:
        lines = s.readlines()
x=choice(lines).strip('\n')
print("Welcome to Hangman Game!")
ltips=[]
tips=''
letter=' '
for i in range(len(x)):
        ltips.append('_')
        tips+='_ '
print(tips)
while tips.replace(' ','')!=x or len(letter)!=1:
        letter = input("Guess a letter: ").upper()
        for i in range(len(x)):
                if letter==x[i]:
                        ltips[i]=x[i]
        tips=''
        for i in range(len(ltips)):
                tips+=ltips[i]+' '
        print(tips)
print("Well done!! Congratulation! You guess the correct word!\n")
