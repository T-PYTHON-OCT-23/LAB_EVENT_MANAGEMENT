workshops = [
    {'Workshop_ID': 'W1', 'Title': 'Photography Basics', 'Seats_Available': 20},
    {'Workshop_ID': 'W2', 'Title': 'Intro to Python', 'Seats_Available': 15},
    # ...
]

participants = {
    'Alice': ['W1'],
    'Bob': ['W1', 'W2'],
    # ...
}

def add_workshop():
    while True:
        exit = input("if you want out input 'exit' and if you want add workshop input anything : ")
        if exit == "exit":
            break
        workshop = {}
        workshop["Workshop_ID"] = input("enter workshop ID : ")
        workshop["Title"] = input("enter workshop title : ")
        workshop["Seats_Available"] = input("enter seats available in workshop  : ")
        workshops.append(workshop)
        print("done add workshop successfully")
        
def participant_registration():
    while True:
        exit = input("if you want out input 'exit' and if you want add workshop input anything : ")
        if exit == "exit":
            break
        workshop_ID = []
        name_participant = input("enter name participant : ")
        participants.append(name_participant)
        workshop_ID.append(input("enter workshop_ID : "))
        participants[name_participant] = workshop_ID
        
        print("done add participant successfully")    

def search_workshop(workshops, Workshop_ID):
    count = 0 
    for workshop in workshops:
        if workshops[count]["Workshop_ID"] == Workshop_ID:
            print(f"the title workshop :{workshops[count].get('Title')}, and seats avaliable : {workshops[count].get('Seats_Available')} ")
            break
        else: 
            print("the workshop can not found ")
            count += 1

def register_workshop(workshops, participants, participant_name, Workshop_ID):
    count = 0 
    for workshop in workshops:
        if workshops[count]["Workshop_ID"] == Workshop_ID and workshops[count]["Seats_Available"] > 0 :
            participants[participant_name].append(Workshop_ID) 
            workshops[count].update(Seats_Available = workshops[count].get("Seats_Available")-1)
            print(f"done add {participant_name} in workshop {Workshop_ID} successfully")
            break
        if workshops[count]["Workshop_ID"] == Workshop_ID and workshops[count]["Seats_Available"] <= 0 :
            print("There is no seat available") 
            break   
        else:
            count += 1
    print("the workshop can not found ")
            
def cancel_registration(workshops, participants, participant_name, Workshop_ID):
    count = 0 
    for workshop in workshops:
        if workshops[count]["Workshop_ID"] == Workshop_ID and  Workshop_ID in participants[participant_name]:
            participants[participant_name].pop(Workshop_ID) 
            workshops[count].update(Seats_Available = workshops[count].get("Seats_Available")+1)
            print(f"done cancel {participant_name} in workshop {Workshop_ID} successfully")
            break   
        else:
            count += 1
            
    print("the workshop can not found ")         

def list_workshops(participants, participant_name):
    for participant in participants :
        if participant == participant_name:
            print(" Registered workshops ", participant_name , participants.get(participant_name))  
            break
        else:
          print(" can not found ",participant_name)    
        
def list_participants(workshops, participants, Workshop_ID) :
    for participant in participants :
        if Workshop_ID in participants.get(participant):
            print(participant)
        else:
            print("There is no one registered for this workshop")
        

