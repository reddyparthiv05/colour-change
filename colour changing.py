import tkinter as tk
from tkmacosx import Button
def blue():
    root.config(bg='blue')
def red():
    root.config(bg='red')
def green():
    root.config(bg='green')
def pink():
    root.config(bg='pink')
root=tk.Tk()
root.title('simple caluculator')
root.geometry('1000x1000')
button1=tk.Button(root,text='blue',bg='blue',fg='black',command=blue)
button1.place(x=100,y=200)
button2=tk.Button(root,text='red',bg='red',fg='black',command=red)
button2.place(x=200,y=200)
button3=tk.Button(root,text='green',bg='green',fg='black',command=green)
button3.place(x=300,y=200)
button4=tk.Button(root,text='pink',bg='pink',fg='black',command=pink)
button4.place(x=400,y=200)
root.mainloop()