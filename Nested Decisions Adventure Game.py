#Question 1 Task 1

place = input("Choose a place: forest or cave? ")
action = input("Climb a tree or cross a river?") #variable definition needed to be moved

if place == "forest": #operator needed to be changed to '=='
    if action == "climb a tree": #operator needed to be changed to '=='
        print("You found a bird's nest!")
    else: #no need for the 'action = "cross a river"' statement
        print("You found a boat!")
else: #changed 'elif place = "cave"' statement to and 'else' statement
    print("You find a hidden treasure!")
    
#Question 1 Task 2

place = input("Choose a place: forest or cave? ")
action = input("Climb a tree or cross a river?") 
action1 = input("Light a torch or proceed in the dark?")

if place == "forest": 
    if action == "climb a tree": 
        print("You found a bird's nest!")
    else: 
        print("You found a boat!")
else: 
    print("You find a hidden treasure!")
if place == "cave" and action1 == "light a torch":        
    print("Light the way!")
if place == "cave" and action1 == "proceed in the dark":
    print("Stumble ahead!")


#Question 1 Task 3


place = input("Choose a place: forest or cave? ")
action = input("Climb a tree or cross a river?")
action1 = input("Light a torch or proceed in the dark?")

if place == "forest": 
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
else: 
    print("You find a hidden treasure!")
    if place == "cave" and action1 == "light a torch":        
        print("Light the way!")
    if place == "cave" and action1 == "proceed in the dark":
        print("Stumble ahead!")
    else:
        pass