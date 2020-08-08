import random

GAME_OPTIONS = ['r', 'p', 's']


def generate_random_choice() -> str:
    return random.choice(GAME_OPTIONS)


# Returns:
#  - 0 for user win
#  - 1 for user loss
#  - 2 for draw
def decide_winner(user_choice: str, comp_choice: str) -> int:
    if user_choice == comp_choice:
        return 2

    if (user_choice == 's' and comp_choice == 'p') or \
            (user_choice == 'p' and comp_choice == 'r') or \
            (user_choice == 'r' and comp_choice == 's'):
        return 0

    return 1


# Prints a scoreboard based on the wins & losses parameters
def print_score(wins: int, losses: int, draws: int):
    print('****SCORE****')
    print(f'WINS: {wins}')
    print(f'LOSSES: {losses}')
    print(f'DRAWS: {draws}')
    print('*************')


def main():
    print('Let\'s play a game!!')
    wins = 0
    losses = 0
    draws = 0

    while True:
        user_choice = input('Your choice is (r,p,s):')
        comp_choice = generate_random_choice()

        if user_choice in GAME_OPTIONS:
            print(f'An epic battle between your {user_choice} and {comp_choice}')

            status = decide_winner(user_choice, comp_choice)
            if status == 0:
                print('HOORAY, YOU WIN!')
                wins = wins + 1
            elif status == 1:
                print('Maybe some other time.')
                losses = losses + 1
            elif status == 2:
                print('That would be a draw.')
                draws = draws + 1
        else:
            print('Please choose a suitable option!')

        print_score(wins, losses, draws)

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
