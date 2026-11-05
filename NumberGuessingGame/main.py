import random


def choose_difficulty():
    print("\nSelect Difficulty:")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")

    while True:
        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            return 10
        elif choice == '2':
            return 7
        elif choice == '3':
            return 5
        else:
            print("Invalid choice! Select 1, 2, or 3.")


def play_game():
    print("\n===== NUMBER GUESSING GAME =====")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        max_attempts = choose_difficulty()
        number_to_guess = random.randint(1, 100)
        attempts = 0
        guessed_correctly = False

        print(f"\nYou have {max_attempts} attempts. Good luck!")

        while attempts < max_attempts:
            try:
                guess = int(input("\nEnter your guess: "))

                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue

            except ValueError:
                print("Invalid input! Please enter a whole number.")
                continue

            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try a higher number.")

            elif guess > number_to_guess:
                print("Too high! Try a lower number.")

            else:
                guessed_correctly = True
                print(f"\nCongratulations! You guessed it: {number_to_guess}")
                print(f"You guessed correctly in {attempts} attempts!")
                break

            print(f"Attempts used: {attempts}/{max_attempts}")

        if not guessed_correctly:
            print("\nGame Over!")
            print(f"The correct number was {number_to_guess}.")
            print(f"You used all {max_attempts} attempts.")

        while True:
            replay = input("\nDo you want to play again? (yes/no): ").lower().strip()

            if replay == 'yes':
                break
            elif replay == 'no':
                print("Thanks for playing! Goodbye!")
                return
            else:
                print("Please enter yes or no.")


if __name__ == "__main__":
    play_game()