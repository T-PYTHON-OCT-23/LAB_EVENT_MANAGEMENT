
workshops = [
        {'Workshop_ID': 'W1', 'Title': 'Photography Basics', 'Seats_Available': 20},
        {'Workshop_ID': 'W2', 'Title': 'Intro to Python', 'Seats_Available': 15},
        {'Workshop_ID':'W3', 'Title':'C++',' Seats_Available':10},
        {'Workshop_ID':'W4', 'Title':'ML',' Seats_Available':3},
    ]

participants = {
        'Alice': ['W1'],
        'Bob': ['W1', 'W2'],
        'Reef':['W3','W4'],
    }

def search_workshop(workshops, Workshop_ID):
    for work in workshops :
        if work['Workshop_ID']==Workshop_ID:
            return work
    else:
        return"This workshop ,it does not"
    

work=input("Enter the worksho ID : ")
print(search_workshop(workshops, work))



def register_workshop(workshops, participants, participant_name, Workshop_ID):
    work=search_workshop(workshops, Workshop_ID)
    if work=="This workshop ,it does not":
        print("This workshop ,it does not")
        


    if work['Seats_Available'] > 0:
        participants.setdefault(participant_name, []).append(Workshop_ID)
        work['Seats_Available']-=1
       # participants[participant_name] = [Workshop_ID]
        print(f"Registration successful for {participant_name} in {work['Title']}")
    elif Workshop_ID in participants.get(participant_name , []):
        print(f"Sorry, {participant_name} you are already registered in this {work['Title']}")
    else:
        print(f"invalid register in {workshops('Title')}, workshop is full")


ID=str(input("Enter the worksho ID that want register it : "))
name=str(input("please enter your name: "))
register_workshop(workshops, participants, name, ID)
    


def cancel_registration(workshops, participants, participant_name, Workshop_ID):
    work=search_workshop(workshops, Workshop_ID)
    if work=="This workshop ,it does not":
        print("This workshop ,it does not")
    
    if participant_name in participants and Workshop_ID in participants[participant_name]:
        participants[participant_name].remove(Workshop_ID)
        work['Seats_Available'] += 1
        print(f"Registration canceled for {participant_name} in {work['Title']}")
    else:
        print(f"Registration not found for {participant_name} in {work['Title']}.")
    
mame=input("Do you want to cancel registration? Enter your name: ")
ID=input("Enter Workshop ID : ")
cancel_registration(workshops, participants, name, ID)


def list_workshops(participants, participant_name):
    if participant_name in participants:
        print(participants[participant_name])
    else:
        print("Participant not found.")
    

name=input("that lists all the workshops a participant is registered for, Enter name : ")
list_workshops(participants, name)

def list_participants(workshops, participants, Workshop_ID):
    participant_list = [name for name, workshops_list in participants.items() if Workshop_ID in workshops_list]
    if participant_list:
        print(participant_list)
    else:
        print("No participants registered for this workshop.")

ID=input("that lists all the participants registered for a given workshop: ")
list_participants(workshops, participants,ID)

