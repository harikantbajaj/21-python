print('Welcome to my computer quiz')

playing = input("do you want to play? ") 
SCORE = 0
if playing.lower() != "yes":
    quit()
    
print ("Okay let's play ")
answer = input("what does dl stands for? ")
if answer.lower() =="deep learning":
    print("Correct")
    SCORE += 1
else:
    print("Incorrect")
    
answer = input("what does gpu stands for? ")
if answer.lower() =="graphics processing unit":
    print("Correct")
    SCORE += 1
else:
    print("Incorrect")
    
answer = input("what does ml stands for? ")
if answer.lower() =="machine learning":
    print("Correct")
    print("You won ")
    SCORE +=1
    
else:
    print("Incorrect")
print("you got " + str(SCORE) + " question correct")