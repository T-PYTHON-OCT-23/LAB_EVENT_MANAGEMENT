restorant = [
    {'Restorant_Name': 'The Spice Spoon', 'Tyep_of_Food': 'Mexican cuisine', 'Available_Tables': 10},
    {'Restorant_Name': 'Bella Italia', 'Tyep_of_Food': 'Italian cuision', 'Available_Tables': 2},
   ''' {'Restorant_Name': 'Sushi Hous', 'Tyep_of_Food': 'Japanese cusine', 'Available_Tables': 5},
    {'Restorant_Name': 'Curry House', 'Tyep_of_Food': 'Indian cuisine', 'Available_Tables': 7},
    {'Restorant_Name': 'The Steakhouse', 'Tyep_of_Food': 'Amirican Steakhouse', 'Available_Tables': 14},'''
]

choices_of_reestorant = {
    'James': ['The Steakhouse','Bella Italia'],
    'Mary': ['Curry House','Bella Italia','Bella Italia'],
    'John': ['The Spice Spoon', 'Curry House'],
    'Megan': ['Sushi Hous'],
    'Daniel': ['Sushi Hous', 'The Steakhouse']
}

#sarch for restorance 
def search_restorant(restorant , Restorant_Name):
    print(input("Enter restorant name :" )) 
    for name in restorant:
        if name ['Restorant_Name'] == Restorant_Name:
            return restorant
        else:
            return "restorant not found"
search_restorant(restorant , 'Bella Italia')

#reservation a table in restorant
def table_resrvation (restorant ,choices_of_reestorant , choices_of_reestorant_name , Restorant_Name):
    name = search_restorant(restorant , Restorant_Name)
    if name == "restorant not found" :
        return "Invalid restorant name"
    if name ['Available_Tables']>0 :
        if choices_of_reestorant_name in choices_of_reestorant :
           choices_of_reestorant[choices_of_reestorant_name].append(Restorant_Name)
        else:
            choices_of_reestorant[choices_of_reestorant_name] = Restorant_Name

            name['Available_Tables'] -= 1
            return "reservation successfuly"
    else:
        return 'No available tables'
table_resrvation(restorant,choices_of_reestorant , 'Mary' ,'Bella Italia')
    
# cancel reservation
def cancel_resrvation (restorant ,choices_of_reestorant , choices_of_reestorant_name , Restorant_Name):
    if choices_of_reestorant_name in choices_of_reestorant and Restorant_Name in choices_of_reestorant[choices_of_reestorant_name]:
        choices_of_reestorant[choices_of_reestorant_name].remove(Restorant_Name)

        for name in restorant:
            if name['Restorant_Name'] == Restorant_Name:
               name['Available_Tables'] += 1
               break
        return 'resrvation canceled successfully'
    else:
        return 'not found'

#list of restorant for choices_of_reestorant
def list_of_restorant (choices_of_reestorant , choices_of_reestorant_name):
    if choices_of_reestorant_name in choices_of_reestorant:
        return choices_of_reestorant[choices_of_reestorant_name]
    else:
        return "choices_of_reestorant not found"
    
#list of choices_of_reestorant for restorant
def list_choices_of_reestorant (restorant ,choices_of_reestorant , Restorant_Name):
    __name__== search_restorant(restorant , Restorant_Name)
    if __name__ == 'restorunt not found':
        return "invalid restorant name"
    
    restorunt_resrvation = []
    for choices , restorunt_resrvation_resrvation in choices_of_reestorant.items():
        if Restorant_Name in table_resrvation:
            restorunt_resrvation.append(choices)
    return restorunt_resrvation

'''# Example usage
Restorant_Name = 'The Spice Spoon'
restorant_details = search_restorant(restorant , Restorant_Name)
print("Restorant Details:")
print(restorant_details)

choices_of_reestorant_name = 'James'
Restorant_Name = 'The Steakhouse'
reservation_status = table_resrvation(restorant, choices_of_reestorant, choices_of_reestorant_name, Restorant_Name)
print("\nReservation Status:", reservation_status)

Restorant_Name = 'The Steakhouse'
cancellation_status = cancel_resrvation(restorant, choices_of_reestorant, choices_of_reestorant_name, Restorant_Name)
print("\nCancellation Status:", cancellation_status)

choices_of_reestorant_name = 'Mary'
restorantList =  list_of_restorant(choices_of_reestorant, choices_of_reestorant_name)
print("\nrestorant for", choices_of_reestorant_name)
print(restorantList)

Restorant_Name = 'The Spice Spoon'
choicesList = list_choices_of_reestorant(restorant, choices_of_reestorant, Restorant_Name)
print("\nthe choise restorant", Restorant_Name)
print(choicesList)'''


            