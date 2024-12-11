import os
import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk
from tkinter import font

current_flags_folder = "flagi"
historical_flags_folder = "hist flagi"
imperia_flags_folder = "imperia"
time_flags_folder = "time"

print("Current flags folder:", current_flags_folder)
print("Historical flags folder:", historical_flags_folder)
print("Imperia flags folder:", imperia_flags_folder)
print("Time flags folder:", time_flags_folder)

folders = [current_flags_folder, historical_flags_folder, imperia_flags_folder, time_flags_folder]
for folder in folders:
    if os.path.exists(folder):
        print(f"{folder} exists")
    else:
        print(f"{folder} does not exist")

current_flags = {
    "wb.png": "United Kingdom",
    "germa.png": "Germany",
    "poland.png": "Poland",
    "brazil.png": "Brazil",
    "spain.png": "Spain",
    "chec.png": "Czech Republic",
    "swed.png": "Sweden"
}

historical_flags = {
    "avstro.png": "Austro-Hungarian Empire",
    "cccr.png": "Soviet Union",
    "germa.png": "Third Reich",
    "imperia.png": "Russian Empire",
    "prussia.png": "Prussia",
    "yugo.png": "Yugoslavia",
    "osman.png": "Ottoman Empire"
}

imperia_flags = {
    "imperia.png": "Russian Empire",
    "rome.png": "Roman Empire",
    "byzan.png": "Byzantine Empire",
    "swed.png": "Swedish Empire",
    "brita.png": "British Empire",
    "france.png": "French Empire"
}

time_flags = {
    "wb.png": "United Kingdom",
    "germa.png": "Germany",
    "poland.png": "Poland",
    "brazil.png": "Brazil",
    "spain.png": "Spain",
    "chec.png": "Czech Republic",
    "swed.png": "Sweden",
    "avstro.png": "Austro-Hungarian Empire",
    "cccr.png": "Soviet Union",
    "germa.png": "Third Reich",
    "osman.png": "Ottoman Empire",
    "prussia.png": "Prussia",
    "yugo.png": "Yugoslavia",
    "imperia.png": "Russian Empire",
    "rome.png": "Roman Empire",
    "byzan.png": "Byzantine Empire",
    "swed.png": "Swedish Empire",
    "brita.png": "British Empire",
    "france.png": "French Empire"
}

correct_country = ""
mode = "flags"
record = 0
time_limit = 15
time_remaining = time_limit
timer_running = False

def exit_game():
    window.quit()

def show_flag(flag_dict, folder):
    global correct_country, timer_running
    flag_file, country_name = random.choice(list(flag_dict.items()))
    print(f"Selected flag for mode {mode}: {flag_file}, Country: {country_name}")
    
    correct_country = flag_file
    
    flag_path = os.path.join(folder, flag_file)
    
    if not os.path.exists(flag_path):
        messagebox.showerror("Error", f"File {flag_path} not found.")
        return
    
    img = Image.open(flag_path)
    img = img.resize((300, 150))
    flag_image = ImageTk.PhotoImage(img)
    
    flag_label.config(image='')
    flag_label.image = None
    
    flag_label.config(image=flag_image)
    flag_label.image = flag_image

    countries = list(flag_dict.values())
    countries.remove(country_name)
    random_countries = random.sample(countries, min(3, len(countries)))
    answer_options = random_countries + [country_name]
    random.shuffle(answer_options)
    
    for i, btn in enumerate(buttons):
        btn.config(text=answer_options[i], command=lambda c=answer_options[i]: check_answer(c, flag_dict))

    if mode == "time":
        time_label.pack(pady=10)
        if not timer_running:
            time_remaining = time_limit
            timer_running = True
            update_timer()
    else:
        time_label.pack_forget()

def check_answer(selected_country, flag_dict):
    global record
    if selected_country == flag_dict[correct_country]:  
        record += 1
        record_label.config(text=f"Score: {record}")
        show_flag(flag_dict, current_flags_folder if flag_dict == current_flags else historical_flags_folder if flag_dict == historical_flags else imperia_flags_folder if flag_dict == imperia_flags else time_flags_folder)
    else:
        end_game(f"You lost! Your score: {record}\nThe correct answer was: {flag_dict[correct_country]}")

def end_game(message):
    global record, timer_running
    timer_running = False
    messagebox.showinfo("Game Over", message)
    record = 0
    record_label.config(text="Score: 0")
    menu_frame.pack()

def start_game():
    global mode
    mode = "flags"
    menu_frame.pack_forget()
    mode_frame.pack(pady=50)

def start_game_with_mode(selected_mode):
    global mode
    mode = selected_mode.lower()
    print(f"Selected mode: {mode}")
    
    mode_frame.pack_forget()
    game_frame.pack()
    record_label.config(text="Score: 0")
    
    if mode == "flags":
        show_flag(current_flags, current_flags_folder)
    elif mode == "history":
        show_flag(historical_flags, historical_flags_folder)
    elif mode == "empire":
        show_flag(imperia_flags, imperia_flags_folder)
    elif mode == "time":
        show_flag(time_flags, time_flags_folder)

def update_timer():
    global time_remaining, timer_running
    if timer_running:
        if time_remaining > 0:
            time_label.config(text=f"Time left: {time_remaining} seconds")
            time_remaining -= 1
            window.after(1000, update_timer)
        else:
            end_game(f"Time is up! Your score: {record}")

window = tk.Tk()
window.title("Guess the Flag")
window.geometry("500x400")

menu_frame = tk.Frame(window)
menu_frame.pack()

title_font = font.Font(family="Helvetica", size=24, weight="bold")

title_label = tk.Label(menu_frame, text="Guess the Flag", font=title_font)
title_label.pack(pady=20)

start_button = tk.Button(menu_frame, text="Play", width=20, height=2, command=start_game)
start_button.pack(pady=10)

exit_button = tk.Button(menu_frame, text="Exit", width=20, height=2, command=exit_game)
exit_button.pack(pady=10)

mode_frame = tk.Frame(window)

flags_button = tk.Button(mode_frame, text="Flags", width=20, height=2, command=lambda: start_game_with_mode("flags"))
flags_button.pack(pady=10)

history_button = tk.Button(mode_frame, text="History", width=20, height=2, command=lambda: start_game_with_mode("history"))
history_button.pack(pady=10)

empire_button = tk.Button(mode_frame, text="Empire", width=20, height=2, command=lambda: start_game_with_mode("empire"))
empire_button.pack(pady=10)

time_button = tk.Button(mode_frame, text="Time", width=20, height=2, command=lambda: start_game_with_mode("time"))
time_button.pack(pady=10)

game_frame = tk.Frame(window)

flag_label = tk.Label(game_frame)
flag_label.pack(pady=20)

record_label = tk.Label(game_frame, text="Score: 0", font=font.Font(family="Helvetica", size=18, weight="bold"))
record_label.pack(pady=10)

time_label = tk.Label(game_frame, text="Time left: 0 seconds", font=font.Font(family="Helvetica", size=14, weight="bold"))

buttons = []
for i in range(4):
    btn = tk.Button(game_frame, text="", width=20, height=2)
    btn.pack(pady=5)
    buttons.append(btn)

window.after(100, lambda: show_flag(current_flags, current_flags_folder))

window.mainloop()