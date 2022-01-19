print("\nWelcome to the game of tic-tac-toe!")
a = "|   |   |   |"
b = "|   |   |   |"
c = "|   |   |   |"
def pBoard(a,b,c):
        r = "         --- --- --- "
        f = "             row"
        s = "          1   2   3"
        x = "       1"
        y = "column 2"
        z = "       3"
        return f+"\n"+s+"\n"+r+"\n"+x+a+"\n"+r+"\n"+y+b+"\n"+r+"\n"+z+c+"\n"+r
def isnumber1to3(x):
        if x.isnumeric()==True:
                if int(x)>=1 and int(x)<=3:
                        return "True"
                else:
                        return "False"
        else:
                return "False"
def locationR(x):
        if x=="1":
                return "2"
        elif x =="2":
                return "6"
        elif x=="3":
                return "10"
def draw(q,w,e,x,y,z):
        y=int(y)
        if x=="1":
                global a
                if a[y]=="X" or a[y]=="O":
                        print("That\'s cheating!! You lost a move!")
                else:
                        a=q[:y]+z+q[y+1:]
        elif x=="2":
                global b
                b=w[:y]+z+w[y+1:]
        elif x=="3":
                global c
                c=e[:y]+z+e[y+1:]
def PlayerSign(x):
        if x==1:
                return "X"
        elif x==2:
                return "O"
def askPlayer(x):
        ur = "0"
        uc = "0"
        while isnumber1to3(ur)=="False":
                ur=input("Player {}, please type number of row(1, 2 or 3): ".format(str(x)))
        ur=locationR(ur)
        while isnumber1to3(uc)=="False":
                uc=input("Player {}, please type number of column(1, 2 or 3): ".format(str(x)))
        draw(a,b,c,uc,ur,PlayerSign(x))
def win(a,b,c,x):
        if a[2]==a[6]==a[10]==PlayerSign(x):
                return "True"
        elif b[2]==b[6]==b[10]==PlayerSign(x):
                return "True"
        elif c[2]==c[6]==c[10]==PlayerSign(x):
                return "True"
        elif a[2]==b[6]==c[10]==PlayerSign(x):
                return "True"
        elif a[10]==b[6]==c[2]==PlayerSign(x):
                return "True"
        elif a[2]==b[2]==c[2]==PlayerSign(x):
                return "True"
        elif a[6]==b[6]==c[6]==PlayerSign(x):
                return "True"
        elif a[10]==b[10]==c[10]==PlayerSign(x):
                return "True"
        else:
                return "False"
print(pBoard(a,b,c))
for i in [1,2,1,2,1,2,1,2,1]:
        if win(a,b,c,i)=="False":
                askPlayer(i)
                print(pBoard(a,b,c))
                if win(a,b,c,i)=="True":
                        print("Congratulation!! Player {} win this game! End game.\n".format(i))
                        w = "True"
                        break
if w!="True":
        print("It\'s a draw!")
