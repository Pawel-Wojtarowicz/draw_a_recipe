import tkinter as tk
from PIL import ImageTk

bg_color = "#eaeced"

# init
root = tk.Tk()
root.title("Draw a recipe")
root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, width=600, height=400, bg=bg_color)
frame1.grid(row=0, column=0)
frame1.pack_propagate(False)

# frame1 widgets
logo_img = ImageTk.PhotoImage(file="logo.png")
logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
logo_widget.image = logo_img
logo_widget.pack()

# run app
root.mainloop()
