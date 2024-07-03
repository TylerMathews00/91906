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

class PlayWindow:
    def __init__(self, parent):
        self.parent = parent
        self.play_window = Toplevel(self.parent)
        self.play_window.geometry("500x700")
        self.play_window.configure(bg="#90EE90")
        self.num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        self.create_widgets()

    def create_widgets(self):
        self.num1 = random.choice(self.num)
        self.num2 = random.choice(self.num)
        
        self.question_label = Label(self.play_window, text=f"{self.num1} + {self.num2}", font=("Arial", 24))
        self.question_label.place(relx=0.3, rely=0.2)
        
        self.answer_entry = Entry(self.play_window, font=("Arial", 18))
        self.answer_entry.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.1)
        
        submit_button = Button(self.play_window, text="Submit", command=self.submit_answer)
        submit_button.place(relx=0.35, rely=0.55, relwidth=0.34, relheight=0.1)
        
        try_again_button = Button(self.play_window, text="Try Again", command=self.try_again)
        try_again_button.place(relx=0.39, rely=0.7)

    def submit_answer(self):
        answer = self.answer_entry.get()
        if answer.isdigit() and int(answer) == self.num1 + self.num2:
            result_label = Label(self.play_window, text="Correct!", fg="green", font=("Arial", 16))
        else:
            result_label = Label(self.play_window, text="Wrong!", fg="red", font=("Arial", 16))
        result_label.place(relx=0.35, rely=0.85)

    def try_again(self):
        self.num1 = random.choice(self.num)
        self.num2 = random.choice(self.num)
        self.question_label.config(text=f"{self.num1} + {self.num2}")
        self.answer_entry.delete(0, END)


root = Tk()
app = WindowOne(root)
root.mainloop()
        
        
   

root = Tk()
window_one()

mainloop()

