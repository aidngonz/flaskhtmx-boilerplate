# models/counter.py

counter = 0  # Global variable for the counter

def update_counter(action):
    global counter  # Use the global variable
    if action == 'increment':
        counter += 1
    elif action == 'decrement':
        counter -= 1
    return counter
