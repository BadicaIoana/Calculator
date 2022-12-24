# importing everything from tkinter
from tkinter import *
# Creating the main window

root = Tk()

# Setting the title of the window

root.title('Calculator')

# Setting the size of the window

root.geometry('350x510')

# Schedule a task to be executed after a certain time interval

root.after(300)

# Setting a string variable

equation = StringVar()

# Setting a variable with empty string

result = ""

# This code defines a function named click() that takes in a parameter number


def click(number):
    global result
    result = result + str(number)
    equation.set(result)
    
# This code defines a function named equal_btn() that calculates the result entered the field


def equal_btn():
    global result
    total = str(eval(result))
    equation.set(total)
    result = ""
    
# This code defines a function named clear_btn() that clears the contents of an input field


def clear_btn():
    result_field.delete(0, END)
    
# In this code, an Entry widget is being created and placed in a grid layout in a Tkinter GUI.
# The Entry widget is used to create an input field in which the user can enter text.


result_field = Entry(root, textvariable=equation, width=30, )
result_field.grid(columnspan=5, ipadx=70)

# Setting the buttons

button1 = Button(root, text='1', width=10, height=5, command=lambda: click('1'))
button2 = Button(root, text='2', width=10, height=5, command=lambda: click('2'))
button3 = Button(root, text='3', width=10, height=5, command=lambda: click('3'))
button4 = Button(root, text='4', width=10, height=5, command=lambda: click('4'))
button5 = Button(root, text='5', width=10, height=5, command=lambda: click('5'))
button6 = Button(root, text='6', width=10, height=5, command=lambda: click('6'))
button7 = Button(root, text='7', width=10, height=5, command=lambda: click('7'))
button8 = Button(root, text='8', width=10, height=5, command=lambda: click('8'))
button9 = Button(root, text='9', width=10, height=5, command=lambda: click('9'))

button0 = Button(root, text='0', width=10, height=5, command=lambda: click('0'))
clear = Button(root, text='C', width=10, height=5, command=lambda: clear_btn())
equal = Button(root, text='=', width=10, height=5, command=lambda: equal_btn())

plus = Button(root, text='+', width=10, height=5, command=lambda: click('+'))
minus = Button(root, text='-', width=10, height=5, command=lambda: click('-'))
multiply = Button(root, text='*', width=10, height=5, command=lambda: click('*'))
divide = Button(root, text='/', width=10, height=5, command=lambda: click('/'))
decimal = Button(root, text=',', width=10, height=5, command=lambda: click(','))


# Placing the buttons

button1.grid(row=2, column=0)
button2.grid(row=2, column=1)
button3.grid(row=2, column=2)

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)

button7.grid(row=4, column=0)
button8.grid(row=4, column=1)
button9.grid(row=4, column=2)

button0.grid(row=5, column=0)
clear.grid(row=2, column=3)
equal.grid(row=3, column=3)

plus.grid(row=4, column=3)
minus.grid(row=5, column=3)
multiply.grid(row=5, column=2)
divide.grid(row=5, column=1)
decimal.grid(row=6, column=0)

root.mainloop()
