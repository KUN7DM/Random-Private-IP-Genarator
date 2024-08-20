import random
import tkinter as tk
from tkinter import ttk

def Class_A():
    private = ['10', str(random.randint(0,255)),str(random.randint(0,255)),str(random.randint(0,255))]
    result = '.'.join(private)
    Output_Lbl.set(result)

def Class_B():
    private = ["172", str(random.randint(16,31)), str(random.randint(0,255)), str(random.randint(0,255))]
    result = ".".join(private)
    Output_Lbl.set(result)

def Class_C():
    private = ["192", "168", str(random.randint(0,255)), str(random.randint(0,255))]
    result = ".".join(private)
    Output_Lbl.set(result)

window = tk.Tk()
window.geometry('250x150')
window.title('IP Generator')

# Main Label
main_label = ttk.Label(master=window, text='Pick an Option', font='Calibri 12')
main_label.pack()

# Buttons
Frame = ttk.Frame(master=window)
Frame.pack()
A_Button = ttk.Button(master=Frame, text='Class A', command = Class_A)
A_Button.pack(side='left')
B_Button = ttk.Button(master=Frame, text='Class B', command = Class_B)
B_Button.pack(side='left')
C_Button = ttk.Button(master=Frame, text='Class C', command = Class_C)
C_Button.pack(side='left')

# Output
Output_Lbl = tk.StringVar()
Output = ttk.Label(master=window, font='Calibri 24', textvariable=Output_Lbl)
Output.pack(pady=25)

window.mainloop()
