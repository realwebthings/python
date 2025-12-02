import tkinter as tk
from tkinter import messagebox

# Tic Tac Toe Game
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("400x500")
root.resizable(False, False)

# Game variables
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False
score_x = 0
score_o = 0

# UI Elements
title_label = tk.Label(root, text="Tic Tac Toe", font=("Arial", 24, "bold"), fg="blue")
title_label.pack(pady=10)

player_label = tk.Label(root, text=f"Player {current_player}'s Turn", font=("Arial", 16))
player_label.pack(pady=5)

# Score display
score_frame = tk.Frame(root)
score_frame.pack(pady=5)

score_label = tk.Label(score_frame, text=f"X: {score_x}  |  O: {score_o}", font=("Arial", 14))
score_label.pack()

# Game board
board_frame = tk.Frame(root, bg="black")
board_frame.pack(pady=20)

buttons = []

def button_click(row, col):
    global current_player, game_over
    
    if game_over or board[row][col] != "":
        return
    
    # Make move
    board[row][col] = current_player
    buttons[row][col].config(text=current_player, 
                           fg="red" if current_player == "X" else "blue",
                           font=("Arial", 20, "bold"))
    
    # Check for win
    if check_winner():
        game_over = True
        winner = current_player
        update_score(winner)
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
        return
    
    # Check for tie
    if is_board_full():
        game_over = True
        messagebox.showinfo("Game Over", "It's a tie!")
        return
    
    # Switch player
    current_player = "O" if current_player == "X" else "X"
    player_label.config(text=f"Player {current_player}'s Turn")

def check_winner():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return True
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    
    return False

def is_board_full():
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True

def update_score(winner):
    global score_x, score_o
    if winner == "X":
        score_x += 1
    else:
        score_o += 1
    score_label.config(text=f"X: {score_x}  |  O: {score_o}")

# Create board buttons
for i in range(3):
    button_row = []
    for j in range(3):
        button = tk.Button(board_frame, text="", width=6, height=3,
                          font=("Arial", 20, "bold"), bg="white",
                          command=lambda r=i, c=j: button_click(r, c))
        button.grid(row=i, column=j, padx=2, pady=2)
        button_row.append(button)
    buttons.append(button_row)

# Control buttons
control_frame = tk.Frame(root)
control_frame.pack(pady=20)

def new_game():
    global board, current_player, game_over
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False
    
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", bg="white")
    
    player_label.config(text=f"Player {current_player}'s Turn")

def reset_scores():
    global score_x, score_o
    score_x = 0
    score_o = 0
    score_label.config(text=f"X: {score_x}  |  O: {score_o}")
    new_game()

tk.Button(control_frame, text="New Game", command=new_game, 
         bg="lightgreen", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
tk.Button(control_frame, text="Reset Scores", command=reset_scores, 
         bg="lightcoral", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)

# AI Player (Simple)
def ai_move():
    global current_player, game_over
    
    if game_over or current_player != "O":
        return
    
    # Simple AI: find first empty spot
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                button_click(i, j)
                return

ai_var = tk.BooleanVar()
ai_frame = tk.Frame(root)
ai_frame.pack(pady=10)

ai_checkbox = tk.Checkbutton(ai_frame, text="Play against AI", variable=ai_var,
                           font=("Arial", 12))
ai_checkbox.pack()

# Override button_click for AI
original_button_click = button_click

def button_click_with_ai(row, col):
    original_button_click(row, col)
    if ai_var.get() and not game_over and current_player == "O":
        root.after(500, ai_move)  # AI moves after 500ms delay

# Update button commands
for i in range(3):
    for j in range(3):
        buttons[i][j].config(command=lambda r=i, c=j: button_click_with_ai(r, c))

# Game modes
mode_frame = tk.Frame(root)
mode_frame.pack(pady=10)

tk.Label(mode_frame, text="Game Mode:", font=("Arial", 12)).pack()

mode_var = tk.StringVar(value="normal")

tk.Radiobutton(mode_frame, text="Normal", variable=mode_var, value="normal",
              font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
tk.Radiobutton(mode_frame, text="Best of 3", variable=mode_var, value="best3",
              font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
tk.Radiobutton(mode_frame, text="Best of 5", variable=mode_var, value="best5",
              font=("Arial", 10)).pack(side=tk.LEFT, padx=5)

def check_series_win():
    mode = mode_var.get()
    if mode == "best3" and (score_x >= 2 or score_o >= 2):
        winner = "X" if score_x >= 2 else "O"
        messagebox.showinfo("Series Winner", f"Player {winner} wins the series!")
        reset_scores()
    elif mode == "best5" and (score_x >= 3 or score_o >= 3):
        winner = "X" if score_x >= 3 else "O"
        messagebox.showinfo("Series Winner", f"Player {winner} wins the series!")
        reset_scores()

# Update the update_score function
original_update_score = update_score

def update_score(winner):
    original_update_score(winner)
    check_series_win()

# Instructions
instructions = tk.Label(root, 
    text="Click on empty squares to make your move.\nFirst to get 3 in a row wins!",
    font=("Arial", 10), fg="gray", justify=tk.CENTER)
instructions.pack(pady=10)

root.mainloop()