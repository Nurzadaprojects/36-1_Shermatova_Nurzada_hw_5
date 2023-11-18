import random

def play_game(bet_amount, selected_slot):
    winning_slot = random.randint(1, 30)
    if selected_slot == winning_slot:
        return bet_amount * 2, winning_slot
    else:
        return -bet_amount, winning_slot
