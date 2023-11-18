from decouple import config
from casino_logic import play_game

def main():
    my_money = int(config("MY_MONEY", default=1000))
    while True:
        print(f"Your current balance: ${my_money}")
        bet_amount = int(input("Place your bet: $"))
        selected_slot = int(input("Select a slot number (1-30): "))
        
        if my_money < bet_amount:
            print("Not enough money to place this bet. Please try again.")
            continue
        
        result, winning_slot = play_game(bet_amount, selected_slot)
        my_money += result
        
        if result > 0:
            print(f"Congratulations! You won ${result}. The winning slot was {winning_slot}.")
        else:
            print(f"Sorry, you lost ${bet_amount}. The winning slot was {winning_slot}.")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"Game Over. Your final balance: ${my_money}")
            break

if __name__ == "__main__":
    main()
