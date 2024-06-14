**Guess My Number Game**


*Description*

This is a simple number guessing game written in Python. The game randomly selects a number between 1 and 100, and the player has to guess the number within a limited number of attempts. After each guess, the game provides feedback on whether the guess was too high, too low, or correct. If the player guesses the correct number, they win the game. If they use up all their guesses, they lose. The game also provides hints if the guess is close to the actual number and saves the player's guesses to a file.


*How to Run*

1. Ensure you have Python installed on your computer.
2. Save the script to a file, for example, `guess_my_number.py`.
4. Run the script using the command: `python guess_my_number.py`


*How to Play*

1. The game will display a greeting message from the greetings.txt file.
2. You will be prompted to guess a number between 1 and 100.
3. Enter your guess and press Enter.
4. The game will provide feedback on your guess:
    If your guess is too high, it will say "Your guess was too high."
    If your guess is too low, it will say "Your guess was too low."
    If your guess is close to the correct number (within 5 numbers), it will provide a hint once.
5. You have a maximum of 5 guesses to find the correct number.
6. If you guess the correct number within the allowed attempts, you win.
7. If you use up all your guesses without finding the correct number, you lose, and the game reveals the correct number.
8. After each game, you will be asked if you want to play again. Enter 'yes' or 'no'.
9. The game saves all your guesses to a file named `guesses.txt`.


*Files*
    
- `guess_my_number.py`: The main game script.
- `greetings.txt`: A text file containing a greeting message that is displayed at the start of the game.
- `guesses.txt`: A text file where the player's guesses are stored after each game.


*Code Overview*

- `guess_my_number()`: The main function that runs the game logic.
    - Picks a random number between 1 and 100.
    - Reads and prints a greeting message from `greetings.txt`.
    - Prompts the player for their guesses and provides feedback.
    - Keeps track of the number of guesses and provides hints if the guess is close.
    - Saves the player's guesses to `guesses.txt` and prints them at the end of the game.
- The game loop:
    - Continuously runs the game until the player decides to stop.
    - Prompts the player to play again and handles their response.
 

*Example Usage*

`python guess_my_number.py`

When prompted, enter your guesses and follow the feedback. After the game ends, decide if you want to play again by entering 'yes' or 'no'.


*Note*

Ensure that the `greetings.txt` file is in the same directory as the script and contains a welcome message. The `guesses.txt` file will be created by the script to store your guesses.
