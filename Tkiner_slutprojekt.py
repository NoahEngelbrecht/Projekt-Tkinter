#========================================Import===================================#
from tkinter import *
from tkinter import messagebox
import random

#=================Settings==================================#
root = Tk()
root.geometry("400x500")
root.title("Slutprojekt")
root.resizable(width=False, height=False)

#==============Variabel=======================
colour1 = "#b68d40"
colour2 = "#122620"
player1_turn_color = "#f4ebd0"
player2_turn_color = "#f4ebd0"

root.configure(bg=colour1)

result_dice = StringVar()
current_score = StringVar(value="Nuvarande poäng: 0")
player1_score = 0
player2_score = 0
current_player = 1
current_turn_score = 0
if current_player == 1:
    player1_turn_color = "#f4ebd0"
# =======================Frames========================#

top_first = Frame(root, width=400, height=50, bg=colour1)
top_first.pack(side="top")
top_second = Frame(root, width=400, height=50, bg=colour1)
top_second.pack(side="top")
top_third = Frame(root, width=400, height=50, bg=colour1)
top_third.pack(side="top")
top_fourth = Frame(root, width=400, height=50, bg=colour1)
top_fourth.pack(side="top")
top_fifth = Frame(root, width=400, height=50, bg=colour1)
top_fifth.pack(side="top")
top_sixth = Frame(root, width=400, height=50, bg=colour1)
top_sixth.pack(side="top")

# =======================Functions=====================#
def throw():
    global current_turn_score
    dice_roll = random.randint(1, 6)
    result_dice.set(dice_roll)
    
    if dice_roll == 1:
        current_turn_score = 0
        current_score.set("Nuvarande poäng: 0")
        switch_player()
    else:
        current_turn_score += dice_roll
        current_score.set(f"Nuvarande poäng: {current_turn_score}")

def keep():
    global player1_score, player2_score, current_player, current_turn_score
    if current_turn_score > 0:
        if current_player == 1:
            player1_score += current_turn_score
            lbl_firstPlayer.config(text=f"Spelare 1: {player1_score}")
            check_winner(player1_score)
        else:
            player2_score += current_turn_score
            lbl_secondPlayer.config(text=f"Spelare 2: {player2_score}")
            check_winner(player2_score)
        
        current_turn_score = 0
        current_score.set("Nuvarande poäng: 0")
        switch_player()

def check_winner(score):
    if score >= 50:
        winner = "Spelare 1" if player1_score >= 50 else "Spelare 2"
        result_message = f"{winner} har vunnit! Vill du spela igen?"
        if messagebox.askyesno("Spelare vinner!", result_message):
            reset_game()
        else:
            root.quit()
        
def switch_player():
    global current_player
    current_player = 2 if current_player == 1 else 1
    result_dice.set("")
    update_turn_label()

def update_turn_label():
    if current_player == 1:
        lbl_firstPlayer.config(bg=player1_turn_color)
        lbl_secondPlayer.config(bg=colour1)
    else:
        lbl_secondPlayer.config(bg=player2_turn_color)
        lbl_firstPlayer.config(bg=colour1)

def reset_game():
    global player1_score, player2_score, current_player, current_turn_score
    player1_score = 0
    player2_score = 0
    current_player = 1
    current_turn_score = 0
    current_score.set("Nuvarande poäng: 0")
    lbl_firstPlayer.config(text="Spelare 1: 0", bg=colour1)
    lbl_secondPlayer.config(text="Spelare 2: 0", bg=colour1)
    result_dice.set("")
    update_turn_label()


# =======================Buttons=======================#
btn_throw = Button(top_fifth, text="Kasta tärningen", width=16,font=("T-25", 36), bg=colour2, command=throw)
btn_throw.pack(side=LEFT, padx=5, pady=5)
btn_keep = Button(top_sixth, text="Behåll", width=6,font=("T-25", 36), bg=colour2, command=keep)
btn_keep.pack(side=LEFT, padx=5, pady=5)


# =======================Label & Entry=================#
lbl_firstPlayer = Label(top_first, text="Spelare 1: 0", font=("T-25", 36), bg=colour1)
lbl_firstPlayer.pack(side=LEFT, padx=5, pady=5)
lbl_secondPlayer = Label(top_second, text="Spelare 2: 0", font=("T-25", 36), bg=colour1)
lbl_secondPlayer.pack(side=LEFT, padx=5, pady=5)
lbl_currentPoints = Label(top_third, font=("T-25", 16), bg=colour1, textvariable=current_score)
lbl_currentPoints.pack(side=LEFT, padx=5, pady=5)

lbl_result = Label(top_fourth, bg=colour2, width=1, font=("T-25", 36), textvariable=result_dice)
lbl_result.pack(side=LEFT,padx=5,pady=5)






# =======================Run===========================#
root.mainloop()