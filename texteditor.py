import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text.delete("1.0", tk.END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text.delete("1.0", tk.END)
            text.insert("1.0", file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get("1.0", tk.END))

def about():
    messagebox.showinfo("About", "Simple Text Editor\nVersion 1.0\nCreated by YourName")

# Create the main application window
app = tk.Tk()
app.title("Simple Text Editor")

# Create a text widget
text = tk.Text(app, wrap="word", undo=True)
text.pack(expand=True, fill="both")

# Create a menu
menu_bar = tk.Menu(app)
app.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)

# Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

app.mainloop()


