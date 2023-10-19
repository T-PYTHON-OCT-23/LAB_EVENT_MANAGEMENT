#------------------------------------VARIABLES------------------------------------
workshops = [
        {'Workshop_ID': 'W1', 'Title': 'Photography Basics', 'Seats_Available': 20},
        {'Workshop_ID': 'W2', 'Title': 'Intro to Python', 'Seats_Available': 15},
        {'Workshop_ID': 'W3', 'Title': 'Cyper Security', 'Seats_Available': 0},
        {'Workshop_ID': 'W4', 'Title': 'Flutter', 'Seats_Available': 8}
    ]
participants = {
        'Alice': ['W1'],
        'Bob': ['W1','W2'],
        'Mohammed': ['W4','W1','W2','W3'],
        'Ahmed': ['W4', 'W1'],
        'Ali': ['W3']
    }
#------------------------------------FUNCTIONS------------------------------------
def search_workshop(workshops, Workshop_ID):
    for i in workshops:
        if Workshop_ID in i["Workshop_ID"]:
            print(Workshop_ID,"workshop already exists!")
            print(f"its title is {i["Title"]} and the seats available are {i["Seats_Available"]}")
            break
    else:
        print("This Workshop doesn't exist")
def register_workshop(workshops, participants, participant_name, Workshop_ID):
    _exit=0
    for i in workshops:
        if Workshop_ID in i["Workshop_ID"]:
            for j in participants:
                if participant_name == j:
                    if i["Seats_Available"]>0:
                        i["Seats_Available"] = i["Seats_Available"]-1
                        participants[participant_name].append(Workshop_ID)
                        _exit+=1
                        break
                    else:
                        raise Exception("Sorry, there is no seats available in this workshop.")
            else:
                raise Exception(f"{participant_name} is not in participants list.")
        if _exit!=0:
            break
    else:   
        raise Exception(f"{Workshop_ID} is not in the workshop list")

            
            
def cancel_registration(workshops, participants, participant_name, Workshop_ID):
    _exit=0
    for i in workshops:
        if Workshop_ID in i["Workshop_ID"]:
            for j in participants:
                if participant_name == j:
                    if Workshop_ID in participants[participant_name]:
                        i["Seats_Available"] = i["Seats_Available"]+1
                        participants[participant_name].remove(Workshop_ID)
                        _exit+=1
                        break
                    else:
                        raise Exception(f"{participant_name} is not taking {Workshop_ID}")
            else:
                raise Exception(f"{participant_name} is not in participants list.")
        if _exit!=0:
            break
    else:        
        raise Exception(f"{Workshop_ID} is not in the workshop list")
def list_workshops(participants, participant_name):
    _exit=0
    for i in participants:
        if i==participant_name:
            print(participant_name,"is now taking workshops: ", end=" ")
            for j in participants[i]:
                print(j,end = " ")
            print()
            _exit+=1
        if _exit!=0:
            break
    else:
        raise Exception(f"{participant_name} is not in participants list.")
def list_participants(workshops, participants, Workshop_ID):
    _exit=0
    for i in workshops:
        if i["Workshop_ID"]== Workshop_ID:
            for j in participants:
                if Workshop_ID in participants[j]:
                    print(f"( {j} )",end=" ")
            else:
                print(f"is/are participating in: {i["Title"]} workshop")
                break
    else:
        raise Exception(f"{Workshop_ID} is not in the workshop list")


#------------------------------------TESTING------------------------------------
try:
    search_workshop(workshops,"W4")
    #search_workshop(workshops,"W5")
    register_workshop(workshops,participants, "Ali", "W4")      # all good 
    #register_workshop(workshops,participants, "Alice", "W3")    # no seats available
    #register_workshop(workshops,participants, "khalid", "W1")   # participant is not available
    #register_workshop(workshops,participants, "Alice", "W5")    # workshop is not available
    #cancel_registration(workshops, participants, "Mohammed", "W2")
    #cancel_registration(workshops, participants, "Alice", "W3") 
    list_workshops(participants, "Mohammed")
    #list_workshops(participants, "Abdulrahaman")
    list_participants(workshops, participants, "W3")
    #print(participants)
    #print(workshops)
except Exception as e:
    print(e)