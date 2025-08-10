''' IMPORTS '''
import spacy, time

''' MODULES '''
from modules.line_delay_animation import line_delay_animation
from modules.character_delay_animation import character_delay_animation
from modules.clear_screen import clear_screen
from modules.display_format import display_format

''' FUNCTIONS: UTILITY '''
def tasky_response(message):
    character_delay_animation(f"[Tasky]: {message}", 0.02)

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
    tasky_response("Let me display your task list!")
    print("{ ~~~ Task List ~~~ }")
    time.sleep(0.5)
    
    line_delay_animation('#' * 21, 0.2)
    for task in to_do_list:
        print(f"* {task}")
        time.sleep(0.3)
    line_delay_animation('#' * 21, 0.2)

# FUNCTION: Exit the program
def exit_tasky():
    tasky_response("See you next time!")
    time.sleep(1)

# FUNCTION: Process user's command using Natural Language Processing(NLP)
def process_command(user_command):
    doc = nlp(user_command)

    # Add task to the list
    if any(token.lemma_ == "add" for token in doc):
        found_verb = False
        for i, token in enumerate(doc):
            if token.pos_ == "VERB": # If verb is found
                found_verb = True
                for j, token in enumerate(doc[i+1:]):
                    if token.pos_ == "VERB": # If second verb is found
                        task_to_add = [word.text for word in doc[i+1:]]
                        task_str = ' '.join(task_to_add).strip().lower()  # join into one string and normalize case
                        if task_str in (task.lower() for task in to_do_list):
                            tasky_response("That task is already in your list!")
                        else:
                            add_to_list(task_str)
                            break

        # ERROR: Input task does not contain a verb
        if not found_verb: 
            tasky_response("I'm sorry, but that's not a valid task...")

    # Remove task from the list
    elif any(token.lemma_ == "remove" for token in doc):
        found_verb = False
        for i, token in enumerate(doc):
            if token.pos_ == "VERB": # If verb is found
                found_verb = True
                for j, token in enumerate(doc[i+1:]):
                    if token.pos_ == "VERB": # If second verb is found
                        task_to_remove = [word.text for word in doc[i+1:]]
                        task_str = ' '.join(task_to_remove).strip().lower()

                        if task_str not in (task.lower() for task in to_do_list):
                            tasky_response("That task does not exist...")
                        else:
                            remove_from_list(task_str)
                        break
                break

        # ERROR: Task does not exist in the list
        if not found_verb:
            tasky_response("I'm sorry, but that task does not exist...")

    # Display task list
    elif any("display" or "show" in token.lemma_ for token in doc):
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
    character_delay_animation('#' * 35, 0.02)
    
    # Display Tasky's message
    tasky_response("What would you like to do?")

    while True:
        # Prompt user to enter a task
        user_command = input("  [You]: ").strip().lower()

        # Process user's command
        process_command(user_command)

display_interface() # Start program
