from tkinter import *


class window_one:
    def __init__(self):
       
        
        root.geometry("300x400")
        root.configure(bg="#90EE90")

        def exit():
            root.destroy()
      
        
        Play = Button(root, text="Play", command=play_window)
        Play.pack(anchor=W, padx=10)

            
        Exit = Button(root, text="Exit", command=exit) 
        Exit.pack(anchor= W, padx=10)
        
        Instructions = Button(root, text="Instructions", command=window_one)
        Instructions.pack(anchor= W, padx=10)
        
        Leaderboard = Button(root, text="Leaderboard", command=window_one)
        Leaderboard.pack(anchor= W, padx=10)
        
        Username_Label = Label(root, text="Enter Username")
        Username_Label.pack(anchor= W, padx=10)
        Username_textbox = Entry(root)
        Username_textbox.pack(anchor= W, padx=10)

        Age_Label = Label(root, text="Enter Age")
        Age_Label.pack(anchor= W, padx=10)
        Age_textbox = Entry(root)
        Age_textbox.pack(anchor= W, padx=10)

class play_window:
    def __init__(self):

        root.geometry("500x700")
        
        
   

root = Tk()
window_one()

mainloop()

