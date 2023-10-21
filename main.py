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
            print(" ------\n",f"{Workshop_ID} is there, more detils about:\n Title: {workshop['Title']}\n Seats Available: {workshop['Seats_Available']}\n","------")

user_input = input("Please enter workshop you locking for: ")
search_workshop(workshops,user_input)


def register_workshop(workshops, participants, participant_name, Workshop_ID):
    for workshop in workshops:
        if Workshop_ID in workshop["Workshop_ID"] and workshop['Seats_Available'] > 0:
            participants = {
                participant_name: [Workshop_ID],
            }
            print("Registration successfully")
            return participants

print("Note: If you want to register with us, fill the form below:")               
print("-"*4,"Registeration Form","-"*4)
participants_names = input("Enter your name: ")
workshops_id = input("Enter workshop name. Note: workshop name like: (W1,W2 etc...): ")
participants.update = register_workshop(workshops,participants,participants_names,workshops_id)
print(participants,"After registration")
participants_names = input("Enter your name: ")
workshops_id = input("Enter workshop name. Note: workshop name like: (W1,W2 etc...): ")
participants.update = register_workshop(workshops,participants,participants_names,workshops_id)
print(participants,"Try to add another workshop")