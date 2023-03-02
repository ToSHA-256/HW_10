import sys

if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk

# Main window
root = tk.Tk()
root.title("Calculate it ...")
root.geometry("600x400")

# Labels and text boxes
label_one = tk.Label(root, text="Operand X:", font=("Arial", 12), fg="blue")
label_two = tk.Label(root, text="Operand Y:", font=("Arial", 12), fg="blue")
label_res = tk.Label(root, text="Result!", font=("Arial", 20), fg="black")
label_exception = tk.Label(root, text="", font=("Arial", 20), fg="black")

operand_one = tk.Entry(root, width=25)
operand_two = tk.Entry(root, width=25)

label_one.grid(column=0, row=0)
operand_one.grid(column=0, row=1)

label_two.grid(column=0, row=2)
operand_two.grid(column=0, row=3)

label_res.grid(column=0, row=5)

# Buttons
button_add = tk.Button(root, text="+", padx=10, pady=5,
                       command=lambda: label_res.config(text=calc_add(operand_one.get(), operand_two.get())))
button_sub = tk.Button(root, text="-", padx=10, pady=5,
                       command=lambda: label_res.config(text=calc_sub(operand_one.get(), operand_two.get())))
button_time = tk.Button(root, text="*", padx=10, pady=5,
                        command=lambda: label_res.config(text=calc_time(operand_one.get(), operand_two.get())))
button_dev = tk.Button(root, text="/", padx=10, pady=5,
                       command=lambda: label_res.config(text=calc_dev(operand_one.get(), operand_two.get())))
button_mod = tk.Button(root, text="x mod (y)", padx=10, pady=5,
                       command=lambda: label_res.config(text=calc_mod(operand_one.get(), operand_two.get())))
button_perc = tk.Button(root, text="%", padx=10, pady=5,
                        command=lambda: label_res.config(text=calc_perc(operand_one.get(), operand_two.get())))
button_pow = tk.Button(root, text="x^y", padx=10, pady=5,
                       command=lambda: label_res.config(text=calc_pow(operand_one.get(), operand_two.get())))

button_add.grid(column=1, row=0, padx=5, pady=5)
button_sub.grid(column=2, row=0, padx=5, pady=5)
button_time.grid(column=3, row=0, padx=5, pady=5)
button_dev.grid(column=1, row=1, padx=5, pady=5)
button_perc.grid(column=2, row=1, padx=5, pady=5)
button_pow.grid(column=3, row=1, padx=5, pady=5)
button_mod.grid(column=2, row=2)


# Functions
def calc_add(one, two):
    try:
        return float(one) + float(two)
    except BaseException as xcp:
        return xcp


def calc_sub(one, two):
    try:
        return float(one) - float(two)
    except BaseException as xcp:
        return xcp


def calc_time(one, two):
    try:
        return float(one) * float(two)
    except BaseException as xcp:
        return xcp


def calc_dev(one, two):
    try:
        if float(two) == 0:
            raise MyException("Учи матчасть! На 0 делишь!")
        return float(one) / float(two)
    except MyException as my_xcp:
        return my_xcp
    except BaseException as xcp:
        return xcp


def calc_perc(one, two):
    try:
        return float(one) / float(two) * 100
    except BaseException as xcp:
        return xcp


def calc_pow(one, two):
    try:
        return float(one) ** float(two)
    except BaseException as xcp:
        return xcp


def calc_mod(one, two):
    try:
        return float(one) % float(two)
    except BaseException as xcp:
        return xcp


class MyException(Exception):
    def __init__(self, message):
        self.message = message


root.mainloop()
