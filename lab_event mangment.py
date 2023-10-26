workshops = [
        {'Workshop_ID': 'W1', 'Title': 'Photography Basics', 'Seats_Available': 20},
        {'Workshop_ID': 'W2', 'Title': 'Intro to Python', 'Seats_Available': 15},
        {'Workshop_ID': 'W3', 'Title': 'Artificial intelligence', 'Seats_Available': 10},
        # ...
    ]

participants = {
        'Alice': ['W1'],
        'Bob': ['W1', 'W2'],
        'Sufana':['W1','W3']
        # ...
    }

def search_workshop(workshops, Workshop_ID):
    if Workshop_ID == workshops[0]['Workshop_ID']:
        return workshops[0]
    elif Workshop_ID == workshops[1]['Workshop_ID']:
        return workshops[1]
    elif Workshop_ID == workshops[2]['Workshop_ID']:
        return workshops[2]
    else:
        print("No information for this workshop.")

def register_workshop(workshops, participants, participant_name, Workshop_ID):
    count = 0
    participants[participant_name] = [Workshop_ID]
    if Workshop_ID == workshops[0]['Workshop_ID']:
            count = workshops[0]['Seats_Available']-1
            print(f"only seats left {count}")
    elif Workshop_ID == workshops[1]['Workshop_ID']:
            count = workshops[1]['Seats_Available']-1
            print(f"only seats left {count}")
    elif Workshop_ID == workshops[2]['Workshop_ID']:
            count = workshops[2]['Seats_Available']-1
            print(f"only seats left {count}")
    else:
        print("Invaild input")

def cancel_registration(workshops, participants, participant_name, Workshop_ID):
    if participant_name in participants:
        if Workshop_ID in participants[participant_name]:
            count = 0 
            participants[participant_name].remove(Workshop_ID)
            count = workshops[1]['Seats_Available']+1
            print(participants)
    else:
        print("Invaild Input.")
        

def list_workshops(participants, participant_name):
    if participant_name in participants:
        print(f"{participant_name} is registered for: {participants[participant_name]}")
    else:
        print("Not found.")


def list_participants(workshops, participants, Workshop_ID):
        for parti_name,workshops in participants.items():
            if Workshop_ID in workshops:
                print(f"The participant registered for {Workshop_ID} : {parti_name}")


print("-"*22)
print("-----WELCOME TO OUR PROGRAM-----")
while True:
    option = input("Do you want to:\n 1-Search for a Workshop \n 2-Register for a Workshop \n 3-Cancel particepation \n 4-List Workshops for a Participant \n 5-List Participants for a Workshop\n 6-Exit.\n choose a number:")
    if option =="1":
        #**Search for a Workshop**
        for i in workshops:
            print(i)
        WorkshopID = input("Enter the workshop ID: ")
        print(f"The details of this workshop : {search_workshop(workshops,WorkshopID)} ")
        print("***Thank you for visiting our program****")
        
    elif option =="2":
        #**Register for a Workshop**
        print("Register for a Workshop")
        parti_name = input("Enter your name: ")
        new_WorkshopID = input("Enter the ID of workshop: ")
        register_workshop(workshops,participants,parti_name,new_WorkshopID)
        print(participants)
        print("***Thank you for visiting our program****")

    elif option =="3":
        #cancel particepation 
        print("TO CANCLE YOUR PARTICEPATION.")
        parti_name = input("Enter your name : ")
        WorkshopID = input("Enter the workshop ID :")
        cancel_registration(workshops,participants,parti_name,WorkshopID)
        print("***Thank you for visiting our program****")

    elif option == "4":
        #List Workshops for a Participant
        print("List Workshops for a Participant")
        name_participants = input("Enter your name: ")
        list_workshops(participants,name_participants)
        print("***Operartion is Done****")
        print("***Thank you for visiting our program****")

    elif option == "5":
        #List Participants for a Workshop
        Workshop_ID = input("Enter the workshop ID:")
        list_participants(workshops, participants, Workshop_ID)
        print("***Operartion is Done****")
        print("***Thank you for visiting our program****")

    elif option == "6":
        print("Bye, See you next time.")
        break

    else:
        print("Invaild input please choose any number from the above.")

