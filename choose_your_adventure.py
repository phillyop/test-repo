name = input("type your name: ")
print("welcome", name, "to this adventure!")

answer = input('you are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ')

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around it or swim to swim across: ")
    
    if answer == "swim":
        print("You swam across and was eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose. ")

elif  answer == "right":
    answer = input("You come to a bridge it looks wobbly, do you want to cross it or head back? (cross/back) ")
    
    if answer == "cross":
        print("You cross and risk falling down to your end or actually proceeding to the next level.")
    elif answer == "back":
        print("You go back to the intersection,and try the other direction.")
    else:
        print("Not a valid option. You lose. ")
else:
    print("Not a valid option. You lose. ")