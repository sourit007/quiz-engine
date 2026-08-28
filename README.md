# 🎮 Terminal-Based KBC Quiz Engine

A command-line trivia game inspired by the popular television show **Kaun Banega Crorepati (KBC)**. Test your general knowledge, answer progressively harder questions, and see how much virtual prize money you can win!

---

## 📝 Project Description

This project is a lightweight, interactive quiz engine that runs entirely in the terminal. It simulates the hot-seat experience by presenting the user with multiple-choice questions, accepting their input, and calculating their total prize money based on correct answers. 

It was built to demonstrate fundamental programming concepts, specifically data structures and control flow.

---

## ⚙️ Technical Implementation

At the core of this quiz engine are three essential programming concepts that work together to drive the game's logic:

### 1. Lists (Data Storage)
We use **Lists** to store the game's data. This includes:
*   A list of nested elements (or dictionaries) containing the questions, four multiple-choice options, and the correct answer.

### 2. For Loops (Game Progression)
A **`for` loop** is used to iterate through the list of questions. Instead of writing repetitive code for each question, the loop seamlessly pulls the next question, displays the options, and pauses for the user's answer before moving on to the next round.

### 3. If-Else Statements (Answer Validation)
**`if-else` conditionals** handle the core game mechanics and validation. 
*   **`if`** the user's input matches the correct answer, the program prints a congratulatory message, updates their current prize money, and allows the loop to continue.
*   **`else`**, the game immediately ends, printing a "Game Over" message along with the total amount of money the player takes home.

---

## 🚀 How to Run

1. Ensure you have Python (or your respective programming language compiler) installed on your system.
2. Clone this repository or download the source code file.
3. Open your terminal or command prompt.
4. Navigate to the directory where the file is saved.
5. Run the script:
   ```bash
   KBC.py
