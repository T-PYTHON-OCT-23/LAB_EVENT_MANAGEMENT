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
    return 'Workshop is not found.'

#dictionary.setdefault(keyname, value) dictionary هذي خاصه ب 
def register_workshop(workshops, participants, participant_name, Workshop_ID):
    for workshop in workshops:
        if workshop['Workshop_ID'] == Workshop_ID and workshop['Seats_Available'] > 0:
            participants.setdefault(participant_name, []).append(Workshop_ID)
            workshop['Seats_Available'] -= 1
            return 'Registration is done successfully.'
    return 'Workshop is not found or there are no available seats.'

def cancel_registration(workshops, participants, participant_name, Workshop_ID):
    if participant_name in participants and Workshop_ID in participants[participant_name]:
        participants[participant_name].remove(Workshop_ID)
        for workshop in workshops:
            if workshop['Workshop_ID'] == Workshop_ID:
                workshop['Seats_Available'] += 1
        return 'Cancellation is done successfully.'
    return 'Participant or workshop is not found'

def list_workshops(participants, participant_name):
#get(participant_name, هذي الرساله يطلعها اذا مو موجود')
    return participants.get(participant_name, 'Participant not found')

def list_participants(workshops, participants, Workshop_ID):
  print(f'The following participants are registered for workshop {Workshop_ID}:')
  for participant_name, workshops in participants.items():
    if Workshop_ID in workshops:
      print(f'{participant_name}')



print(search_workshop(workshops,'W1'))
print(register_workshop(workshops,participants,'Aseel','W2'))
print(cancel_registration(workshops, participants,'Alice', 'W1'))
print(list_workshops(participants, 'Bob'))
list_participants(workshops, participants, 'W2')




