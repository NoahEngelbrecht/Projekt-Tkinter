#========================================Import===================================#
from tkinter import *
from tkinter import messagebox
import random

#=================Settings=====================================#
root = Tk()
root.geometry("400x500")
root.title("Slutprojekt")
root.resizable(width=False, height=False)

#========================Variabel=============================#
colour_player1 = "#f4ebd0"
colour1 = "#b68d40"
colour2 = "#d6ad60"
player1_turn_color = "#f4ebd0"
player2_turn_color = "#f4ebd0"

root.configure(bg=colour1)

result_dice = StringVar()
current_score = StringVar(value="Nuvarande poäng: 0")
player1_score = 0
player2_score = 0
current_player = 1
current_turn_score = 0
# =======================Frames========================#

# Frames för att kunna placera ut alla buttons och labels på korrekt plats. Av Noah

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
def throw(): # Funktion för att man ska kunna slå tärningen och så att poängen ska adderas till nuvarande poäng. Av Noah
    global current_turn_score
    if not is_turn:
        return

    dice_roll = random.randint(1, 6)
    result_dice.set(dice_roll)
    
    if dice_roll == 1:
        current_turn_score = 0
        current_score.set("Nuvarande poäng: 0")
        switch_player()
    else:
        current_turn_score += dice_roll
        current_score.set(f"Nuvarande poäng: {current_turn_score}")

def keep(): # Funktion för att knappen för att spara poäng och uppdatera spelarens poäng i labeln. Av Noah
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

def check_winner(score): # Funktion för att kolla om en spelare har nått 50 poäng och därmed vunnit. Tar även upp en messagebox om en person vinner för att fråga om spelarna vill spela igen. Av Noah
    if score >= 50:
        winner = "Spelare 1" if player1_score >= 50 else "Spelare 2"
        result_message = f"{winner} har vunnit! Vill du spela igen?"
        if messagebox.askyesno("Spelare vinner!", result_message):
            reset_game()
        else:
            root.quit()
        
def switch_player(): # Funktion för att byta spelare. Av Noah
    global current_player, is_turn
    is_turn = False
    current_player = 2 if current_player == 1 else 1
    result_dice.set("")
    update_turn_label()
    
    root.after(1000, enable_turn)

def enable_turn(): # Funktion för att ha koll på om det är en spelares tur, gjord för att kunna lägga till så att man inte råkar slå tärningen en extra gång efter att man har slått en etta. Av Noah
    global is_turn
    is_turn = True

def update_turn_label(): # Funktion som ändrar bakgrundsfärg på ena labeln som visar poäng för att göra det lättare att se vems tur det är. Av Noah
    if current_player == 1:
        lbl_firstPlayer.config(bg=player1_turn_color)
        lbl_secondPlayer.config(bg=colour1)
    else:
        lbl_secondPlayer.config(bg=player2_turn_color)
        lbl_firstPlayer.config(bg=colour1)

def reset_game(): # Funktion för att starta om spelet när en person har vunnit. Av Noah
    global player1_score, player2_score, current_player, current_turn_score, is_turn
    player1_score = 0
    player2_score = 0
    current_player = 1
    current_turn_score = 0
    current_score.set("Nuvarande poäng: 0")
    lbl_firstPlayer.config(text="Spelare 1: 0", bg=colour1)
    lbl_secondPlayer.config(text="Spelare 2: 0", bg=colour1)
    result_dice.set("")
    update_turn_label()
    is_turn = True
# =======================Buttons=======================#
btn_throw = Button(top_fifth, text="Kasta tärningen", width=16,font=("T-25", 36), bg=colour2, command=throw) # Knapp för att kasta tärningen. Av Noah
btn_throw.pack(side=LEFT, padx=5, pady=5)
btn_keep = Button(top_sixth, text="Behåll", width=6,font=("T-25", 36), bg=colour2, command=keep) # Knapp för att behålla nuvarande poäng. Av Noah
btn_keep.pack(side=LEFT, padx=5, pady=5)

# =======================Label=========================#
lbl_firstPlayer = Label(top_first, text="Spelare 1: 0", font=("T-25", 36), bg=colour_player1) # Label för att visa sparade poängen för spelare 1. Av Noah
lbl_firstPlayer.pack(side=LEFT, padx=5, pady=5)
lbl_secondPlayer = Label(top_second, text="Spelare 2: 0", font=("T-25", 36), bg=colour1) # Label för att visa sparade poängen för spelare 2. Av Noah
lbl_secondPlayer.pack(side=LEFT, padx=5, pady=5)
lbl_currentPoints = Label(top_third, font=("T-25", 16), bg=colour1, textvariable=current_score) # Label för att visa nuvarande poäng som ej är sparade. Av Noah
lbl_currentPoints.pack(side=LEFT, padx=5, pady=5)

lbl_result = Label(top_fourth, bg=colour2, width=1, font=("T-25", 36), textvariable=result_dice) # Label för att visa resultatet av tärningsslaget. Av Noah.
lbl_result.pack(side=LEFT,padx=5,pady=5)

# =======================Run===========================#
is_turn = True
root.mainloop()
