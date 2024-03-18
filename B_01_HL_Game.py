# checking user enters yes / no (takes in a question)
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")

    response = input(question).lower()
    # checks user response, question
    # repeats if users don't enter yes / no
    if response == "yes" or response == "y":
        return "yes"
    elif response == "no" or response == "n":
        return "no"
    else:
        print("Please enter yes / no")


def instructions():
    print('''

**** instructions ****

To begin, choose the number of rounds and either customise
the game parameters or go with the default game (where the 
secret number will be between 1 and 100).

Then choose how many rounds you'd like to play <enter> for 
infinite mode.

Your goal is to try to guess the secret number without
running out of guesses 

 Good Luck!

    ''')


# checks that users enters an integer
def int_check(question):
    while True:
        error = "Please enter a integer that is 1 or more"

        to_check = input(question)
        # check for infinite Mode
        if to_check == "":
            return "infinite"
        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


# Main Routine starts here

# Initialise game variables
mode = "regular"
rounds_played = 0

print("🔼🔼🔼 Welcome to the Higher Lower Game 🔻🔻🔻")
print()

want_instructions = yes_no("Do you want to read the instructions? ")

# checks user enters yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5
# Game loop starts here
while rounds_played < num_rounds:

    # Rounds heading
    if mode == "infinite":
        rounds_heading = f"\n⭕⭕⭕ Round {rounds_played + 1} (infinite mode) ⭕⭕⭕"
    else:
        rounds_heading = f"\n 💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    # get user choice
    user_choice = input("Choose: ")

    # if user choice is in the exit code, break the loop
    if user_choice == "xxx":
        break

    rounds_played += 1

    # if user are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here