import random

nb_range = 20
rand_nb = random.randrange(20)

found = False
while not found:
    user_guess = input(f'Guess the number between 0 and {nb_range} : ')

    try:
        user_nb = int(user_guess)
        if not 0 < user_nb < nb_range:
            raise
    except Exception as e:
        print(f'Value provided by user is not valid: {e}')
        continue

    if user_nb == rand_nb:
        print(f'You found the right number: {rand_nb}')
        found = True
    elif user_nb < rand_nb:
        print('The random number is higher')
    elif user_nb > rand_nb:
        print('The random number is lower')
