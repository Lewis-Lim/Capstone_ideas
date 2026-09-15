# Simple Board Game First-Player & Turn-Order Spinner

import random
import time


def get_players():
    """Get player names from user input."""
    print("🎲 BOARD GAME TURN GENERATOR 🎲\n")
    while True:
        names_input = input(
            "Enter player names separated by commas (e.g., Alice, Bob, Charlie):\n"
        )
        players = [name.strip() for name in names_input.split(",") if name.strip()]

        if len(players) >= 2:
            return players
        print("❌ Please enter at least 2 players!\n")


def pick_first_player(players):
    """Simulate a dramatic random pick for who goes first."""
    print("\nChoosing who goes first...")

    # Fun dramatic suspense loop
    for i in range(3, 0, -1):
        print(f"Rolling the dice... {i}")
        time.sleep(0.6)

    first_player = random.choice(players)
    print(f"\n🎉 **{first_player}** goes first! 🎉\n")
    return first_player


def randomize_turn_order(players):
    """Randomize and display the full turn order."""
    shuffled_players = players.copy()
    random.shuffle(shuffled_players)

    print("--- 🔄 TURN ORDER ---")
    for rank, name in enumerate(shuffled_players, start=1):
        print(f"  {rank}. {name}")
    print("---------------------\n")


def main():
    players = get_players()

    while True:
        print("\nWhat would you like to do?")
        print("1. Pick First Player Only")
        print("2. Shuffle Full Turn Order")
        print("3. Enter New Players")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            pick_first_player(players)
        elif choice == "2":
            randomize_turn_order(players)
        elif choice == "3":
            players = get_players()
        elif choice == "4":
            print("\nHave a great game night! Goodbye! 👋")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()