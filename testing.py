import tkinter as tk

# Create the window and set its title
window = tk.Tk()
window.title("Puzzle Game")

# Create a canvas where the game will be drawn
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Create a player character as a rectangle
player = canvas.create_rectangle(0, 0, 25, 25)

# Set the player's initial position
canvas.move(player, 200, 200)

# Define movement functions
def move_up():
    canvas.move(player, 0, -5)

def move_down():
    canvas.move(player, 0, 5)

def move_left():
    canvas.move(player, -5, 0)

def move_right():
    canvas.move(player, 5, 0)

# Bind the movement functions to the arrow keys
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

# Create a main loop to keep the window open
window.mainloop()