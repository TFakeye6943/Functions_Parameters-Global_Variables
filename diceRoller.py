#Coin flip program
#Describe the purpose of this program here.
#This code should ask the user for input and then roll the number they wanted to roll
import random,time


s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"#This list prints the side of the die
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"

roll=(0)
def roll():
    print("rolling.....")
    roll = random.randint(1,6)#This function makes sure you can only ask for a number from 1-6
    return roll
rolling=roll()
time.sleep(1)

def show_dice():
    roll=int(input("What do you want to roll- "))# This function asks the user for input on how much they want to roll then prints out the correct side of the die
    if roll == 1:
        print(s1)
    elif roll == 2:
        print(s2)
    elif roll== 3:
        print(s3)
    elif roll == 4:
        print(s4)
    elif roll == 5:
        print(s5)
    else:
        print(s6)


dice=show_dice()
time.sleep(1)



#Errors
#no indentation
#Always rolls a six
#Should only print 1-6 not 1-7
#S1 instead of s1
