# Import random

# Functions go here
def check_rounds():
    valid = False
    while not valid:
        response = input("How many rounds: ")

        round_error = "please type either <enter> " \
                      "or an integer that is more than 0\n"
        # If infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to
                # start of loop
                if response < 1:
                    print(round_error)
                    continue

                    # If response is not an integer, go back to
                    # start of loop

            except ValueError:
                print(round_error)
                continue

        return response


def choice_checker(question):
    error = "Please choose from rock / paper /" \
            "scissors (or xxx to quit)"

    valid = False
    while not valid:
        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        if response == "r" or response == "rock":
            return "rock"
        elif response == "p" or response == "paper":
            return "paper"
        elif response == "s" or response == "scissors":
            return "scissors"

        # check for exit code..
        elif response == "xxx":
            return response
        else:
            print(error)


# Main routine goes here

# Lists of vaild responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before.
# If 'yes', show instructions


# Ask user for # of rounds then loop...
rounds_played = 0
choose_instructions = "please choose rock (r), paper (p) or scissors (s)"

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of game game play loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: " \
                  "Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of " \
                  "{}".format(rounds_played + 1, rounds)

    print(heading)

    # Ask user for choice and check it's valid
    choose = choice_checker("choose rock / paper / "
                            "scissors (r/p/s): ")

    rounds_played += 1

    # End game if exit code is type
    if choose == "xxx" or rounds_played >= rounds:
        break

    print("you chose {}".format(choose))

print("thanks for playing")
