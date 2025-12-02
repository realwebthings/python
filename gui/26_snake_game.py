import tkinter as tk
import random

# Snake Game
root = tk.Tk()
root.title("Snake Game")
root.geometry("600x650")
root.resizable(False, False)

# Game constants
BOARD_WIDTH = 600
BOARD_HEIGHT = 600
UNIT_SIZE = 25
GAME_UNITS = BOARD_WIDTH // UNIT_SIZE
DELAY = 100

# Game variables
snake = [(0, 0)]
food = (0, 0)
direction = "Right"
score = 0
high_score = 0
game_running = False

# Colors
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

# UI Elements
info_frame = tk.Frame(root, bg="black", height=50)
info_frame.pack(fill=tk.X)
info_frame.pack_propagate(False)

score_label = tk.Label(info_frame, text=f"Score: {score}", font=("Arial", 16), 
                      bg="black", fg="white")
score_label.pack(side=tk.LEFT, padx=20, pady=10)

high_score_label = tk.Label(info_frame, text=f"High Score: {high_score}", font=("Arial", 16), 
                           bg="black", fg="yellow")
high_score_label.pack(side=tk.RIGHT, padx=20, pady=10)

# Game canvas
canvas = tk.Canvas(root, bg=BACKGROUND_COLOR, width=BOARD_WIDTH, height=BOARD_HEIGHT)
canvas.pack()

def new_food():
    global food
    x = random.randint(0, GAME_UNITS - 1) * UNIT_SIZE
    y = random.randint(0, GAME_UNITS - 1) * UNIT_SIZE
    food = (x, y)

def draw_food():
    canvas.create_oval(food[0], food[1], food[0] + UNIT_SIZE, food[1] + UNIT_SIZE, 
                      fill=FOOD_COLOR, tags="food")

def draw_snake():
    canvas.delete("snake")
    for i, (x, y) in enumerate(snake):
        if i == 0:  # Head
            canvas.create_rectangle(x, y, x + UNIT_SIZE, y + UNIT_SIZE, 
                                  fill="yellow", outline="black", width=2, tags="snake")
        else:  # Body
            canvas.create_rectangle(x, y, x + UNIT_SIZE, y + UNIT_SIZE, 
                                  fill=SNAKE_COLOR, outline="darkgreen", tags="snake")

def move_snake():
    global snake
    head_x, head_y = snake[0]
    
    if direction == "Up":
        new_head = (head_x, head_y - UNIT_SIZE)
    elif direction == "Down":
        new_head = (head_x, head_y + UNIT_SIZE)
    elif direction == "Left":
        new_head = (head_x - UNIT_SIZE, head_y)
    elif direction == "Right":
        new_head = (head_x + UNIT_SIZE, head_y)
    
    snake.insert(0, new_head)

def check_collisions():
    head_x, head_y = snake[0]
    
    # Check wall collision
    if (head_x < 0 or head_x >= BOARD_WIDTH or 
        head_y < 0 or head_y >= BOARD_HEIGHT):
        return True
    
    # Check self collision
    if snake[0] in snake[1:]:
        return True
    
    return False

def check_food():
    global score, high_score
    if snake[0] == food:
        score += 10
        score_label.config(text=f"Score: {score}")
        
        if score > high_score:
            high_score = score
            high_score_label.config(text=f"High Score: {high_score}")
        
        new_food()
        canvas.delete("food")
        draw_food()
    else:
        snake.pop()  # Remove tail if no food eaten

def game_over():
    global game_running
    game_running = False
    canvas.create_text(BOARD_WIDTH // 2, BOARD_HEIGHT // 2, 
                      text="GAME OVER", fill="red", font=("Arial", 30, "bold"))
    canvas.create_text(BOARD_WIDTH // 2, BOARD_HEIGHT // 2 + 40, 
                      text=f"Final Score: {score}", fill="white", font=("Arial", 16))
    canvas.create_text(BOARD_WIDTH // 2, BOARD_HEIGHT // 2 + 70, 
                      text="Press SPACE to restart", fill="yellow", font=("Arial", 14))

def game_loop():
    global game_running
    
    if game_running:
        move_snake()
        
        if check_collisions():
            game_over()
            return
        
        check_food()
        draw_snake()
        
        root.after(DELAY, game_loop)

def start_game():
    global snake, direction, score, game_running
    
    snake = [(0, 0)]
    direction = "Right"
    score = 0
    game_running = True
    
    score_label.config(text=f"Score: {score}")
    canvas.delete("all")
    
    new_food()
    draw_food()
    draw_snake()
    
    game_loop()

def change_direction(new_direction):
    global direction
    
    if not game_running:
        return
    
    # Prevent reverse direction
    opposite_directions = {
        "Up": "Down", "Down": "Up",
        "Left": "Right", "Right": "Left"
    }
    
    if new_direction != opposite_directions.get(direction):
        direction = new_direction

def on_key_press(event):
    key = event.keysym
    
    if key == "space":
        if not game_running:
            start_game()
    elif key in ["Up", "Down", "Left", "Right"]:
        change_direction(key)
    elif key in ["w", "W"]:
        change_direction("Up")
    elif key in ["s", "S"]:
        change_direction("Down")
    elif key in ["a", "A"]:
        change_direction("Left")
    elif key in ["d", "D"]:
        change_direction("Right")

# Control buttons
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

tk.Button(control_frame, text="Start Game", command=start_game, 
         bg="lightgreen", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)

def pause_game():
    global game_running
    game_running = not game_running
    if game_running:
        game_loop()

tk.Button(control_frame, text="Pause/Resume", command=pause_game, 
         bg="lightyellow", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)

# Speed control
speed_frame = tk.Frame(root)
speed_frame.pack(pady=5)

tk.Label(speed_frame, text="Speed:", font=("Arial", 10)).pack(side=tk.LEFT)

def change_speed(value):
    global DELAY
    DELAY = 200 - int(value)  # Invert so higher value = faster

speed_scale = tk.Scale(speed_frame, from_=1, to=10, orient=tk.HORIZONTAL, 
                      command=change_speed, length=200)
speed_scale.set(5)
speed_scale.pack(side=tk.LEFT, padx=10)

# Arrow key controls
arrow_frame = tk.Frame(root)
arrow_frame.pack(pady=10)

tk.Label(arrow_frame, text="Controls:", font=("Arial", 12, "bold")).pack()

controls_frame = tk.Frame(arrow_frame)
controls_frame.pack(pady=5)

tk.Button(controls_frame, text="↑", command=lambda: change_direction("Up"), 
         width=3, height=1).grid(row=0, column=1)
tk.Button(controls_frame, text="←", command=lambda: change_direction("Left"), 
         width=3, height=1).grid(row=1, column=0)
tk.Button(controls_frame, text="↓", command=lambda: change_direction("Down"), 
         width=3, height=1).grid(row=1, column=1)
tk.Button(controls_frame, text="→", command=lambda: change_direction("Right"), 
         width=3, height=1).grid(row=1, column=2)

# Instructions
instructions = tk.Label(root, 
    text="Use arrow keys or WASD to move • SPACE to start/restart • Eat red food to grow!",
    font=("Arial", 10), fg="gray")
instructions.pack(pady=5)

# Bind keyboard events
root.bind("<KeyPress>", on_key_press)
root.focus_set()

# Initialize game
canvas.create_text(BOARD_WIDTH // 2, BOARD_HEIGHT // 2, 
                  text="SNAKE GAME", fill="white", font=("Arial", 30, "bold"))
canvas.create_text(BOARD_WIDTH // 2, BOARD_HEIGHT // 2 + 50, 
                  text="Press SPACE to start", fill="yellow", font=("Arial", 16))

root.mainloop()