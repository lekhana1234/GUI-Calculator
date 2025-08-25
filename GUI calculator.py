import tkinter as tk

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    gui = tk.Tk()
    gui.configure(background="lightgray")
    gui.title("OutriX – Basic Calculator")
    gui.geometry("320x420")

    expression = ""
    equation = tk.StringVar()

    entry_field = tk.Entry(gui, textvariable=equation, font=('Arial', 20),
                           bd=10, relief="sunken", justify="right")
    entry_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=10)

    buttons = [
        ('C', 1, 0), ('/', 1, 1), ('*', 1, 2), ('-', 1, 3),
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('=', 3, 3),
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('.', 4, 3),
        ('0', 5, 0),
    ]

    for (text, row, col) in buttons:
        if text == "C":
            btn = tk.Button(gui, text=text, fg="white", bg="red",
                            command=clear, height=3, width=6, font=('Arial', 16))
        elif text == "=":
            btn = tk.Button(gui, text=text, fg="white", bg="green",
                            command=equalpress, height=3, width=6, font=('Arial', 16))
        else:
            btn = tk.Button(gui, text=text, fg="black", bg="lightgray",
                            command=lambda t=text: press(t), height=3, width=6, font=('Arial', 16))
        btn.grid(row=row, column=col, padx=5, pady=5)

    zero_btn = tk.Button(gui, text="0", fg="black", bg="lightgray",
                         command=lambda: press("0"), height=3, width=14, font=('Arial', 16))
    zero_btn.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    gui.mainloop()
