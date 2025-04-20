name= input("Type Your Name ")
print("welcome" ,name, "to this adventure ")

answer=input("you are in a dirt road, it has come to an end and you can go left or right. which way would you like to go. ").lower()


if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")
    if answer=="swim":
        print("you swam accross and you are now on the other side of the river")
    elif answer=="walk":
        print("you walked around the river and you are now on the other side of the river")
    else:
        print("not a valid option")


elif  answer == "right":
    answer=input("You are on the bridge and have 2 options choose a jump in the river or eaten up by zombies- type zombie or jump ")
    if answer == "zombie":
        print("you are now a zombie and you are eating brains")
    elif answer=="jump":
        print("you jumped in the river and you are now on the other side of the river")
    else:
        print("not a valid option")
        
                       
else:
    print("not a valid option")