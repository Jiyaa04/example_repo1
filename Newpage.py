import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

#Creating fuction to count scores
def game(players):
    max_score = 50
    score = [0 for _ in range(players)]
    current = 0
    
    while max(score) < max_score:
        print(f"\nPlayer {current + 1}'s turn.")
        turn_total = 0
        
        while True:
            roll_value = roll()
            print(f"Player {current + 1} rolled: {roll_value}")
            
            if roll_value == 1:
                print(f"Player {current + 1} loses turn! No points added.")
                turn_total = 0
                break
            else:
                turn_total += roll_value
                print(f"Turn total: {turn_total}")
                
                # Ask player if they want to hold or roll again
                choice = input("Hold or Roll again? (h/r): ").lower()
                if choice == 'h':
                    score[current] += turn_total
                    break

        print(f"Player {current + 1} total score: {score[current]}")
        
        if score[current] >= max_score:
            print(f"\nPlayer {current + 1} wins with a score of {score[current]}!")
            break
        
        # Move to the next player
        current = (current + 1) % players

# Loop to get the valid number of players
while True:
    players = input("Enter number of players (1-4): ")
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break
        else:
            print("Please enter a number between 1 and 4.")
    else:
        print("Invalid input. Please enter a number.")

print(f"Number of players: {players}")

# Starting with the game
game(players)
