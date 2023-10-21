restorant = [
    {'Restorant_Name': 'The Spice Spoon', 'Type_of_Food': 'Mexican cuisine', 'Available_Tables': 10},
    {'Restorant_Name': 'Bella Italia', 'Type_of_Food': 'Italian cuisine', 'Available_Tables': 2},
    {'Restorant_Name': 'Sushi House', 'Type_of_Food': 'Japanese cuisine', 'Available_Tables': 5},

]

choices_of_restaurant = {
    'James': ['Sushi House','Bella Italia'],
    'Mary': ['The Spice Spoon', 'Bella Italia','Sushi House'],
    'Bob': ['The Spice Spoon']
}


# Search for a restaurant
def search_restaurant(restaurants, restaurant_name):
    for restaurant in restaurants:
        if restaurant['Restorant_Name'] == restaurant_name:
            return restaurant
    return "Restaurant not found"
#test search_restaurant
restauant_name = 'Spoon'
result = search_restaurant(restorant,restauant_name)
print(result)


# Reserve a table in a restaurant
def table_reservation(restaurants, choices_of_restaurant, customer_name, restaurant_name):
    restaurant = search_restaurant(restaurants, restaurant_name)
    if restaurant == "Restaurant not found":
        return "Invalid restaurant name"
    if restaurant['Available_Tables'] > 0:
        if customer_name in choices_of_restaurant:
            choices_of_restaurant[customer_name].append(restaurant_name)
        else:
            choices_of_restaurant[customer_name] = [restaurant_name]

        restaurant['Available_Tables'] -= 1
        return "Reservation successful"
    else:
        return 'No available tables'
#test table_reservation
customer_name ='James'
restauant_name = 'Bella Italia'
result= table_reservation(restorant,choices_of_restaurant,customer_name,restauant_name)
print(result)


# Cancel reservation
def cancel_reservation(restaurants, choices_of_restaurant, customer_name, restaurant_name):
    if customer_name in choices_of_restaurant and restaurant_name in choices_of_restaurant[customer_name]:
        choices_of_restaurant[customer_name].remove(restaurant_name)

        for restaurant in restaurants:
            if restaurant['Restorant_Name'] == restaurant_name:
                restaurant['Available_Tables'] += 1
                break
        return 'Reservation canceled successfully'
    else:
        return 'Reservation not found'
#test cancel_reservation
customer_name ='James'
restauant_name = 'Bella Italia'
result= cancel_reservation(restorant,choices_of_restaurant,customer_name,restauant_name)
print(result)


# List of restaurants for a customer
def list_of_restaurants(choices_of_restaurant, customer_name):
    if customer_name in choices_of_restaurant:
        return choices_of_restaurant[customer_name]
    else:
        return "Customer not found"
#test
customer_name ='Bee'
result= list_of_restaurants(choices_of_restaurant, customer_name)
print(result)


# List of customers for a restaurant
def list_of_customers(restaurants, choices_of_restaurant, restaurant_name):
    restaurant = search_restaurant(restaurants, restaurant_name)
    if restaurant == 'Restaurant not found':
        return "Invalid restaurant name"

    customers_reservation = []
    for customer, reservations in choices_of_restaurant.items():
        if restaurant_name in reservations:
            customers_reservation.append(customer)
    return customers_reservation
#test list_of_customers
restauant_name = 'mac'
result= list_of_customers(restorant, choices_of_restaurant, restauant_name)
print(result)




'''# Test the functions
print(table_reservation(restorant, choices_of_restaurant, 'James', 'Bella Italia'))
print(table_reservation(restorant, choices_of_restaurant, 'John', 'Sushi House'))
print(cancel_reservation(restorant, choices_of_restaurant, 'James', 'Bella Italia'))
print(cancel_reservation(restorant, choices_of_restaurant, 'John', 'Sushi House'))
print(list_of_restaurants(choices_of_restaurant, 'James'))
print(list_of_customers(restorant, choices_of_restaurant, 'Bella Italia'))
print(table_reservation(restorant, choices_of_restaurant, 'James', 'Bella'))'''
