import random


# define a function to run the game
def guess_my_number():

    # pick a random number between 1 and 100 and store in a variable
    random_number = random.randint(1, 100)

    # initialize some variables
    guess_count = 0
    max_guesses = 5
    hint = 0
    guesses = []  # List to store the guesses

    # clear previously stored guesses
    open("guesses.txt", "w").close()

    # read and print the text from a text file
    with open('greetings.txt', 'r') as greeting_text:
        print(greeting_text.read())

    # make sure the number of guesses are less than the max number allowed
    while guess_count < max_guesses:

        # check if the user's input is a valid number
        try:
            user_guess = int(input('Enter your guess: '))
        except ValueError:
            print('Please enter a valid number')
            continue

        # Store the guess in the list
        guesses.append(user_guess)

        # increase the number of guesses by 1
        guess_count += 1

        # if the user guessed the correct number let them know they won by printing
        if user_guess == random_number:
            print(f'You got it! The number was {random_number}')
            break

        # if the user's guess is greater than the random number let them know their guess was too high
        elif user_guess > random_number:

            # if the user's guess is within 5 numbers let them know their close
            if user_guess - random_number < 5 and hint == 0:
                print(f'You are close! The number is between {user_guess - 5} and {user_guess}')
                # add 1 to the hint so this code will not run again
                hint += 1
            else:
                print('Your guess was too high.')

        # if the user's guess is less than the random number let them know their guess was too low
        elif user_guess < random_number:

            # if the user's guess is within 5 numbers let them know their close
            if random_number - user_guess < 5 and hint == 0:
                print(f'You are close! The number is between {user_guess} and {user_guess + 5}')
                # add 1 to the hint so this code will not run again
                hint += 1
            else:
                print('Your guess was too low.')

        # calculate how many guesses the user have left and store it in a variable
        remaining_guesses = max_guesses - guess_count

        # is the remaining guesses are 1 or more, show the user how many guesses they have left
        if remaining_guesses > 0:
            print(f'You have {remaining_guesses} guesses left.')
        else:
            # else, if the number of remaining guesses is 0, let the user know they're out of guesses
            print(f'Sorry. You are out of guesses. The number was {random_number}')

    # Save the guesses to a file
    with open('guesses.txt', 'a') as guess_storage:
        guess_storage.write('The guesses you made were: ' + ', '.join(map(str, guesses)) + '\n')

    # Print the guesses at the end of the game
    with open('guesses.txt', 'r') as guess_storage:
        print(guess_storage.read())


# while True keeps running this code until it's asked to stop
while True:
    # call the function to run the game
    guess_my_number()
    # ask the user if they want to play again and store their input in a variable
    restart = input('Would you like to play again? (yes/no)').lower()

    # loop until the user provides a valid input
    while restart not in ['yes', 'y', 'no', 'n']:
        # if the user's input is neither 'yes' nor 'no', ask them to enter a valid input
        print('Please enter yes or no.')
        restart = input('Would you like to play again? (yes/no)').lower()

    # based on if they say 'yes' or 'no', continue or break the loop
    if restart in ['yes', 'y']:
        continue
    elif restart in ['no', 'n']:
        break
