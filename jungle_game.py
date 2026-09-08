name = input("choose player name? ")
playing = input("are you ready for a new adventure? ")
if playing.lower() != "yes":
    quit()
    
print("Okay! Let's play", name,"!")

print("For this adventure you need to choose one of these tools to bring along.")
list