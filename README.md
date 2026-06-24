# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
      This is a guessing game where the user must enter guesses to find a correct number within a certain range.
- [ ] Detail which bugs you found.
      While initially playing this game, I noticed that the hints given to the user were incorrect. For example, if the correct number is 50 and the user guesses 40, then the game will incorrectly give a hint of "Too High". Another hint that I had found was that the game could not detect when the user guessed a number that was outside of the bounds to be guessed in.
- [ ] Explain what fixes you applied.
      To fix the first issue, I switched the "Too High"/"Too Low" hints in the code to correctly output based on when a user enters a guess that is too high/low. I added a check for if the user enters guesses that are out of bounds. Finally, I refactored the code so that the core logic was separate from the front facing code.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 90
2. Game returns "Too High"
3. User enters a guess of 67 --> "Too Low"
4. User enters a guess of 105 --> "Out of Bounds"
5. Scores updates correctly after each guess
6. Game ends after the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
