workshops = [
    {'Workshop_ID': 'W1', 'Title': 'Photography Basics', 'Seats_Available': 20},
    {'Workshop_ID': 'W2', 'Title': 'Intro to Python', 'Seats_Available': 15},
]

participants = {
    'Alice': ['W1'],
    'Bob': ['W1', 'W2'],
}

def search_workshop(workshops, Workshop_ID):
    for workshop in workshops:
        if workshop['Workshop_ID'] == Workshop_ID:
            return workshop
    raise Exception('No workshop found with ID: {}'.format(Workshop_ID))

def register_workshop(workshops, participants, participant_name, Workshop_ID):
    workshop=search_workshop(workshops,Workshop_ID)
    if workshop['Seats_Available']>=1:
        workshop['Seats_Available']-=1
        if participant_name not in participants:
            participants[participant_name]=[]
        participants[participant_name].append(Workshop_ID)
        return True
    raise Exception('No seats left in {}'.format(Workshop_ID))

def list_workshops(participants, participant_name):
    return participants[participant_name]

def cancel_registration(workshops, participants, participant_name, Workshop_ID):
    workshop=search_workshop(workshops,Workshop_ID)
    list_works=list_workshops(participants,participant_name)
    if Workshop_ID in list_works:
        participants[participant_name].remove(Workshop_ID)
        workshop['Seats_Available']+=1
        return True
    raise  Exception('No participant {} in {} '.format(participant_name,Workshop_ID))

def list_participants(workshops, participants, Workshop_ID):
    temp=[]
    for participant , workshops in participants.items():
        if Workshop_ID in workshops:
            temp.append(participant)
    return temp


print(list_participants(workshops,participants,'W1'))
print(register_workshop(workshops,participants,'Bader','W1'))
print(list_participants(workshops,participants,'W1'))
print(list_workshops(participants,'Bader'))
print(cancel_registration(workshops,participants,'Bader','W1'))
print(list_participants(workshops,participants,'W1'))