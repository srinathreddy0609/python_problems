import random

def gamewin(comp,you):
    if comp == you:
        return None
    elif comp=='r':
        if you=='p':
            return True
        elif you=='s':
            return False
    elif comp=='p':
        if you=='r':
            return False
        elif you=='s':
            return True
    elif comp=='s':
        if you=='r':
            return True
        elif you=='p':
            return False
print("computer turn :  rock(r)  paper(p)  sessior(s)")
randNo= random.randint(1,3)

if randNo==1:
    comp ='r'
elif randNo==2:
    comp ='p'
elif randNo==3:
    comp ='s'
you = input("your turn : rock(r)  paper(p)  sessior(s) ? ")
a= gamewin(comp,you)

print("computer  choose ",comp)
print("you  choopse ",you)

#print(f"computer  choose {comp} ")
#print(f"you  choose  {you} ")

if a==None:
    print("the game is tie!")
elif a:
    print("you win")
else:
    print("you lose")
