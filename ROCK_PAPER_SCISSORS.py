#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tkinter as tk
from tkinter import messagebox
import random

# Game variables
user_score = 0
computer_score = 0
round_number = 1
total_rounds = 5

choices = ["rock", "paper", "scissors"]
emoji_map = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

# Game logic
def get_computer_choice():
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or          (user == "scissors" and computer == "paper") or          (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def update_ui(user_choice):
    global user_score, computer_score, round_number

    if round_number > total_rounds:
        return

    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)

    user_label.config(text=f"🧑 You: {emoji_map[user_choice]}")
    computer_label.config(text=f"🤖 Computer: {emoji_map[computer_choice]}")

    if winner == "tie":
        result_label.config(text="It's a Tie! 😐")
    elif winner == "user":
        result_label.config(text="You Win! 🎉")
        user_score += 1
    else:
        result_label.config(text="Computer Wins! 💻")
        computer_score += 1

    score_label.config(text=f"Score → You: {user_score} | Computer: {computer_score}")
    round_label.config(text=f"Round {round_number}/{total_rounds}")
    round_number += 1

    if round_number > total_rounds:
        show_final_winner()

def show_final_winner():
    if user_score > computer_score:
        msg = "🎉 You are the Champion!"
    elif user_score < computer_score:
        msg = "💻 Computer Wins the Game!"
    else:
        msg = "😐 It's a Draw!"

    messagebox.showinfo("Game Over", f"Final Score\nYou: {user_score} | Computer: {computer_score}\n\n{msg}")

def reset_game():
    global user_score, computer_score, round_number
    user_score = 0
    computer_score = 0
    round_number = 1
    result_label.config(text="")
    score_label.config(text="Score → You: 0 | Computer: 0")
    round_label.config(text="Round 1/5")
    user_label.config(text="🧑 You: ")
    computer_label.config(text="🤖 Computer: ")

# GUI Setup
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x500")
root.config(bg="white")

tk.Label(root, text="🎮 Rock-Paper-Scissors", font=("Helvetica", 18, "bold"), bg="white").pack(pady=10)

round_label = tk.Label(root, text="Round 1/5", font=("Helvetica", 12), bg="white")
round_label.pack(pady=5)

frame_choices = tk.Frame(root, bg="white")
frame_choices.pack(pady=10)

tk.Button(frame_choices, text="🪨 Rock", width=10, command=lambda: update_ui("rock")).grid(row=0, column=0, padx=10)
tk.Button(frame_choices, text="📄 Paper", width=10, command=lambda: update_ui("paper")).grid(row=0, column=1, padx=10)
tk.Button(frame_choices, text="✂️ Scissors", width=10, command=lambda: update_ui("scissors")).grid(row=0, column=2, padx=10)

user_label = tk.Label(root, text="🧑 You: ", font=("Helvetica", 14), bg="white")
user_label.pack(pady=10)

computer_label = tk.Label(root, text="🤖 Computer: ", font=("Helvetica", 14), bg="white")
computer_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 16), fg="blue", bg="white")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score → You: 0 | Computer: 0", font=("Helvetica", 12), bg="white")
score_label.pack(pady=10)

tk.Button(root, text="🔁 Play Again", command=reset_game, bg="#f0f0f0").pack(pady=15)

root.mainloop()


# In[9]:


print(_file_)


# In[ ]:




