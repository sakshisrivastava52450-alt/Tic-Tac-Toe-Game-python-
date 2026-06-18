import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import winsound

# ---------------- WINDOW ---------------- #
root = tk.Tk()
root.title("Tic Tac Toe Pro")
root.geometry("450x600")
root.configure(bg="lightblue")
root.resizable(False, False)

# ---------------- PLAYER NAME ---------------- #
player_name = simpledialog.askstring(
    "Player Name",
    "Enter Your Name:"
)

if not player_name:
    player_name = "Player"

# ---------------- VARIABLES ---------------- #
board = [""] * 9
buttons = []

winning_combinations = [
    [0,1,2], [3,4,5], [6,7,8],
    [0,3,6], [1,4,7], [2,5,8],
    [0,4,8], [2,4,6]
]

# ---------------- SOUNDS ---------------- #
def click_sound():
    winsound.Beep(800, 100)

def win_sound():
    winsound.Beep(1200, 200)
    winsound.Beep(1400, 200)
    winsound.Beep(1600, 300)

# ---------------- FUNCTIONS ---------------- #
def check_winner(player):
    for combo in winning_combinations:
        if all(board[pos] == player for pos in combo):

            # Highlight winning cells
            for pos in combo:
                buttons[pos].config(bg="lightgreen")

            return True
    return False


def is_draw():
    return "" not in board


def disable_board():
    for btn in buttons:
        btn.config(state="disabled")


def restart_game():

    global board
    board = [""] * 9

    for btn in buttons:
        btn.config(
            text="",
            state="normal",
            bg="white"
        )

    status_label.config(
        text=f"{player_name}'s Turn (X)"
    )


def new_game():

    global player_name

    name = simpledialog.askstring(
        "New Player",
        "Enter Player Name:"
    )

    if name:
        player_name = name

    restart_game()


def computer_move():

    available_moves = [
        i for i in range(9)
        if board[i] == ""
    ]

    if not available_moves:
        return

    move = random.choice(available_moves)

    board[move] = "O"

    buttons[move].config(
        text="O",
        state="disabled",
        fg="red"
    )

    if check_winner("O"):

        win_sound()

        status_label.config(
            text="Computer Wins!"
        )

        messagebox.showinfo(
            "Game Over",
            "Computer Wins!"
        )

        disable_board()
        return

    if is_draw():

        status_label.config(
            text="Draw Match!"
        )

        messagebox.showinfo(
            "Draw",
            "It's a Draw!"
        )

        return

    status_label.config(
        text=f"{player_name}'s Turn (X)"
    )


def player_move(index):

    if board[index] != "":
        return

    click_sound()

    board[index] = "X"

    buttons[index].config(
        text="X",
        state="disabled",
        fg="blue"
    )

    if check_winner("X"):

        win_sound()

        status_label.config(
            text=f"{player_name} Wins!"
        )

        messagebox.showinfo(
            "Congratulations 🎉",
            f"{player_name} Wins!\n\nGreat Job!"
        )

        disable_board()
        return

    if is_draw():

        status_label.config(
            text="Draw Match!"
        )

        messagebox.showinfo(
            "Draw",
            "It's a Draw!"
        )

        return

    status_label.config(
        text="Computer Thinking..."
    )

    root.after(500, computer_move)

# ---------------- TITLE ---------------- #
title_label = tk.Label(
    root,
    text="TIC TAC TOE PRO",
    font=("Arial", 22, "bold"),
    bg="lightblue",
    fg="darkblue"
)

title_label.pack(pady=10)

# ---------------- STATUS ---------------- #
status_label = tk.Label(
    root,
    text=f"{player_name}'s Turn (X)",
    font=("Arial", 14, "bold"),
    bg="lightblue"
)

status_label.pack(pady=10)

# ---------------- BOARD ---------------- #
game_frame = tk.Frame(
    root,
    bg="lightblue"
)

game_frame.pack()

for i in range(9):

    button = tk.Button(
        game_frame,
        text="",
        font=("Arial", 24, "bold"),
        width=5,
        height=2,
        bg="white",
        command=lambda i=i: player_move(i)
    )

    button.grid(
        row=i // 3,
        column=i % 3,
        padx=3,
        pady=3
    )

    buttons.append(button)

# ---------------- BUTTONS ---------------- #
restart_btn = tk.Button(
    root,
    text="Restart",
    font=("Arial", 14, "bold"),
    bg="orange",
    command=restart_game
)

restart_btn.pack(pady=10)

new_game_btn = tk.Button(
    root,
    text="New Game",
    font=("Arial", 14, "bold"),
    bg="lightgreen",
    command=new_game
)

new_game_btn.pack(pady=10)

# ---------------- FOOTER ---------------- #
footer = tk.Label(
    root,
    text="Created with Python & Tkinter",
    font=("Arial", 10),
    bg="lightblue"
)

footer.pack(side="bottom", pady=10)

root.mainloop()