#should save a file called scientist_birthdays.json from https://www.practicepython.org/assets/scientist_birthdays.json
import json
with open('scientist_birthdays.json','r') as f:
        a=json.load(f)
#a={"Albert Einstein":"14/03/1879","Thomas Alva Edison":"18/10/1847","Pablo Ruiz Picasso":"25/10/1881"}
print("\nWelcome to the birthday dictionary. We know the birthdays of:")
b=[]
for i in a:
        print(i)
        b.append(i)
user=""

while user not in b:
        user=input("Who's birthday do you want to look up?\n")
else:
        print("{}'s birthday is {}.\n".format(user,a[user]))

user=input('Who else do you want to add to the dictionary?(If don\'t, type \'no\'. If wanna remove name, type \'remove\')\n')
if user.upper() == "REMOVE":
        user=input("Which name you want to remove from dictionary?\n")
        if user in b:
                a.pop(user)
        with open('scientist_birthdays.json','w') as f:
                json.dump(a,f)
elif user.upper() != "NO":
        birth=input('What\'s his/her birthday?(Format of dd/mm/yyyy)\n')
        a[user]=birth
        with open('scientist_birthdays.json','w') as f:
                json.dump(a,f)
