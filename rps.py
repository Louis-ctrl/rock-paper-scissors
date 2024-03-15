import random
import time

#introduction to program, choices presented, variables designated
fullname = "l"
usr = '1'

print("Welcome to rock paper scissors! \n")

def start():
    global usr
    global fullname
    usr = input("Choose rock, paper, or scissors (Only type the first character): ")
    if usr == "r":
        fullname = "rock"
    elif usr == "s":
        fullname = "scissor"
    elif usr == "p":
        fullname = "paper"
    elif usr not in "r" or "p" or "s":
        print("Please enter rock, paper, or scissors! \n")
        start()


start()
print("You chose \n" + fullname)

    

#randomizer and cpu variable designation
chose = 1
cpu = ""

def randomizer():
    global chose
    global cpu
    chose = random.randint(1 , 3)
    cpu = ""

randomizer()

#the picks from the random
def picks():
    global cpu
    if chose == 1:
        print("The Computer chose rock \n")
        cpu = "rock"
        time.sleep(1)
    elif chose == 2:
        print("The Computer chose paper \n")
        cpu = "paper"
        time.sleep(1)
    elif chose == 3:
        print("The Computer chose scissors \n")
        cpu = "scissors"
        time.sleep(1)
picks()


#win and lose conditions and difficulty variable designation

dif = 0
def winning():
    global dif
    if usr[0] == cpu[0]:
        print("The output is a tie! \n")
        dif -= dif
    elif cpu == "paper" and usr == "r" or usr == "rock":
        print("The computer wins! \n")
        dif -= dif
    elif cpu == "scissors" and usr == "p" or usr == "paper":
        print("The computer wins! \n")
        dif -= dif
    elif cpu == "rock" and usr == "s" or usr == "scissors":
        print("The computer wins! \n")
        dif -= dif
    elif cpu == "paper" and usr == "s" or usr == "scissors":
        dif += 1
        print("The user wins! \n")
    elif cpu == "scissors" and usr == "r" or usr == "rock":
        dif += 1
        print("The user wins! \n")
    elif cpu == "rock" and usr == "p" or usr == "paper":
        dif += 1
        print("The user wins! \n")

#win/lose conditions for replays
def winning_again():
    global dif
    if usr[0] == cpu[0]:
        print("The output is a tie! \n")
    elif cpu == "paper" and usr == "r":
        print("The computer wins! \n")
        dif -= dif
    elif cpu == "scissors" and usr == "p":
        print("The computer wins! \n")
        dif -= dif
    elif cpu == "rock" and usr == "s":
        print("The computer wins! \n")
        dif -= dif
    elif cpu == "paper" and usr == "s":
        dif += 1
        print("The user wins! \n")
    elif cpu == "scissors" and usr == "r":
        dif += 1
        print("The user wins! \n")
    elif cpu == "rock" and usr == "p":
        dif += 1
        print("The user wins! \n")

winning()

#replay and difficulty scale
while 0 < dif < 3:
    print("The number of wins you have is")
    print( dif )
    print("Would you like to play again? \n")
    answer = input("Answer yes or no: ")
    if "y" in answer:
        start()
        randomizer()
        picks()
        winning_again()
    else:
        break



#computer challenge (impossible to win)
def comp_chall():
    global usr
    global dif
    if usr == "r":
        print("The Computer chose paper \n")
        print("The computer wins! \n")
        dif -= 4
    if usr == "p":
        print("The Computer chose scissors \n")
        print("The computer wins! \n")
        dif -= 4
    if usr == "s":
        print("The Computer chose rock \n")
        print("The computer wins! \n")
        dif -= 4


while dif == 3:
    print("You're on a roll, the computer would like to challenge you. \n")
    print("Do you accept?")
    acceptance = input("Answer yes or no: ")
    if "y" in acceptance:
        start()
        comp_chall()
    else:
        break


print("Thanks for playing!")
    
#time.sleep(7)