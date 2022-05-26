# Functions go here
def choice_checker(question, vaild_list, error):

 error = "Please choose from rock / paper /" \
        "scissors (or xxx to quit)"

 Vaild = False
 while not valid:

    # Ask user for choice (and put choice in lowercase)
     response = input(question).lower()

# iterates through list and if response is an item

 # loop for testing purpose
 user_choice = ""
 while user_choice != "xxx":

    if __name__ == '__main__':
        if response == "r" or response == "rock":
            return response
        elif response == "p" or response == "paper":
            return response
        elif response == "s" or response == "scissors":
            return response

       # check for exit code..
        elif response == "xxx":
            return response
        else:
            print(error)
# Main routine goes here

#lists for checking response
rps_list = ["rock", "paper", "scissors", "xxx"]

# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":


    # Ask user for choice and check it's vaild
     user_choice = choice_checker("choose rock / paper / "
                                  "scissors (r/p/s): ", rps_list,
                                  "please choose from rock / "
                                  "paper / scissors "
                                  "(or xxx to quit)")


# print out choice for comparison purposes
print("You chose {}".format(user_choice))
