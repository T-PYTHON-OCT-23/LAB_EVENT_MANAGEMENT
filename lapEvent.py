workshops = [
    {'Workshop_ID': 'W1', 'Title': 'Photography Basics', 'Seats_Available': 20},
    {'Workshop_ID': 'W2', 'Title': 'Intro to Python', 'Seats_Available': 15},
    {'Workshop_ID': 'c1' , 'Title': 'Intro to java' ,'Seats_Available': 11  }
    # ...
]






participants = {
    'Alice': ['W1'],
    'Bob': ['W1', 'W2'],
    'Alix': ['c1']
    # ...
}



def search_workshop(workshops):
    Workshop_ID = input("enter name of workshop : ")
    for workshop in workshops:
        if workshop['Workshop_ID'] == Workshop_ID:
            return workshop
    return "Workshop not found."


result = search_workshop(workshops)
if result == "Workshop not found.":
    print("اworkshop not found . ")
else:
    print(f"deteles of workshop : {result}")

def register_workshop(workshops, participants):
    participant_name = input("اenter your name : ")
    Workshop_ID = input("enter workshop name :")

    workshop = search_workshop(workshops, Workshop_ID)
    
    if workshop == "Workshop not found.":
        return"Workshop not found."
    
    if workshop['Seats_Available'] > 0:
        if participant_name in participants:
            participants[participant_name].append(Workshop_ID)
        else:
            participants[participant_name] = [Workshop_ID]
        workshop['Seats_Available'] -= 1
        return f"{participant_name} regisetred in {workshop['Title']}."
    else:
        return f"no available seates {workshop['Title']}."

def cancel_registration(workshops, participants, participant_name, Workshop_ID):
     workshop = search_workshop(workshops, Workshop_ID)
    
     if workshop == "Workshop not found.":
        return"Workshop not found."
    
     if participant_name in participants:
          participants[participant_name]
          del(Workshop_ID)
          workshop['Seats_Available'] += 1
           
          
def list_workshops(participants, participant_name):
     if participant_name in participants:
          return participants[participant_name]         
     return  f"{participant_name} is not register for any workshops" 
 
def list_participants(workshops, participants, Workshop_ID):
    Workshop =search_workshop(workshops, Workshop_ID)
    if Workshop == "workshop not found":
        return "workshop not found"
   
    for name in participants:
        print(" participant name register in workshop :  {participant_name} ")

    
    
    



    








