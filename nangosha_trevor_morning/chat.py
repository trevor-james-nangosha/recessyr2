
import tkinter as tk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("trevor Simple Calculator")

# Create the display
display = tk.Entry(window, width=30, justify="right")
display.grid(row=0, column=0, columnspan=4)

# Create number buttons
button_1 = tk.Button(window, text="1", padx=20, pady=10, bg='red', command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=20, pady=10, bg='red', command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=20, pady=10, bg='red', command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=20, pady=10, bg='yellow', command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=20, pady=10, bg='yellow', command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=20, pady=10, bg='yellow', command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=20, pady=10, bg='green', command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=20, pady=10, bg='green', command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=20, pady=10, bg='green', command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=20, pady=10, command=lambda: button_click(0))

# Create operator buttons
button_add = tk.Button(window, text="+", padx=20, pady=10, command=lambda: button_click("+"))
button_subtract = tk.Button(window, text="-", padx=20, pady=10, command=lambda: button_click("-"))
button_multiply = tk.Button(window, text="*", padx=20, pady=10, command=lambda: button_click("*"))
button_divide = tk.Button(window, text="/", padx=20, pady=10, command=lambda: button_click("/"))

button_equal = tk.Button(window, text="=", padx=20, pady=10, command=button_equal)
button_clear = tk.Button(window, text="C", padx=20, pady=10, command=button_clear)

# Position the buttons on the grid
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_add.grid(row=4, column=3)

# Start the GUI main loop
window.mainloop()
