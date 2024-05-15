print("welcome to my computer quiz!")


playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    
print("Okay! Let's play :)")
score = 0

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!') 
    score += 1  
else:
    print("Incorrect! ")
    
answer = input("how many bits are in a byte? ")
if answer.lower() == "eight":
    print('Correct!')
    score += 1    
else:
    print("Incorrect! ")
    
answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')  
    score += 1  
else:
    print("Incorrect! ")
    
answer = input("who invented Iphone? ")
if answer.lower() == "steve jobs":
    print('Correct!') 
    score += 1   
else:
    print("Incorrect! ")
    
answer = input("who invented the world wide web? ")
if answer.lower() == "tim berners lee":
    print('Correct!') 
    score += 1   
else:
    print("Incorrect! ")
    
print("You got " + str(score) + " questions correct")
print("Your overall score = " + str((score/5) * 100) + "%.")