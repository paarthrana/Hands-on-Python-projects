
# 🎯 Project 02: Number Guessing Game

A command-line number guessing game built using Python. The computer generates a random number between 1 and 100, and the player must guess it within a limited number of attempts.

## ✨ Features

- Random number generation (1–100).
- Three difficulty levels:
  - Easy: 10 attempts
  - Medium: 7 attempts
  - Hard: 5 attempts
- Hints for guesses that are too high or too low.
- Input validation and error handling.
- Attempt counter.
- Replay functionality.
- Game-over message when attempts run out.

## 🛠️ Concepts Practiced

- Functions and modular programming
- Python Random Module
- `random.randint()`
- Conditional Statements (`if`, `elif`, `else`)
- While Loops
- Boolean Variables
- Break and Continue
- Exception Handling (`try-except`)
- String Methods (`lower()`, `strip()`)
- Main Guard (`if __name__ == "__main__"`)

## 📁 Project Structure

```text
02-number-guessing-game/
│
├── number_guessing.py
└── README.md
```

## ▶️ How to Run

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/hands-on-python-projects.git
```

**2. Navigate to the project directory**

```bash
cd hands-on-python-projects/02-number-guessing-game
```

**3. Run the program**

```bash
python number_guessing.py
```

## 💻 Sample Output

```text
===== NUMBER GUESSING GAME =====

I'm thinking of a number between 1 and 100.

Select Difficulty:
1. Easy (10 attempts)
2. Medium (7 attempts)
3. Hard (5 attempts)

Enter choice (1/2/3): 2

You have 7 attempts. Good luck!

Enter your guess: 50
Too low! Try a higher number.

Attempts used: 1/7

Enter your guess: 75
Too high! Try a lower number.

Attempts used: 2/7

Enter your guess: 65

Congratulations! You guessed it: 65
You guessed correctly in 3 attempts!

Do you want to play again? (yes/no): no

Thanks for playing! Goodbye!
```

## 🎓 What I Learned

Through this project, I practiced creating reusable functions, generating random numbers, implementing game logic, managing attempts, validating user input, and controlling program execution using loops.

I also explored modular programming and the Python main guard.

## 🚀 Future Improvements

- Add a leaderboard.
- Store high scores using file handling.
- Add a timer to track guessing speed.
- Display hints based on the distance from the target number.

---

**Project Status:** Completed ✅

**Version:** 2.0

**Part of:** Hands-On Python Projects 🐍