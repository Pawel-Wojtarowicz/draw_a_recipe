import tkinter as tk
from PIL import ImageTk
import sqlite3
from numpy import random

bg_color = "#eaeced"


def fetch_db():
    connection = sqlite3.connect("data/recipes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
    all_tables = cursor.fetchall()
    random_idx = random.randint(0, len(all_tables)-1)

    # fetch ingredients
    table_name = all_tables[random_idx][1]
    cursor.execute("SELECT * FROM " + table_name + ";")
    table_records = cursor.fetchall()

    connection.close()
    return table_name, table_records


def pre_process(table_name, table_records):
    title = table_name[:-6]
    title = "".join([char if char.islower() else " " + char for char in title])

    # ingredients
    ingredients = []
    for i in table_records:
        name = i[1]
        qty = i[2]
        unit = i[3]
        ingredients.append(qty + " " + unit + " of " + name)

    return title, ingredients

def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    

def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False)

    # frame1 widget
    logo_img = ImageTk.PhotoImage(file="logo.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack()
    tk.Label(frame1, text="ready for your random recipe?",
             bg=bg_color, font=("TkMenuFont", 14)).pack(pady=5)

    # button
    tk.Button(frame1, text="DRAW", font=("TkHeadingFont", 16), bg="#b4bccc", cursor="hand2",
              activebackground="#0e2c75", activeforeground="white", command=lambda: load_frame2()).pack(pady=15)


def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()
    table_name, table_records = fetch_db()
    title, ingredients = pre_process(table_name, table_records)

    # frame2 widget
    logo_img = ImageTk.PhotoImage(file="logo.png")
    logo_widget = tk.Label(frame2, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack()

    tk.Label(frame2, text=title, bg=bg_color,
             font=("TkHeadingFont", 18)).pack(pady=5)

    for i in ingredients:
        tk.Label(frame2, text=i, bg="#b4bccc", font=("TkMenuFont", 16)).pack(fill="both")

    tk.Button(frame2, text="BACK", font=("TkHeadingFont", 14), bg="#b4bccc", cursor="hand2",
              activebackground="#0e2c75", activeforeground="white", command=lambda: load_frame1()).pack(pady=15)

# init
root = tk.Tk()
root.title("Draw a recipe")
root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, width=400, height=300, bg=bg_color)
frame2 = tk.Frame(root, bg=bg_color)    

for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky="nesw")

load_frame1()


# run app
root.mainloop()
