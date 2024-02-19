# Calculator
from tkinter import *

# Calculator screen
calc = Tk()
calc.geometry("292x495")
calc.configure(bg="grey")
calc.title("Calculator")

# Assigning functions to buttons
output = ''

def show(value):
    global output
    output += value
    display.config(text=output)


def clear_all():
    display.config(text='')
    global output
    output = ''
    result_display.config(text='0')


def backspace():
    global output
    output = output[:-1]
    display.config(text=output)


def result_print():
    if result != None:
        global output
        output = str(result)
    else:
        pass

state = False

def brackets():
    global state
    if not state:
        show('(')
    elif state:
        show(')')
        
    state = not state



result = ''


def result_show():
    try:
        global result
        result = eval(output)
        result_display.config(text=result)
    except:
        result_display.config(text='ERROR!')
        result = None


# Display
display = Label(calc, width=40, height=5, bg="grey", fg="white", text='', font=("ariel", 9, 'bold'))
display.grid(row=0, columnspan=4)

result_display = Label(calc, width=40, height=4, bg="dark grey", fg="white", text='0', font=("ariel", 9, 'bold'))
result_display.grid(row=1, columnspan=4)

# Creating buttons
one = Button(text="1", width=9, height=4, bg="dim grey", fg="white", command=lambda: show("1"))
one.grid(row=5, column=0)

two = Button(text="2", width=9, height=4, bg="dim grey", fg="white", command=lambda: show("2"))
two.grid(row=5, column=1)

three = Button(text="3", width=9, height=4, bg="dim grey", fg="white", command=lambda: show("3"))
three.grid(row=5, column=2)

four = Button(text="4", width=9, height=4, bg="dim grey", fg="white", command=lambda: show("4"))
four.grid(row=4, column=0)

five = Button(text="5", width=9, height=4, bg="dim grey", fg="white", command=lambda: show("5"))
five.grid(row=4, column=1)

six = Button(text="6", width=9, height=4, bg="dim grey", fg="white", command=lambda: show("6"))
six.grid(row=4, column=2)

seven = Button(text="7", width=9, height=4, bg="dim grey", fg="white", command=lambda: show("7"))
seven.grid(row=3, column=0)

eight = Button(text="8", width=9, height=4, bg="dim grey", fg="white", command=lambda: show("8"))
eight.grid(row=3, column=1)

nine = Button(text="9", width=9, height=4, bg="dim grey", fg="white", command=lambda: show("9"))
nine.grid(row=3, column=2)

zero = Button(text="0", width=9, height=4, bg="dim grey", fg="white", command=lambda: show("0"))
zero.grid(row=6, column=1)

dot = Button(text=".", width=9, height=4, bg="dim grey", fg="white", command=lambda: show("."))
dot.grid(row=6, column=0)

equal = Button(text="=", width=9, height=4, bg="dim grey", fg="white", command=lambda: [result_show(), result_print()])
equal.grid(row=6, column=2)

plus = Button(text="+", width=9, height=4, bg="dim grey", fg="white", command=lambda: show("+"))
plus.grid(row=6, column=3)

minus = Button(text="-", width=9, height=4, bg="dim grey", fg="white", command=lambda: show("-"))
minus.grid(row=5, column=3)

multiply = Button(text="x", width=9, height=4, bg="dim grey", fg="white", command=lambda: show("*"))
multiply.grid(row=4, column=3)

divide = Button(text="÷", width=9, height=4, bg="dim grey", fg="white", command=lambda: show("/"))
divide.grid(row=3, column=3)

power = Button(text="^", width=9, height=4, bg="dim grey", fg="white", command=lambda: show("**"))
power.grid(row=2, column=0)

bracket = Button(text="( )", width=9, height=4, bg="dim grey", fg="white", command=brackets)
bracket.grid(row=2, column=1)

back_space = Button(text="<--", width=9, height=4, bg="dim grey", fg="white", command=backspace)
back_space.grid(row=2, column=3)

clear = Button(text="C", width=9, height=4, bg="dim grey", fg="white", command=clear_all)
clear.grid(row=2, column=2)

calc.mainloop()
