

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




def search_workshop(workshops, Workshop_ID) :
    '''
    for i in workshops:
        if i.values() == Workshop_ID:
            return i 

'''

    
    for workshop in workshops:
        if workshop['Workshop_ID'] == Workshop_ID:
            return workshop
        
    return "Workshop not found."
    


'''
    for i in range(len(workshops)):
        if not workshops[i] in Workshop_ID:
            print("indicating it does not")
            break
        else:
            i.find(Workshop_ID) in workshops
            workshops[i] = str(i)
            return i.items()
        '''

#filter
#print(workshops['Seats_Available'].get())






def register_workshop(workshops, participants, participant_name, Workshop_ID):
    k=1
    for i in workshops:
        if i["Workshop_ID"] == Workshop_ID: 
            if participants.setdefault(participant_name):
                participants[participant_name] = Workshop_ID 
                workshops['Seats_Available'] - k
    
        
    #found = search_workshop(workshops , Workshop_ID)








def cancel_registration(workshops, participants, participant_name, Workshop_ID):
   k=1
   for i in participants:
       if participant_name in participants:
          participants.pop(participants.get(participant_name) )
   for i in workshops:
       if i["Workshop_ID"] == Workshop_ID: 
           workshops['Seats_Available'] - k
   return participants
    






listofW1=[]

#participants.get
def list_workshops(participants, participant_name):
     
     listofW1 = participants.get(participant_name)
     return listofW1
     
     '''
     for i in participants:
        l=participants.get(participant_name)
        listofW1.append(l)
     return listofW1
'''
     '''
     for i in participants:
        if participants.get(participant_name) == 'W1':
            listofW1.append(i)
        elif participants.get(participant_name) == 'W2':
            listofW2.append(i)
        else:
            print("somthing went wrong")
            
     return listofW1 , listofW2
'''


listOfPar=[]

def list_participants(workshops, participants, Workshop_ID ):
    for i in participants:
        if participants[i] == Workshop_ID:
            listOfPar.insert(1, participants.keys())
            #listOfPar= participants.keys()
    return listOfPar






#print(search_workshop(workshops,'W1'))

#workshop_id_to_search = 'W1'






print("\n")
result = search_workshop(workshops, 'W1')
print("output of search worksop : \n",result)
print("\n")
print("output of list of workshops : ")
print(list_workshops( participants, 'Alice'))
print("\n")
print("output of list of participants : ")
print(list_participants( workshops,participants, 'W2' ))
print("\n")
print("output of cancel registration : ")
print(cancel_registration(workshops, participants, "Bob", "W2"))
print("\n")
print("output of register workshop : ")
register_workshop(workshops, participants, "anoud", 'W2')
print(participants ,"\n", workshops)


