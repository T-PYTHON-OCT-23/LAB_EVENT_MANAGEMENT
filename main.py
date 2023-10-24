
workshops = [
    {'Workshop_ID': 'W1', 'Title': 'Photography Basics', 'Seats_Available': 20},
    {'Workshop_ID': 'W2', 'Title': 'Intro to Python', 'Seats_Available': 15},
    
]#List

participants = {
    'Alice': ['W1'],
    'Bob': ['W1', 'W2'],  
}

Workshop_ID = input("please input the id :").upper()
def searchWorkshop(workshops, Workshop_ID): #done 
   
    res=[]
    for item in workshops:
        if Workshop_ID in item.values():
            res.append(item)   
    return res
  

res = searchWorkshop(workshops, Workshop_ID)
print(res) 


def register_workshop(workshops, participants, participant_name, Workshop_ID):
     
    
     return

def cancel_registration(workshops, participants, participant_name, Workshop_ID):
     key=1
     for i in participants:
       if participant_name in participants:
          participants.pop(participants.get(participant_name) )
       for i in workshops:
        if i["Workshop_ID"] == Workshop_ID: 
           workshops['Seats_Available'] - key
       return participants



def list_workshops(participants, participant_name):
     listofW = participants.get(participant_name)
     return listofW
   

def list_participants(workshops, participants, Workshop_ID):
    


#list_participants(workshops, participants, Workshop_ID)
 print("output of list of workshops : ")
print(list_workshops( participants, 'Alice'))

