import random
import sys
import time

print('Welcome to rock paper scissors')

moves: dict = {'rock':'🪨', 'paper':'📃', 'scissor':'✂️'}

valid_moves: list[str] = list(moves.keys())

user_wins: int = 0
computer_wins: int = 0
moves_tied: int = 0

# Start of game
while True:
    user_move:str = input('Please enter your move: Rock, Paper, Scissor: ').lower()
    if user_move == 'exit':
        print('Thank you for playing')
        print('--------------------------------')
        print(f'You won {user_wins} times')
        print(f'Computer won {computer_wins} times')
        print(f'Number of ties {moves_tied} times')
        sys.exit()

    if user_move not in valid_moves:
        print('Please enter a valid move')
        continue
    AI_play: dict = random.choice(valid_moves)

# Moves played
    print(f'You: {moves[user_move]}')
    print(f'AI: {moves[AI_play]}')


    if user_move == AI_play:
        print('It is a tie!🪢🪢🪢🪢')
        moves_tied += 1
    elif user_move == 'rock' and AI_play == 'scissor':
        print('You win :) ✅✅✅✅')
        user_wins += 1
    elif user_move == 'paper' and AI_play == 'rock':
        print('You win :) ✅✅✅✅')
        user_wins += 1
    elif user_move == 'scissor' and AI_play == 'paper':
        print('You win :) ✅✅✅✅')
        user_wins += 1
    else:
        print('You lose :( ❌❌❌❌')
        computer_wins += 1

