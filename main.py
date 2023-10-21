workshops = [
    {'Workshop_ID': 'W1', 'Title': 'Photography Basics', 'Seats_Available': 20},
    {'Workshop_ID': 'W2', 'Title': 'Intro to Python', 'Seats_Available': 15},
    {'Workshop_ID': 'W3', 'Title': 'AWS Solution', 'Seats_Available': 11},
    {'Workshop_ID': 'W4', 'Title': 'Startup', 'Seats_Available': 7},
]
participants = {
    'Alice': ['W1'],
    'Bob': ['W1', 'W2'],
    'Charlie': ['W2', 'W3']
}

def search_workshop(workshops, Workshop_ID) -> print:

    for workshop in workshops:
        if Workshop_ID in workshop['Workshop_ID']:
            print(" ------Detils: \n",f"{Workshop_ID} is there, more detils about:\n Title: {workshop['Title']}\n Seats Available: {workshop['Seats_Available']}\n","------")

user_input = input("Please enter workshop you locking for: ")
search_workshop(workshops,user_input)


def register_workshop(workshops, participantse, participant_name, Workshop_ID):
    for workshop in workshops:
        if Workshop_ID in workshop["Workshop_ID"] and workshop['Seats_Available'] > 0:
            if participant_name in participants:
                participants[participant_name].append(Workshop_ID)
            else:
                participants[participant_name] = [Workshop_ID]
            workshop['Seats_Available'] -= 1
            print("Registration successfully")
            return participants

print("Note: If you want to register with us, fill the form below:")               
print("-"*4,"Registeration Form","-"*4)
participants_names = input("Enter your name: ")
workshops_id = input("Enter workshop name. Note: workshop name like: (W1,W2 etc...): ")
participants = register_workshop(workshops,participants,participants_names,workshops_id)
print(participants,"After registration")
close = input("If you want to add another workshop enter ( 1 or exit ) to close: ")

if close == "1":
    participants_names = input("Enter your name: ")
    workshops_id = input("Note: workshop name like: (W1,W2 etc...): ")
    participants = register_workshop(workshops,participants,participants_names,workshops_id)
    print(participants,"After registration")
elif close == "exit":
    print("See you  soon! Bye")
else:
    print("please enter 1 or exit")


def cancel_registration(workshops, participantse, participant_name, Workshop_ID):
        if participant_name in participants:
            if Workshop_ID in participants[participant_name]:
                participants[participant_name].remove(Workshop_ID)
                for n in workshops:
                    if Workshop_ID == n['Workshop_ID']:
                        n['Seats_Available'] += 1
                    print("Cancel successflly")

participants_cancel = input("Enter name to cancel the paraticipate: ")
workshops_cancel = input("Enter the workshop you want to cancel: ")
cancel_registration(workshops,participants,participants_cancel,workshops_cancel)
print(participants,"After cancel")

def list_workshops(participantse, participant_name):
    if participant_name in participants:
        print(f"{participant_name} is participate in these workshop: {', '.join(participants[participant_name])}")

list_participate_name_in_workshop = input("Enter the name your search for: ")
list_workshops(participants,list_participate_name_in_workshop)

def list_participants(workshops, participants, Workshop_ID):
    if Workshop_ID in [workshop['Workshop_ID'] for workshop in workshops]:
        print(f"Participants registered for Workshop {Workshop_ID}:")
        for participant, workshops_list in participants.items():
            if Workshop_ID in workshops_list:
                print(participant)

workshop_list = input("Enter workshop you want to see who register in: ")
list_participants(workshops,participants,workshop_list)