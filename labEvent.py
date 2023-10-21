workshops = [
    {'Workshop_ID': 'W1', 'Title': 'Photography Basics', 'Seats_Available': 20},
    {'Workshop_ID': 'W2', 'Title': 'Intro to Python', 'Seats_Available': 15},
    {'Workshop_ID': 'W3', 'Title': 'Intro to Java', 'Seats_Available': 10}
    
]

participants = {
    'Alice': ['W1'],
    'Bob': ['W1', 'W2'],
    'Ebtesam': ['W1', 'W3']
    
}

def search_workshop(workshops, Workshop_ID):
    for workshop in workshops:
        if workshop["Workshop_ID"] == Workshop_ID:
            return workshop
    return "Workshop not found"


def register_workshop(workshops, participants, participant_name, Workshop_ID):
    workshop = search_workshop(workshops, Workshop_ID)
    if workshop == "Workshop not found":
        print("Workshop not found")

    
    if Workshop_ID in participants.get(participant_name, []):
        print(f"{participant_name} is already registered for this workshop")

    elif workshop["Seats_Available"] > 0:
        participants.setdefault(participant_name, []).append(Workshop_ID)
        workshop['Seats_Available'] -= 1
        print(f"{participant_name} has been registered for {workshop['Title']}.")

    elif workshop["Seats_Available"] == 0:
        print("Sorry workshop is full")
    

    

def cancel_registration(workshops, participants, participant_name, Workshop_ID):
    workshop = search_workshop(workshops, Workshop_ID)
    if workshop == "Workshop not found":
        print("Workshop not found")

    elif Workshop_ID not in participants.get(participant_name, []):
        print(f"{participant_name} is not registered for this workshop")
    else:
        participants[participant_name].remove(Workshop_ID)
        workshop['Seats_Available'] += 1
        print((f"{participant_name}, The workshop({workshop['Title']}) has been successfully deleted."))


def list_workshops(participants, participant_name):
    return participants.get(participant_name, [])

def list_participants(workshops, participants, Workshop_ID):
    workshop = search_workshop(workshops, Workshop_ID)
    if workshop == "Workshop not found":
        return "Workshop not found"
    
    participantsList = [participant for participant, workshops in participants.items() if Workshop_ID in workshops]
    return participantsList

userInput = input("Please enter workshop ID: ")
workShopDetails = search_workshop(workshops,userInput)
print(f"workshop details: {workShopDetails}")

print("If you would like to register for the workshop, complete the following:")
name = input("Please enter name: ")
ID = input("Please enter workshop ID: ")
register_workshop(workshops, participants , name, ID)

print("If you would like to delete the workshop, complete the following:")
name = input("Please enter name: ")
ID = input("Please enter workshop ID: ")
cancel_registration(workshops, participants , name, ID)

nameparticipant = input("To list all workshops for a participant, write the name: ")
print(f"Workshop list: {list_workshops(participants ,nameparticipant )}")


workshopName = input("To list all participant in particular workshop, write the name of workshop: ")
print(f"participants list: {list_participants(workshops, participants ,workshopName )}")