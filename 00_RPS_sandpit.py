# Funtions go here


# Main routine goes here

# Ask user for choice and check it's vaild

def choice_checker(question):
    # Print out choice for comparison
    error = "please choose from rock / paper /" \
            "scissors (or xxx to quit)"

    response = input(question).lower()

    if response == "r" or response == "rock":
        return response
    elif response == "p" or response == "paper":
        return response
    elif response == "s" or response == "scissors":
        return response


user_choice = choice_checker("Choose rock / paper / scissors")