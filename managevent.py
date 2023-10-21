# 1
empty_set = set()
empty_dictionary = {}

workshops_list = [{"workshop ID": "W1", "Title": "Python", "seats_available": 16},
                  {"workshop ID": "W2", "Title": "Javascript", "seats_available": 10},
                  {"workshop ID": "W3", "Title": "Php", "seats_available": 12},
                  {"workshop ID": "W4", "Title": "flutter", "seats_available": 22}]

# 2

participants = {
    "Hadeel": ["W1"],
    "Manal": ["W2"],
    "Sara": ["W1", "W3"],
    "Farah": ["W2", "W4"],
    "Maya": ["W4"]
}

#3


def search_workshop(workshops, workshop_ID):
    for n in workshops:
        if workshop_ID in workshops["workshop_ID"]:
            return print(f"the workshop exists")
        return print(f"The title is {workshops_list['Title']},and the seats available are {workshops_list['Seats_available']}")
    else:
        print("not found !")


user_workshop = input("Enter your workshop: ")
search_workshop("Python", "W1")

#4
def register_workshop(workshops, participants, participant_name, Workshop_ID):
    workshops = workshops_list.append()
    if workshops_list['seats_available'] < 16:
        participants = register_workshop.insert(1,"Hadeel")

workshops = workshops_list
participant_name = "Hadeel"
Workshop_ID = "W1"

register_workshop(workshops, participants, participant_name, Workshop_ID)

#5
def cancel_registration(workshops, participants, participant_name, Workshop_ID):
    del register_workshop()

cancel_registration(workshops, participants, participant_name, Workshop_ID)

#6
def list_workshops(participants, participant_name):
    for participants, participant_name in list_workshops:
        return participants, participant_name
    print(participants, participant_name)

    workshop_input = input("Enter yor workshop: ")
    if  workshop_input in workshops_list:
     print(f"The workshop {workshop_input} is found in {workshops_list['Title']}")
    else:
     print(f"Sorry we don't have the info for {workshop_input}")

list_workshops(participants, participant_name)

#7

def list_participants(workshops, participants, Workshop_ID):
    for register_workshop in workshops_list:
        return workshops, participants, Workshop_ID
    print(workshops, participants, Workshop_ID)

    participants_input = input("Enter yor participants: ")
    if participants_input in participants:
     print(f"The workshop {participants_input} is found in {participants['participant_name']}")
    else:
     print(f"Sorry we don't have the info for {participants_input}")

list_participants()