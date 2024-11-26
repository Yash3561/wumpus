from tkinter import Tk, Button, Label
from wumpus_world_gui import run_game_gui  # Import the GUI-based game function

# Function to handle human play
def handle_human_play():
    run_game_gui()  # Launch the GUI-based game

# Function to exit the application
def exit_app():
    root.destroy()

# Main script for the GUI
if __name__ == "__main__":
    root = Tk()
    root.title("Wumpus World Menu")
    root.geometry("400x300")

    # Add a label for the title
    title_label = Label(root, text="Wumpus World Game", font=("Arial", 18, "bold"))
    title_label.pack(pady=20)

    # Add buttons for each option
    human_button = Button(root, text="Human Play", command=handle_human_play, font=("Arial", 14))
    human_button.pack(pady=10)

    exit_button = Button(root, text="Exit", command=exit_app, font=("Arial", 14))
    exit_button.pack(pady=20)

    root.mainloop()
