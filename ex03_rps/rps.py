from random import randrange


MOVES = ['Rock', 'Paper', 'Scissors']


def get_random_move():
    rand_index = randrange(len(MOVES))
    return MOVES[rand_index]


def generate_moves_str():
    moves_str = str()
    for i, move in enumerate(MOVES):
        moves_str += f' [{i}] {move} \n'
    return moves_str


def winning_shot(player1, player2):
    winner = None
    p1_name, p1_move = player1.values()
    p2_name, p2_move = player2.values()

    if p1_move == 'Rock':
        if p2_move == 'Paper':
            winner = p2_name
        elif p2_move == 'Scissors':
            winner = p1_name
    elif p1_move =='Paper':
        if p2_move == 'Rock':
            winner = p1_name
        elif p2_move == 'Scissors':
            winner = p2_name
    elif p1_move == 'Scissors':
        if p2_move == 'Rock':
            winner = p2_name
        elif p2_move == 'Paper':
            winner = p1_name

    return winner


scores = {'user': 0, 'computer': 0}
loops = 0
while True:
    print(f'------------ Turn {loops} \n')
    moves_str = generate_moves_str()
    user_move_nb = int(input(f'Choose a move by number : \n{moves_str} '))

    computer = {
        'name': 'computer',
        'move': get_random_move(),
    }
    user = {
        'name': 'user',
        'move': MOVES[user_move_nb]
    }

    print(f'You: {user["move"]}. Computer : {computer["move"]}')
    winner = winning_shot(user, computer)
    if winner is not None:
        print(f'{winner} wins.')
        scores[winner] += 1
    loops += 1

    if loops >= 3:
        if scores['user'] > scores['computer']:
            print('You win the game !')
            exit(0)
        elif scores['computer'] > scores['user']:
            print('You lost the game...')
            exit(0)
        else:
            print('Equality: another turn')
