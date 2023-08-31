import random

user_wins = 0
computer_wins = 0

user_name = input("Welcome! What's your name? ")
rps = ["rock","paper","scissors"]
print("Hello",user_name,)

while True:
    
    user_input = input("Choose rock, papers or scissors to play or type Q to quit.").lower()
    if user_input == "q":
        break
        
    if user_input not in rps:
        continue
    
    random_pick = random.randint(0,2)
    #rock: 0, paper: 1, scissors: 2
    computer_pick = rps[random_pick]
    print("Computer picked", computer_pick + ".")
    
    if user_input == "rock" and  computer_pick== "scissors":
        print("You won!")
        user_wins+=1
        continue
    
    if user_input == "scissors" and computer_pick== "paper":
        print("You won!")
        user_wins+=1
        continue
    
    if user_input == "paper" and  computer_pick== "rock":
        print("You won!")
        user_wins+=1
        continue
    
    elif user_input == "paper" and computer_pick == "paper" :
        print("A tie!")
        continue
    elif user_input == "rock" and computer_pick == "rock":
        print("A tie!")
        continue
    elif user_input == "rock" and computer_pick == "rock" :
        print("A tie!")
        continue
    
    else:
        print ("You lost!")
        computer_wins+=1

print ("Goodbye!")
print ("The computer had", computer_wins,"wins")
print ("You had", user_wins,"wins")



