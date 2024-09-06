food = input("Vegetarian food? (yes/no)?: ") #Question 2 Task 3
attendees = int(input("Enter number of attendees: "))# Question 2 Task 1 (change type from str to int and add '()'
venue = "Large hall" if attendees > 100 else "Conference room"
print(venue)

if attendees >= 100: #Question 2 Task 2
    print("Upgrade projector and Audio System")
elif attendees <= 100:
    print("Keep the same audio system and same projector")
else:
    print("No need for a projector!")
if food == "yes":
    print("Veggie Delight Caterers")
else:
    print("Gourmet Meals Caterers")