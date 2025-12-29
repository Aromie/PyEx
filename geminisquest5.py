import pandas as pd
import os

filename = "lesson_progress.csv"
columns = ["student", "step", "week", "day"]

def get_daily_start():
    print("Let's start daily lesson!")
    if os.path.exists(filename):
        data = pd.read_csv(filename)
    else:
        print("Starting fresh with a new list.")
        data = pd.DataFrame(columns=columns)
    
    view_progress(data)

def view_progress(data):
    print("\n--- CURRENT PROGRESS ---")
    print(data.to_string(index=False)) # Prints a clean table without index numbers
    show_menu(data)

def show_menu(data):
    answer = input("\n[A]dd Progress, [V]iew, [T]erminate: ").lower()
    if answer == 'a':
        add_progress(data)
    elif answer == 'v':
        view_progress(data)
    elif answer == 't':
        print("See you soon~")
    else:
        print("Try again!")
        show_menu(data)

def add_progress(data):    
    name = input("Student's name? ").lower()
    step = input("Which step? ")
    week = input("Which week? ")
    day = input("Which day? ")

    # The Pandas way to update or add:
    # If student exists, update them. If not, add a new row.
    if name in data['student'].values:
        data.loc[data['student'] == name, ["step", "week", "day"]] = [step, week, day]
        print(f"Updated {name}'s progress.")
    else:
        new_row = {"student": name, "step": step, "week": week, "day": day}
        data = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)
        print(f"Added new student: {name}")

    save_to_csv(data)
    view_progress(data)

def save_to_csv(data):
    data.to_csv(filename, index=False) # index=False keeps the CSV clean
if __name__ == "__main__":
    get_daily_start()