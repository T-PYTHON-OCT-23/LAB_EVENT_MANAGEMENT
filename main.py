
workshops = [
    {'Workshop_ID': 'W1', 'Title': 'Photography Basics', 'Seats_Available': 20},
    {'Workshop_ID': 'W2', 'Title': 'Intro to Python', 'Seats_Available': 15},        
]


participants = {
    'Alice': ['W1'],
    'Bob': ['W2'],
}



def search_workshop(workshops:list, Workshop_ID:str)->str:
    result=""
    for i in workshops:
        if Workshop_ID == i["Workshop_ID"]:
            for key , value in i.items():

                result+= f"{key}: {value}\n"
            break
            
    if  Workshop_ID != i["Workshop_ID"]:
        return "sory!! workshop not found:"
    return result 
    

def register_workshop(workshops, participants, participant_name, Workshop_ID):
    
    
    list_workshop_id=[]

    seats_available=0 
    for i in workshops:
        if Workshop_ID == i["Workshop_ID"]:
            
           
           i["Seats_Available"]=i["Seats_Available"]-1
           seats_available=i["Seats_Available"]
           if seats_available==1:
               print("sorry seats full")
               break

        if Workshop_ID == i["Workshop_ID"]:
            list_workshop_id.append(Workshop_ID)   
            participants[participant_name]=list_workshop_id

        else:print("sorry the workshop not find")

           
    
    


def cancel_registration(workshops, participants, participant_name, Workshop_ID):


    for i in workshops:
        participants[participant_name]=[Workshop_ID].remove(Workshop_ID)

     

def list_workshops(participants, participant_name):
    print(participants[participant_name])
    

def list_participants(workshops, participants, Workshop_ID):
    

    result=""
    for i in workshops:
        if Workshop_ID == i["Workshop_ID"]:
            for key , value in participants.items():

                result+= f"{key} join in {value}\n"
            break
                    
    if  Workshop_ID != i["Workshop_ID"]:
        return "sory!! workshop not found:"
    return result


try:
    while True:

        searsh=input("to display workshop info enter workshop ID,to exit write exit: ")
        if searsh=="exit":
            break
        if search_workshop(workshops,searsh) =="sory!! workshop not found:":
            print("sory!! workshop not found:")
            continue
        
        print(search_workshop(workshops,searsh))

        register=input("to register in enter your name and the ID of the workshop:")
        name,id=register.split()
        

        


        list_=input("to display date of list participants Enter workshop ID:")
        cancel=input("to cancel register in enter your name and the ID of the workshop:")
        name_c,id_c = cancel.split()

        register_workshop(workshops,participants,name,id)
        cancel_registration(workshops,participants,name_c,id_c)
        list_workshops(participants,name)
        print(list_participants(workshops,participants,list_))
except Exception:
    print("sorry something went wrong!!!")
