import random
top = input("Type a number: ")

if top .isdigit():
    top = int(top)
    
    if top <=0:
        print("Please type a positive integer.")
        quit()
else:
    print("That's not a number!")
    quit()

random_number=random.randint(0,top)
guess = 0
while True:
    user= input("make a guess: ")
    if user.isdigit():
        user = int(user)
        guess += 1
    
    else:
        print("type a number next time. ")
        guess += 1 
        continue
               
    if user ==random_number:
        print("you got it! ")
        break
    else:
        if user > random_number:
            print("too high!")
        else:
            print("too low!")
    if guess ==  3:
        print("you lost")
        break

