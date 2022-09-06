# Rock-paper-scissors-lizard-Spock template

#PRODUCED BY TeCoEd (@dan_aldred)
#23/04/2013
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


import random
import time

#converts number to a name

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "please make a selection"
        
# CONVERTS NAME INTO A NUMBER   

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Yo made an incorrect selection"
        start_play()
         
def rpsls(name): 
    player_number = name_to_number(name)
    print " "
    print "Player chooses", name
    time.sleep(1)
    comp_number = random.randrange(0,4) #selects a random number for the computer
    print " "
    print "Computer chooses", number_to_name(comp_number)
    time.sleep(1)
    
    result = (comp_number - player_number) % 5 
    #print result
    
    if result == 0:
        print "Player and computer tie!"
    elif result >=3:
        print " "
        print "Player wins!"
    else:
        print " "
        time.sleep(1)
        print "Computer wins!"
    print " "

def start_play():
    print  "Welcome to RPSLS"
    time.sleep(1)
    print " "
    print "Your selections, rock, paper, scissors, lizard, spock"
    time.sleep(1)
    print " "
    x = raw_input("Please select your choice. ").lower()
    rpsls(x)
    if raw_input("Run again? Y/N ").lower() == "y":
        start_play()

        
start_play()

