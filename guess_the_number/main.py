import random


# Generates the random number to be guessed during the game
def generate_random_number() -> int:
    return random.randint(0, 20)


# The game function
# Return True if the player has won
def play_game() -> bool:
    correct = generate_random_number()
    tries = 0

    # Debugging purposes
    # print(correct)

    while tries < 3:
        try:
            guess = int(input('Your guess is (0-20):'))

            if guess == correct:
                return True
            else:
                tries = tries + 1
                print('Sorry, try again!')
                status = 'higher' if guess < correct else 'lower'
                print(f'Hint: The correct number is {status} than your guess.')
        except ValueError:
            print("This is not a valid number.")
    return False


# Prints a scoreboard based on the wins & losses parameters
def print_score(wins: int, losses: int):
    print('****SCORE****')
    print(f'WINS: {wins}')
    print(f'LOSSES: {losses}')
    print('*************')


def main():
    print('Let\'s play a game!!')
    wins = 0
    losses = 0

    while True:
        status = play_game()

        if status:
            print('HOORAY, YOU WIN!')
            wins = wins + 1
        else:
            print('Maybe some other time.')
            losses = losses + 1

        print_score(wins, losses)

        ans = input('Should we try another run?[Y/N]')

        if ans == 'y' or ans == 'Y':
            print('Cool!')
        elif ans == 'n' or ans == 'n':
            print('Bye!')
            break
        else:
            print('Kernel Panic!')
            break


if __name__ == '__main__':
    main()
