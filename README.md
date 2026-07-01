# 🎯 Number Guessing Game

A simple command-line **Number Guessing Game** built in Python. The program randomly picks a number between 1 and 100, and the player has to guess it within a limited number of turns based on the difficulty level chosen.

## 📌 Features

- Random number generation between **1 and 100**
- Two difficulty levels:
  - **Easy** → 10 attempts
  - **Hard** → 5 attempts
- Hints after every guess (**too high** / **too low**)
- Turn counter that decreases with every wrong guess
- Clean modular code using functions (`check_answer`, `set_difficulty`, `game`)
- ASCII art welcome banner (via `art` module)

## 🛠️ Tech Stack

- **Language:** Python 3
- **Modules used:** `random`, `art`

## 📂 Project Structure

```
number-guessing-game-python/
│
├── main.py          # Main game logic
├── art.py          # ascii art logo's
└── README.md         # Project documentation
```

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/NinjaVinja/number-guessing-game-python.git
   ```
2. Navigate into the project folder:
   ```bash
   cd number-guessing-game-python
   ```
3. Install the required module:
   ```bash
   pip install art
   ```
4. Run the game:
   ```bash
   python main.py
   ```

## 🎮 How to Play

1. Run the program.
2. Choose a difficulty level — `easy` or `hard`.
3. The game picks a random number between 1 and 100.
4. Enter your guess when prompted.
5. The game will tell you if your guess is **too high** or **too low**.
6. Keep guessing until you find the correct number or run out of attempts!

## 📸 Sample Output

```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts left to guess the number.
Make a guess: 50
Guess is too high.
guess again.
You have 9 attempts left to guess the number.
Make a guess: 25
Guess is too low.
guess again.
...
You guessed the correct number. The answer is 34
```

## 🚀 Future Improvements

- Add input validation (handle non-numeric input gracefully)
- Add a replay option after the game ends
- Track and display best score / fewest attempts
- Add a GUI version using Tkinter or a web version using Flask

## 👤 Author

**Muhammad Taha Ahmad**
- GitHub: [@NinjaVinja](https://github.com/NinjaVinja)
- LinkedIn: [Muhammad Taha Ahmad](https://www.linkedin.com/in/muhammad-taha-ahmad-391679262/)

## 📄 License

This project is open source and free to use for learning purposes.
