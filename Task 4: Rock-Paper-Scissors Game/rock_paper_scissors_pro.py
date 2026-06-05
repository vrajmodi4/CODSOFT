
# Rock Paper Scissors Pro (Starter Edition)
# Features: Tkinter GUI, Best of 3, Difficulty Levels, SQLite, Statistics

import tkinter as tk
from tkinter import ttk, messagebox
import random
import sqlite3
from datetime import datetime

conn = sqlite3.connect("rps.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS history(
id INTEGER PRIMARY KEY AUTOINCREMENT,
date TEXT,
winner TEXT,
user_score INTEGER,
computer_score INTEGER
)
""")
conn.commit()

user_score = 0
computer_score = 0
wins = losses = draws = 0

def save_match(winner):
    cur.execute(
        "INSERT INTO history(date,winner,user_score,computer_score) VALUES(?,?,?,?)",
        (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), winner, user_score, computer_score)
    )
    conn.commit()

def computer_move(user_choice):
    level = difficulty.get()
    choices = ["Rock","Paper","Scissors"]

    if level == "Easy":
        return random.choice(choices)

    if level == "Medium":
        if random.randint(1,100) <= 70:
            return random.choice(choices)

    counters = {"Rock":"Paper","Paper":"Scissors","Scissors":"Rock"}
    return counters[user_choice]

def play(choice):
    global user_score, computer_score, wins, losses, draws

    if user_score == 2 or computer_score == 2:
        return

    comp = computer_move(choice)

    if choice == comp:
        result = "Draw"
        draws += 1
    elif (
        (choice=="Rock" and comp=="Scissors") or
        (choice=="Paper" and comp=="Rock") or
        (choice=="Scissors" and comp=="Paper")
    ):
        result = "You Win"
        user_score += 1
        wins += 1
    else:
        result = "Computer Wins"
        computer_score += 1
        losses += 1

    result_label.config(text=f"You: {choice} | Computer: {comp}\n{result}")
    score_label.config(text=f"Player: {user_score}   Computer: {computer_score}")

    history.insert(tk.END, f"{choice} vs {comp} -> {result}")
    update_stats()

    if user_score == 2:
        save_match("User")
        messagebox.showinfo("Winner", "You won the Best of 3 Match!")
    elif computer_score == 2:
        save_match("Computer")
        messagebox.showinfo("Winner", "Computer won the Best of 3 Match!")

def update_stats():
    total = wins + losses + draws
    win_rate = (wins/total*100) if total else 0
    stats.config(
        text=f"Games:{total}  Wins:{wins}  Losses:{losses}  Draws:{draws}  Win Rate:{win_rate:.1f}%"
    )

def reset_game():
    global user_score, computer_score
    user_score = computer_score = 0
    score_label.config(text="Player: 0   Computer: 0")
    result_label.config(text="Choose your move")
    history.delete(0, tk.END)

def view_db():
    rows = cur.execute("SELECT * FROM history ORDER BY id DESC").fetchall()
    win = tk.Toplevel(root)
    win.title("Match History")
    txt = tk.Text(win, width=70, height=15)
    txt.pack()
    for row in rows:
        txt.insert(tk.END, str(row) + "\n")

root = tk.Tk()
root.title("Rock Paper Scissors Pro")
root.geometry("700x550")
root.configure(bg="#1e1e1e")

tk.Label(root,text="ROCK PAPER SCISSORS PRO",
         bg="#1e1e1e",fg="white",
         font=("Segoe UI",18,"bold")).pack(pady=10)

difficulty = tk.StringVar(value="Easy")
ttk.Combobox(root,textvariable=difficulty,
             values=["Easy","Medium","Hard"],
             state="readonly").pack()

score_label = tk.Label(root,text="Player: 0   Computer: 0",
                       bg="#1e1e1e",fg="white",font=("Arial",14))
score_label.pack(pady=10)

btn_frame = tk.Frame(root,bg="#1e1e1e")
btn_frame.pack()

for item in ["Rock","Paper","Scissors"]:
    tk.Button(btn_frame,text=item,width=12,
              command=lambda x=item: play(x)).pack(side=tk.LEFT,padx=10)

result_label = tk.Label(root,text="Choose your move",
                        bg="#1e1e1e",fg="cyan",font=("Arial",12))
result_label.pack(pady=15)

stats = tk.Label(root,text="Games:0 Wins:0 Losses:0 Draws:0 Win Rate:0%",
                 bg="#1e1e1e",fg="lightgreen")
stats.pack()

tk.Label(root,text="Round History",
         bg="#1e1e1e",fg="white").pack(pady=5)

history = tk.Listbox(root,width=70,height=10)
history.pack()

bottom = tk.Frame(root,bg="#1e1e1e")
bottom.pack(pady=10)

tk.Button(bottom,text="Reset Match",command=reset_game).pack(side=tk.LEFT,padx=5)
tk.Button(bottom,text="View Database History",command=view_db).pack(side=tk.LEFT,padx=5)

root.mainloop()
