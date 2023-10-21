workshops = [
        {"Workshop_ID" : "W1", "Title": "Photography Basics", "Seats_Available": 20},
        {"Workshop_ID": "W2", "Title": "Intro to Python", "Seats_Available": 15},
        {"Workshop_ID": "W3", "Title": "Intro to JavaScript", "Seats_Available": 10},
        {"Workshop_ID": "W4", "Title": "Intro to IOS", "Seats_Available": 5}
    ]
participants = {
        "Alice": ["W1"],
        "Bob": ["W1", "W2"]
        }
def search_workshop(workshops, Workshop_ID):
    for i in workshops:    
        if i["Workshop_ID"] == Workshop_ID:
            print("*****************")

            for key , value in i.items():
                if  key == "Title" or key == "Seats_Available":
                    print(f"This is ({key}) for the workshop is ({value})")       
            break
    else:
        raise Exception (f"Sorry the workshp ({Workshop_ID}) don't found")

def register_workshop(workshops, participants, participant_name, Workshop_ID):
    for i in workshops:    
        if i["Workshop_ID"] == Workshop_ID:
            if i["Seats_Available"]  > 0:
                sub= i["Seats_Available"] - 1
                i["Seats_Available"] = sub
                if participant_name not in participants:
                    participants[participant_name]=[]
                participants[participant_name].append(Workshop_ID)    
                print("**********You have been registered successfully**********")   
            elif i["Seats_Available"] ==0:
                raise TypeError (f"**Sorry the all sets are reserved in ({Workshop_ID})**") 
        elif i["Workshop_ID"] != Workshop_ID:
                raise TypeError(f"The {Workshop_ID} not found !! ")            
def cancel_registration(workshops, participants, participant_name, Workshop_ID):
    for i in workshops:
        
        if i["Workshop_ID"]==Workshop_ID:
            if i["Seats_Available"] >=0:
                sum= i["Seats_Available"] + 1
                i["Seats_Available"] = sum
                participants[participant_name].remove(Workshop_ID)
                print("**********You have been cancle registered successfully**********")
        elif participant_name not in participants:
            raise TypeError (f"The {participant_name} haven't registered in {Workshop_ID}")     
        elif i["Workshop_ID"] != Workshop_ID:  
            raise Exception (f"The {Workshop_ID} not found !! ") 
         
               
def list_workshops(participants, participant_name):
    for key , value in participants.items():
        if key == participant_name :
            print(F"**this is all your workshops: ({value})**")
        if value == []:
            print("**You haven't registered befor,please register**")    

def list_participants(workshops, participants, Workshop_ID):
    workshops=[]
    for key , value in participants.items():
        if Workshop_ID in value:
            workshops.append(key)

    print(F"**This all names of participants registered: {workshops}**")

def main():
    while True:
        print("************Type Your Choic****************")
        print("*******************************To search for woekshops type: 1")
        print("*************************To registration for workshops type: 2")
        print("*************To cancel your registration for workshops type: 3")
        print("********************************To show your workshops type: 4")
        print("To show all participants registered for given workshop type: 5")
        print("**************************************IF ypu want exit tyoe: 0")
        
        
        user=input("Type your choice: ")
        try:
            if user == "0":
                for i in workshops:
                    print(f"Workshop dateils : {i}")    
                print("________________Good Bay_______________")
                break
            if user == "1":
                Workshop_ID = input("please type Workshop_ID: ")
                search_workshop(workshops,Workshop_ID)
        except Exception as e:
            print (e)  
        try:      
            if user == "2":
                participant_name =input("Type your name for registratio: ")
                Workshop_ID = input("please type Workshop ID: ")
                register_workshop(workshops, participants, participant_name, Workshop_ID)
        except Exception as e:
            print (e)  
        try:            
            if user == "3":
                Workshop_ID = input("please type Workshop ID: ")
                participant_name=input("Type your name for cancle registratio: ")
                cancel_registration(workshops, participants, participant_name, Workshop_ID)
        except Exception as e:
            print (e)  
        if user == "4":
            participant_name=input("Type your name for show your workshops: ")
            list_workshops(participants, participant_name)
        if user == "5":
            Workshop_ID = input("please type Workshop ID to show all participants registered: ")
            list_participants(workshops, participants, Workshop_ID)
print("___________Welcome to our workshops________________")        
main()      