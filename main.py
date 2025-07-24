''' IMPORTS '''
import spacy, time

''' MODULES '''
from modules.line_delay_animation import line_delay_animation
from modules.character_delay_animation import character_delay_animation
from modules.clear_screen import clear_screen
from modules.display_format import display_format

''' FUNCTIONS: UTILITY '''
def tasky_response(message):
    character_delay_animation(f"[TASKY]: {message}", 0.02)

''' DEPENDENCIES '''
nlp = spacy.load("en_core_web_sm") # Load English model
to_do_list = [] # Store list of things to do

''' FUNCTIONS: MAIN '''
# FUNCTION: Add task to the list
def add_to_list(task):
    to_do_list.append(task)
    tasky_response(f"I've added \"{task}\".")

# FUNCTION: Remove task from the list
def remove_from_list(task):
    
    to_do_list.remove(task)
    tasky_response(f"I've removed \"{task}\".")

# FUNCTION: Display task list
def display_list():
    tasky_response("Let me show your task list!")
    print("{ ~~~ Task List ~~~ }")
    time.sleep(0.5)
    for task in to_do_list:
        print(f"* {task}")
        time.sleep(0.3)

# FUNCTION: Exit the program
def exit_tasky():
    tasky_response("See you next time!")
    time.sleep(1)

# FUNCTION: Process user's command using Natural Language Processing(NLP)
def process_command(user_command):
    doc = nlp(user_command)

    # Add task to the list
    if any(token.lemma_ == "add" for token in doc):
        for i, token in enumerate(doc):
            if token.pos_ == "VERB": # If verb is found
                for j, token in enumerate(doc[i+1:]):
                    if token.pos_ == "VERB": # If second verb is found
                        task_to_add = [word.text for word in doc[i+1:]]
                        add_to_list(' '.join(task_to_add))
                        break

    # Remove task from the list
    elif any(token.lemma_ == "remove" for token in doc):
        for i, token in enumerate(doc):
            if token.pos_ == "VERB": # If verb is found
                for j, token in enumerate(doc[i+1:]):
                    if token.pos_ == "VERB": # If second verb is found
                        task_to_remove = [word.text for word in doc[i+1:]]
                        remove_from_list(' '.join(task_to_remove))
                        break

    # Display task list
    elif any(token.lemma_ == "display" for token in doc):
        display_list()

    # Exit the program
    elif any(token.lemma_ == "exit" for token in doc):
        exit_tasky()

    # Unrecognized command
    else:
        tasky_response("Sorry, I did not recognize that...")

# FUNCTION: Display Tasky's interface
def display_interface():

    # Display header
    clear_screen()
    character_delay_animation("[------------| TASKY |------------]", 0.02)
    
    # Display Tasky's message
    tasky_response("What would you like to do?")

    while True:
        # Prompt user to enter a task
        user_command = input("  [YOU]: ").strip().lower()

        # Process user's command
        process_command(user_command)

display_interface() # Start program
