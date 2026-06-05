# Rock Paper Scissors Pro

## Overview

Rock Paper Scissors Pro is a desktop-based game developed using Python and Tkinter. The game allows users to play Rock-Paper-Scissors against the computer with multiple difficulty levels, match history storage, and real-time statistics tracking.

This project was developed as part of the CodSoft Python Programming Internship to demonstrate GUI development, database management, and game logic implementation using Python.

---

## Features

### Dark-Themed GUI

* Modern graphical user interface built using Tkinter.
* User-friendly and interactive design.

### Difficulty Levels

* Easy Mode: Computer selects moves randomly.
* Medium Mode: 70% random moves and 30% strategic moves.
* Hard Mode: Computer always selects the counter move.

### Best-of-3 Match System

* First player to win 2 rounds wins the match.
* Automatic winner announcement.

### Statistics Dashboard

Tracks:

* Total Games Played
* Wins
* Losses
* Draws
* Win Rate Percentage

### Match History

* Stores completed match results in an SQLite database.
* Displays previous match records through a dedicated history window.

### Reset Match

* Reset scores and round history instantly.

---

## Technologies Used

* Python 3
* Tkinter
* SQLite3
* Random Module
* Datetime Module

---

## Project Structure

```text
RockPaperScissorsPro/
│
├── rock_paper_scissors_pro.py
├── rps.db
└── README.md
```

---

## Database Schema

### Table: history

| Column         | Type    |
| -------------- | ------- |
| id             | INTEGER |
| date           | TEXT    |
| winner         | TEXT    |
| user_score     | INTEGER |
| computer_score | INTEGER |

---

## How to Run

### Step 1: Install Python

Download Python from:

https://www.python.org/downloads/

### Step 2: Run the Program

Open Command Prompt or Terminal:

```bash
python rock_paper_scissors_pro.py
```

---

## How to Play

1. Select a difficulty level.
2. Click Rock, Paper, or Scissors.
3. The computer generates its move.
4. Scores are updated automatically.
5. First player to reach 2 points wins the match.
6. View previous matches using the "View Database History" button.

---

## Sample Features Demonstrated

* GUI Development using Tkinter
* Event Handling
* SQLite Database Integration
* Statistics Calculation
* Game Logic Design
* Best-of-3 Tournament System

---

## Future Enhancements

* Sound Effects
* Trophy Animation
* Multiplayer Mode
* Export Match History to CSV
* Player Name Customization
* Theme Switching

---

## Conclusion

Rock Paper Scissors Pro is an interactive Python desktop application that combines game logic, GUI design, and database management into a single project. The application provides a fun and engaging user experience while demonstrating important Python programming concepts and software development practices.
