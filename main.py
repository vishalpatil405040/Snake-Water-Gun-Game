import random
'''
1 for snake
-1 for water
0 for gun
'''
computer=random.choice([1,-1,0])
youstr=input("Enter the your choise: ")
youDict={"s":1,"w":-1,"g":0}
reversedDict={1:"snake",-1:"water",0:"gun"}

you=youDict[youstr]
print(f"you chose{reversedDict[you]}\ncomputer chose{reversedDict[computer]}")

if(computer==you):
    print("draw")
else:
    if(computer==-1 and you==1):
        print("You win!")
    elif(computer==-1 and you==0):
        print("you lose!")
    elif(computer==1 and you==-1):
        print("you lose!")
    elif(computer==1 and you==0):
        print("you win!")
    elif(computer==0 and you==1):
        print("you lose!")
    elif(computer==0 and you==-1):
        print("you Win!")
    else:
        print("something went wrong")  

        
