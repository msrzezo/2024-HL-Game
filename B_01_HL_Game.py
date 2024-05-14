import math
import random


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


# checks for an integer with optional upper /
# lower limits and an optional exit code for infinite mode
# / quitting the game
def int_check(question, low=None, high=None, exit_code=None):
    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter a integer"

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")

    # if the number needs to between low & high
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            if low is not None and response < low:
                print(error)

                # check response is more than the low number
            elif high is not None and response > high:
                print(error)
                # if response is valid, return it
            else:
                return response

        except ValueError:
            print(error)


# Calculate the maximum number of guesses
def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


# Main Routine starts here

# Initialise game variables
mode = "regular"
rounds_played = 0

game_history = []
all_scores = []

print("🔼🔼🔼 Welcome to the Higher Lower Game 🔻🔻🔻")
print()

want_instructions = yes_no("Do you want to read the instructions? ")

# checks user enters yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode:  ",
                       low=1, exit_code="")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

# Get Game parameters
low_num = int_check("Low Number? ")
high_num = int_check("High Number?", low=1)
guesses_allowed = calc_guesses(low_num, high_num)

feedback = ""

end_game = "no"

# Game loop starts here

while rounds_played < num_rounds:

    # check that game has not ended!
    if end_game == "yes":
        break

    # set guesses used to zero at the start of each round
    guesses_used = 0
    already_guessed = []

    secret = random.randint(low_num, high_num)

    # Rounds heading
    if mode == "infinite":
        rounds_heading = f"\n⭕⭕⭕ Round {rounds_played + 1} (infinite mode) ⭕⭕⭕"
    else:
        rounds_heading = f"\n 💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    guess = ""

    # start of guessing loop
    while guess != secret and guesses_used < guesses_allowed:

        # get user choice
        guess = int_check("Guess: ", low_num, high_num, "xxx")

        # check that they don't want to quit
        if guess == "xxx":
            end_game = "yes"
            break

        # check that guess is not a duplicate
        if guess in already_guessed:
            print(f"You've already guesses {guess}. You've used "
                  f"{guesses_used} / {guesses_allowed} guesses ")
            continue

        # if guess is not a duplicate, add it to the 'already guessed' list
        else:
            already_guessed.append(guess)

        guesses_used += 1

        if guess < secret and guesses_used <= guesses_allowed:
            feedback = f"Too low, try a higher number 🔼🔼" \
                       f" you've used {guesses_used} / {guesses_allowed}"

        elif guess > secret and guesses_used < guesses_allowed:
            feedback = f"Too high, try a lower number 🔻🔻 " \
                       f"you've used {guesses_used} / {guesses_allowed}"
        elif guess > secret and guesses_used == guesses_allowed:
            feedback = f"Too high," \
                       f" you've used {guesses_used} / {guesses_allowed}"
        elif guess == secret and guesses_used == 1:
            feedback = "🍀🍀 Lucky! you got it on your first try! 🍀🍀"
        else:
            feedback = f"😊✅Yay! you've guessed the right number in {guesses_used} guesses 😊✅"

        print(feedback)

        if guesses_allowed == guesses_used and guess != secret:
            print()
            print(f"❌😢You lost, The secret number was {secret},"
                  f" better luck next time! ❌😢 ")

    # end of guessing loop - update rounds played
    rounds_played += 1

    # add score to all scores unless user has typed exit code
    if guess!= "xxx":
        all_scores.append(guesses_used)
        history_item = f"Round {rounds_played}: {feedback}"
        game_history.append(history_item)

    # if user are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1
    # Game  loop ends here

print("all scores list: ", all_scores)

if rounds_played > 0:
    all_scores.sort()
    best_score = all_scores[0]
    worst_score = all_scores[-1]
    average_score = sum(all_scores) / len(all_scores)

    # Output Game statistics
    print()
    print("📊📊📊 Game statistics 📊📊📊")
    print(f" Best {best_score:.2f} \t "
          f" Worst {worst_score:.2f} \t "
          f" average {average_score:.2f} \t ")

print()
show_history = yes_no("Do you want to see the game history?")
if show_history == "yes":
    print("\n ⌛⌛⌛ Game History⌛⌛⌛")

    for item in game_history:
        print(item)

    print()
    print("Thanks for playing.")
