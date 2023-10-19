workshops = [
    {'Workshop_ID': 'W1', 'Title': 'Photography Basics', 'Seats_Available': 20},
    {'Workshop_ID': 'W2', 'Title': 'Intro to Python', 'Seats_Available': 15},
]
participants = {
    'Alice': ['W1'],
    'Bob': ['W1', 'W2'],
}


def search_workshop(workshops, Workshop_ID) -> print:

    for workshop in workshops:
        print(workshop)
        print(len(workshop),"-----",len(workshops))
        if Workshop_ID in workshop['Workshop_ID']:
            return print(f"{Workshop_ID} is there, more detils about:\n Title: {workshop['Title']}\n Seats Available: {workshop['Seats_Available']}")
        if len(workshop) == len(workshops):
            return print("Workshop is not found")

user_input = input("Please enter workshop you locking for: ")
search_workshop(workshops,user_input)

def register_workshop(workshops, participants, participant_name, Workshop_ID):
    for workshop in workshops:
        if workshop['Workshop_ID'] in workshops and g:
            if workshop['Seats_Available'] > 0:
                participants[participant_name] = Workshop_ID
                

participants_names = "Hazal"
workshops_id = "W1"
register_workshop(workshops,participants,participants_names,workshops_id)