
place = input("Choose a place: forest or cave? ")
action = input("Climb a tree or cross a river?") # Question 1 Task 1 (variable definition needed to be moved)
action1 = input("Light a torch or proceed in the dark?") # Question 1 Task 2

if place == "forest": # Question 1 Task 1 (operator needed to be changed to '==')
    if action == "climb a tree": # Question 1 Task 1 (operator needed to be changed to '==')
        print("You found a bird's nest!")
    else: # Question 1 Task 1 (no need for the 'action = "cross a river"' statement)
        print("You found a boat!")
else: # Question 1 Task 1 (changed 'elif place = "cave"' statement to and 'else' statement)
    print("You find a hidden treasure!")
    if place == "cave" and action1 == "light a torch":        
        print("Light the way!")
    if place == "cave" and action1 == "proceed in the dark":
        print("Stumble ahead!")
    else: # Question 1 Task 3
        pass