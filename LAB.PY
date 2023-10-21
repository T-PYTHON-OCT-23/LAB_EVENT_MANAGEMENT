workshops = [
    {"Workshop_ID" : "W1", "Title": "Photography Basics", "Seats_Available": 20},
    {"Workshop_ID": "W2", "Title": "Intro to Python", "Seats_Available": 15},
]
participants = {
    'Alice': ['W1'],
    'Bob': ['W1', 'W2'],
    # ...
}

def search_workshop(workshops, Workshop_ID):
     for workshop in workshops:
        if workshop["Workshop_ID"] == Workshop_ID:
            return workshop
        return None

def register_workshop(workshops, participants, participant_name, Workshop_ID):
    workshop = search_workshop(workshops, Workshop_ID)
    if workshop and workshop["Seats_Available"] > 0:
        workshop["Seats_Available"] -= 1
        participants.setdefault(participant_name, []).append(Workshop_ID)
        print("You have been registered successfully.")
    else:
        print("Sorry, the seats are full or the workshop was not found.")

def cancel_registration(workshops, participants, participant_name, Workshop_ID):
    workshop = search_workshop(workshops, Workshop_ID)
    if workshop and participant_name in participants and Workshop_ID in participants[participant_name]:
        workshop["Seats_Available"] += 1
        participants[participant_name].remove(Workshop_ID)
        print("You have successfully cancelled your registration.")
    else:
        print("Sorry, you are not registered for this workshop or the workshop was not found.")

def list_workshops(participants, participant_name):
    for key , value in participants.items():
        if key == participant_name :
            print(F"this is all your workshops: {value}")   
def list_participants(workshops, participants, Workshop_ID):
    for key , value in participants.items():
        if value == [Workshop_ID]:
           print(F"This all names of participants registered: {[key]}")

def main():
    while True:
        print("Welcome to our workshops")
        user=input("1:search_workshop 2 :register_workshop 3 : cancel_registration 4: list_workshops 5:  list_participants  0 to exit ")
        if user == "0":
            break
        Workshop_ID = input("Please type Workshop ID: ")
        participant_name = input("Type your name: ")
        if user == "1":
                search_workshop(workshops, Workshop_ID)
                print(workshops)
        elif user == "2":
                register_workshop(workshops, participants, participant_name, Workshop_ID)
        elif user == "3":
                cancel_registration(workshops, participants, participant_name, Workshop_ID)
        elif user == "4":
                list_workshops(participants, participant_name)
        elif user == "5":
                list_participants(workshops, participants, Workshop_ID)

main()
print(workshops)
print(participants)
