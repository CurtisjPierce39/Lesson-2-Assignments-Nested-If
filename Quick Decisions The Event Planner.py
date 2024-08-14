#Question 2 Task 1

attendees = int(input("Enter number of attendees: ")) #change type from str to int and add '()'
venue = "Large hall" if attendees > 100 else "Conference room"
print(venue)


#Question 2 Task 2

attendees = int(input("Enter number of attendees: "))
venue = "Large hall" if attendees > 100 else "Conference room"
print(venue)

if attendees > 100:
    print("Upgrade projector")
    if attendees > 100:
        print("Upgrade audio system")
    elif attendees < 100:
        print("Keep the same audio system")
else:
    print("No need for a projector!")

#Question 2 Task 3

food =input("Vegetarian food? (Yes/No)?: ")
attendees = int(input("Enter number of attendees: "))
venue = "Large hall" if attendees > 100 else "Conference room"
print(venue)

if attendees > 100:
    print("Upgrade projector and Audio System")
elif attendees < 100:
    print("Keep the same audio system and same projector")
else:
    print("No need for a projector!")
if food == "Yes":
    print("Veggie Delight Caterers")
else:
    print("Gourmet Meals Caterers")