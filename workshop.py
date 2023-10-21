#1.Initialize Workshops**: Create a list of dictionaries, where each dictionary represents 
#a workshop with attributes like 'Workshop_ID', 'Title', and 'Seats_Available'.

workshops = [
        {'Workshop_ID': 'W1', 'Title': 'Photography Basics', 'Seats_Available': 20},
        {'Workshop_ID': 'W2', 'Title': 'Intro to Python', 'Seats_Available': 15},
        {'Workshop_ID': 'W3', 'Title': 'Intro to Java', 'Seats_Available': 10},
        {'Workshop_ID': 'W4', 'Title': 'Intro to Java', 'Seats_Available': 25},
    ]
     
    
#2.Participant Registration**: Create a dictionary where the keys are participant names and the values are lists of workshops they've registered for.
   
participants = {
        'Alice': ['W1'],
        'Bob': ['W1', 'W2'],
        'Naif': ['W1','W4'],
        'Abdullah': ['W3', 'W2'],
    }

print(participants.values())
print(participants.keys())
print(participants.get("Bob")) 

#*****

def search_workshop(workshops, Workshop_ID):
  for workshop in workshops:
   if workshop['Workshop_ID'] == Workshop_ID:
       return workshop
   
    #return "Workshop not found."

n = search_workshop(workshops, 'W4')

if isinstance(n, dict):
    print( f"Workshop{n['Workshop_ID']} - {n['Title']}, Seats Available: {n['Seats_Available']} ")
else:
    print(n)

#********

def register_workshop(workshops, participants, participant_name, Workshop_ID):

  # Check if the participant_name exists in the participants dictionary
 if participant_name in participants:
 # Check if the participant is already registered for the workshop
  if Workshop_ID not in participants[participant_name]:
   for workshop in workshops:
     if workshop['Workshop_ID'] == Workshop_ID:
      seats_available = workshop['Seats_Available']
   if seats_available > 0:

    participants[participant_name].append(Workshop_ID)
    workshop['Seats_Available'] -= 1      
    print(f"{participant_name} is now registered for Workshop {Workshop_ID}.")
 
 else:
  
  print(f"No available seats in Workshop {Workshop_ID}.")

  print(f"{participant_name} is already registered for Workshop {Workshop_ID}.")
        
  register_workshop(workshops, participants, 'Alice', 'W2')

#****

def cancel_registration(workshops, participants, participant_name, Workshop_ID):
  pass

#*****
def list_workshops(participants, participant_name):
  for n in participants:
       if n==participant_name:
        print(n)
        print(participants.values())
        print(len(['Alice','Bob','Naif','Abdullah',]))
#****
def list_participants(workshops, participants, Workshop_ID):
   for n in workshops:
       if n==participants:
        print(n)
        print(Workshop_ID.keys())
        print(len([['W1'],['W1', 'W2'],['W1','W4'],['W3', 'W2']]))

