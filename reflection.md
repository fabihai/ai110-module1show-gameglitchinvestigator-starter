# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  The first time I ran the game, it seemed normal. The UI is clean. However, when I started guessing numbers, it began to give issues. For example, when I guessed 99 it said to "go higher", but when I chose 100, it said to "go lower". In reality, the correct number was 68. A majority of the hints were incorrect. It continued to say "go higher" for every guess until I reached the bound.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| guess of 90 | "Go Lower" hint | "Go Higher" hint | none |
| guess of 0 | "Out of Bounds" error | "Go Lower" hint | none |
| click "New Game" after you win | open a new game | it stays on the same game page | "You already won. Start a new game to play again." |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    - I used Claude for this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    - The AI suggested to fix the message text in `check_guess` because the hints were the opposite of what should have been given to the user. This is one of the bugs that I had initially noticed, and it gave the correct suggestion of switching these outcome labels.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
    - Of the suggestions that the AI gave, none of them seemed to be unreasonable. I clearly outlined the specific bugs that I wanted fixed and it gave solutions specifically to those issues. When I tested against these changes that were added, the game and tests ran successfully.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

  I played the game after applying the fixes and specifically tested for the bugs that I had noticed the first time when playing the game (out of bounds guesses and inverted high/low hints). I noticed that I no longer received incorrect information in the game. Additionally, in the test file, the test cases were successful. For one of the manual tests, the secret was 80. I tried a few guesses under 80, to which it said "go higher", and then a few tests above 80, to which it said "go lower". After I added the correct number, then it changed to show a success message. This showed that the errors that I originally noticed are no longer present. I gave the AI a description of the specific types of bugs I was targetting in the tests and it generated the files to target those bugs.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
