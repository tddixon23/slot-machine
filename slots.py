import random

def roulette():
    number = random.randint(0, 36)  # Simulating roulette wheel spin
    return number

def place_bet(bet_type, bet_value):
    spin_result = roulette()
    print(f"The ball landed on {spin_result}")
    if bet_type == "number" and bet_value == spin_result:
        return "You win 35x your bet!"
    # Add other bet types here like color, odd/even, etc.
    else:
        return "You lose."

# Example interaction:
bet_type = input("Bet on a number, odd/even, or color: ")
bet_value = int(input("Enter the number you want to bet on: "))
print(place_bet(bet_type, bet_value))
