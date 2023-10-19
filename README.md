
Imagine you are managing an event where people can register for various workshops. 
Each workshop has a limited number of seats. Participants can register for multiple workshops.

#### Exercise Description

1. **Initialize Workshops**: Create a list of dictionaries, where each dictionary represents a workshop with attributes like 'Workshop_ID', 'Title', and 'Seats_Available'.
    ```python
    workshops = [
        {'Workshop_ID': 'W1', 'Title': 'Photography Basics', 'Seats_Available': 20},
        {'Workshop_ID': 'W2', 'Title': 'Intro to Python', 'Seats_Available': 15},
        # ...
    ]
    ```

2. **Participant Registration**: Create a dictionary where the keys are participant names and the values are lists of workshops they've registered for.
    ```python
    participants = {
        'Alice': ['W1'],
        'Bob': ['W1', 'W2'],
        # ...
    }
    ```

3. **Search for a Workshop**: Write a function `search_workshop(workshops, Workshop_ID)` that takes the workshops list and a Workshop_ID as input. The function should return the workshop details if it exists or a message indicating it does not. 

4. **Register for a Workshop**: Write a function `register_workshop(workshops, participants, participant_name, Workshop_ID)` that registers a participant for a workshop if seats are available.

5. **Cancel Registration**: Write a function `cancel_registration(workshops, participants, participant_name, Workshop_ID)` that cancels a participant's registration for a workshop and frees up a seat.

6. **List Workshops for a Participant**: Write a function `list_workshops(participants, participant_name)` that lists all the workshops a participant is registered for.

7. **List Participants for a Workshop**: Write a function `list_participants(workshops, participants, Workshop_ID)` that lists all the participants registered for a given workshop.
