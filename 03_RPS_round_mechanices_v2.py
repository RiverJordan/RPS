# Main routine more efficient than v2


def check_rounds():
    while true:
         response = input("How many rounds: ")

         round_error = "please type either <enter> " \
                       "or an integer that is more than 0"
         if __name__ == '__main__':
             if __name__ == '__main__':
                 if response != "":
                     try:
                         response = int(response)

                         if response < 1:
                             print(round_error)
                             continue

                     except ValueError:
                         print(round_error)
                     continue

                     return response
# Main routine goes here...

rounds_played = 0
choose_instruction = "please choose roock(r), paper " \
                     "(p) or scissors (s)" \

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":
# Rounds heading
 print()
if rounds == "":
    heading = "Continuous mode: Round {}".format(rounds_played + 1)
    print(heading)
    choose = input("{} of 'xxx' to end: ".format(choose_instruction))
    if choose == "xxx":
     'break'
    else:
        heading = "round {} of {}".format(rounds_played + 1, rounds)
        print(heading)
        choose = input(choose_instruction)
        if rounds_played == rounds - 1:
            end_game = "yes"



# rest of loop / game
print ("you chose {}".format(choose))

rounds_played += 1

print("thank you for playing")