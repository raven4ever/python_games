import string
import random


def generate_password(no_chars: int, special_chars: bool) -> str:
    all_chars = string.ascii_letters + string.digits

    if special_chars:
        all_chars += string.punctuation

    return ''.join(random.sample(all_chars, no_chars))


def str2bool(v):
    return v.lower() in ("yes", "y")


def main():
    print('Let\'s get you a secure password!')

    try:
        no_chars = int(input('Insert the number of characters for your password:'))
        special_chars = input('Should it contain special characters?(Y/N)').lower()
    except ValueError:
        print("This is not a valid number.")

    print(f'Your new password is: {generate_password(no_chars, str2bool(special_chars))}')


if __name__ == '__main__':
    main()
