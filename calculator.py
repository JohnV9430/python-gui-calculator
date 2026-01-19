import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Display
entry = tk.Entry(root, font=("Arial", 20), borderwidth=5,
                 relief="ridge", justify="right")
entry.pack(pady=20, padx=10, fill="x")

# Functions


def button_click(value):
    entry.insert(tk.END, value)


def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# Buttons
frame = tk.Frame(root)
frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row = 0
col = 0

for btn in buttons:
    if btn == "C":
        b = tk.Button(frame, text=btn, width=6, height=2, command=clear)
    elif btn == "=":
        b = tk.Button(frame, text=btn, width=6, height=2, command=calculate)
    else:
        b = tk.Button(frame, text=btn, width=6, height=2,
                      command=lambda x=btn: button_click(x))

    b.grid(row=row, column=col, padx=5, pady=5)
    col += 1

    if col > 3:
        col = 0
        row += 1

root.mainloop()
