workshops = [
        {"Workshop_ID" : "W1", "Title": "Photography Basics", "Seats_Available": 20},
        {"Workshop_ID": "W2", "Title": "Intro to Python", "Seats_Available": 15},
    ]
participants = {
        "Alice": ["W1"],
        "Bob": ["W1", "W2"]
        }
def search_workshop(workshops, Workshop_ID):
    for i in workshops:    
        if i["Workshop_ID"] == Workshop_ID:
            print(i)
            break
    else:
        print("Sorry the workshp don't found")

def register_workshop(workshops, participants, participant_name, Workshop_ID):
    for i in workshops:    
        if i["Workshop_ID"] == Workshop_ID:
            if i["Seats_Available"]  > 0:
                sub= i["Seats_Available"] - 1
                i["Seats_Available"] = sub
                participants[participant_name]=[Workshop_ID]
                print("_________You have been registered successfully______")
            elif i["Seats_Available"] ==0:
                print("Sorry the sets are full")    
def cancel_registration(workshops, participants, participant_name, Workshop_ID):
    for i in workshops:
        
        if i["Workshop_ID"]==Workshop_ID:
            if i["Seats_Available"] >=0:
                sum= i["Seats_Available"] + 1
                i["Seats_Available"] = sum
                del participants[participant_name]
                print("_________You have been cancle registered successfully______")
def list_workshops(participants, participant_name):
    for key , value in participants.items():
        if key == participant_name :
            print(F"this is all your workshops: {value}")   
def list_participants(workshops, participants, Workshop_ID):
    for key , value in participants.items():
        if value == [Workshop_ID]:
           print(F"This all names of participants registered: {[key]}")

def main():
    while True:
        print("___________Welcome to our workshops________________")
        print("To search for woekshops type: 1")
        print("To registration for workshops type: 2 ")
        print("To cancel your registration for workshops type: 3 ")
        print("To show your workshops type: 4 ")
        print("To show all participants registered for given workshop type: 5 ")
        print("IF ypu want exit tyoe: 0")
        
        
        user=input("Type your choice: ")
        if user == "0":
            break
        if user == "1":
            Workshop_ID = input("please type Workshop_ID: ")
            search_workshop(workshops,Workshop_ID)
        if user == "2":
            participant_name =input("Type your name for registratio: ")
            Workshop_ID = input("please type Workshop ID: ")
            register_workshop(workshops, participants, participant_name, Workshop_ID)
        if user == "3":
            participant_name=input("Type your name for cancle registratio: ")
            Workshop_ID = input("please type Workshop ID: ")
            cancel_registration(workshops, participants, participant_name, Workshop_ID)
        if user == "4":
            participant_name=input("Type your name for show your workshops: ")
            list_workshops(participants, participant_name)
        if user == "5":
            Workshop_ID = input("please type Workshop ID to show all participants registered: ")
            list_participants(workshops, participants, Workshop_ID)
        
main()
print(workshops)
print(participants)
        