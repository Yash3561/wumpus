from tkinter import Tk, Button, Label, Frame, messagebox
from game import game as WumpusWorld

def run_game_gui():
    # Initialize Tkinter
    root = Tk()
    root.title("Wumpus World Game")
    root.geometry("600x700")

    # Create a Frame for the grid
    grid_frame = Frame(root)
    grid_frame.pack(pady=20)

    # Feedback Label
    feedback_label = Label(root, text="Welcome to Wumpus World!", font=("Arial", 14))
    feedback_label.pack(pady=10)

    # Initialize Game
    seed = WumpusWorld.generate_seed()
    game = WumpusWorld.Game(seed)
    game.set_initial_state()

    # Create a 4x4 Grid in the Frame
    cells = [[Label(grid_frame, text=" ", width=10, height=5, bg="white", relief="solid") for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            cells[i][j].grid(row=i, column=j, padx=2, pady=2)

    # Function to Update GUI Elements
    def update_gui():
        for i in range(4):
            for j in range(4):
                cell = game.board[i][j]
                cells[0][0]['bg'] = 'lightgreen'  # Reset background
                if game.player.get_player_position() == (i, j):
                    # Highlight player position and show direction
                    direction = game.player.get_player_direction()
                    if direction == 'north':
                        cells[i][j]['text'] = '↑'  # Replace '^' with '↑'
                    elif direction == 'east':
                        cells[i][j]['text'] = '->'  # Replace '>' with '->'
                    elif direction == 'south':
                        cells[i][j]['text'] = '↓'  # Replace 'v' with '↓'
                    elif direction == 'west':
                        cells[i][j]['text'] = '<-'  # Replace '<' with '<-'
                    cells[i][j]['bg'] = 'blue'  # Highlight Player's position
                    cells[i][j]['fg'] = 'white'  # Set text color to white
                else:
                    cells[i][j]['bg'] = 'white'  # Reset background
                    cells[i][j]['text'] = ""  # Clear text

                # Display other elements like gold, pits, and Wumpus
                if cell.get_gold():
                    cells[i][j]['text'] = 'G'
                if cell.get_pit():
                    cells[i][j]['text'] = 'P'
                if cell.get_wumpus():
                    cells[i][j]['text'] = 'W'

        # Update feedback
        feedback = []
        if game.sensors['breeze']:
            feedback.append("You feel a breeze.")
        if game.sensors['stench']:
            feedback.append("You smell a stench.")
        if game.sensors['glitter']:
            feedback.append("You see a glitter.")
        feedback_label.config(text="\n".join(feedback))

    # Function to Handle Actions
    def handle_action(action):
        game.update_game_state(action)
        update_gui()
        if game.game_over:
            if game.game_won:
                messagebox.showinfo("Game Over", "Congratulations! You won!")
            else:
                messagebox.showinfo("Game Over", "You lost. Better luck next time!")
            root.destroy()  # Close the GUI after the game ends

    # Handle Keyboard Input
    def handle_keypress(event):
        key = event.char.lower()  # Convert to lowercase
        valid_keys = ['w', 'a', 's', 'd', 'g', 'x', 'q']
        if key in valid_keys:
            handle_action(key)

    root.bind("<Key>", handle_keypress)  # Bind all keypresses to handle_keypress

    # Action Buttons
    button_frame = Frame(root)
    button_frame.pack(pady=20)

    buttons = {
        'w': Button(button_frame, text="Move Forward (w)", command=lambda: handle_action('w')),
        'a': Button(button_frame, text="Turn Left (a)", command=lambda: handle_action('a')),
        's': Button(button_frame, text="Move Backward (s)", command=lambda: handle_action('s')),
        'd': Button(button_frame, text="Turn Right (d)", command=lambda: handle_action('d')),
        'g': Button(button_frame, text="Grab Gold (g)", command=lambda: handle_action('g')),
        'x': Button(button_frame, text="Shoot Arrow (x)", command=lambda: handle_action('x')),
        'q': Button(button_frame, text="Quit (q)", command=lambda: handle_action('q')),
    }

    for key, btn in buttons.items():
        btn.pack(side="left", padx=5)

    # Initial GUI Update
    update_gui()

    root.mainloop()
