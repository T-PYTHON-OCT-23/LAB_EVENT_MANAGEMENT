workshops = [
        {'Workshop_ID': 'W1', 'Title': 'Photography Basics', 'Seats_Available': 20},
        {'Workshop_ID': 'W2', 'Title': 'Intro to Python', 'Seats_Available': 15},
        {'Workshop_ID': 'W3', 'Title': 'Intro to AI', 'Seats_Available': 20},

        # ...
    ]

participants = {
        'Alice': ['W1'],
        'Bob': ['W1', 'W2'],

        # ...
    }

def search_workshop(workshops, Workshop_ID):
    '''
    the workshops list and a Workshop_ID as input.The function should return the workshop 
    details if it exists or a message indicating it does not.'''
    for x in search_workshop:
        if x in search_workshop:
            result = print(f"{Workshop_ID} registerd in {workshops} ")
    else: 
        print("sorry, you havn't registerd yet")

        return result


def register_workshop(workshops, participants, participant_name, Workshop_ID):
    '''that registers a participant for a workshop if seats are available'''
while register_workshop(Seats_Available] == register_workshop(Seats_Available.getValue()) :



def list_workshops(participants, participant_name) :

    ''' **List Workshops for a Participant**: Write a function 
list_workshops(participants, participant_name) that lists all the workshops a participant is registered for.'''



def list_participants(workshops, participants, Workshop_ID):
    '''**List Participants for a Workshop**: Write a function `
list_participants(workshops, participants, Workshop_ID)` that lists all the participants registered for a given workshop'''