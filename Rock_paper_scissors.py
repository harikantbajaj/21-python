import random   

user_win =0
computer_wins=0

options=["rock","paper","scissors","test"]

while True:
    user_input= input("Type Rock/paper/Scissors or q to Quit  ").lower()
    if user_input == "q":
        break
    
    if user_input not in["rock","paper","scissors"]:
        continue
    random_number = random.randint(0,2)
    
    computer_pick = options[random_number]
    print("computer picked", computer_pick+".")
    
    if user_input =="rock" and computer_pick =="scissors":
        print("you win")
        user_win +=1
        
    elif user_input =="paper" and computer_pick =="rock":
        print("you win")
        user_win +=1
        
    elif user_input =="scissors" and computer_pick =="paper":
        print("you win")
        user_win +=1
    elif user_input =="rock" and computer_pick =="rock":
        print("same choosen")
        continue
        
    elif user_input =="paper" and computer_pick =="paper":
        print("same choosen")

        continue        
    elif user_input =="scissors" and computer_pick =="scissors":
        print("same choosen")
        continue
print("you won"+user_win+"times")
print("computer won"+computer_wins+"times")

print("Goodbye!!")
