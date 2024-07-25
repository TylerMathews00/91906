from tkinter import *
import random

def data_file():
    username_info = self.username_textbox.get()
    age_info = self.age_textbox.get()
    score_info = score.get()
    print(username_info, age_info, score_info)

    file = open("user.txt", "w")
    file.write(username_info)
    file.write(age_info)
    file.write(score_info)
    file.close()
    print(" User: ", username_info, " Age: ", age_info, "Achieved a score of: ", score_info)


    

class WindowOne:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.root.configure(bg="#90EE90")
        self.root.title("Math For Kids")
       
        
        self.create_widgets()

    def create_widgets(self):
        play_button = Button(self.root, text="Play", command=self.open_play_window, height = 3, width= 3)
        play_button.pack()

        exit_button = Button(self.root, text="Exit", command=self.root.destroy)
        exit_button.pack(anchor=W, padx=10)
        
        instructions_button = Button(self.root, text="Instructions", command=self.show_instructions)
        instructions_button.pack(anchor=W, padx=10)
        
        leaderboard_button = Button(self.root, text="Leaderboard", command=self.show_leaderboard)
        leaderboard_button.pack(anchor=W, padx=10)
        
        username_label = Label(self.root, text="Enter Username")
        username_label.pack(anchor=W, padx=10)
        
        self.username_textbox = Entry(self.root)
        self.username_textbox.pack(anchor=W, padx=10)

        age_label = Label(self.root, text="Enter Age")
        age_label.pack(anchor=W, padx=10)
        
        self.age_textbox = Entry(self.root)
        self.age_textbox.pack(anchor=W, padx=10)

        register = Button(self.root, text = "Register", command = data_file, bg= "SpringGreen4")
        register.place(x = 15, y = 350)

    def open_play_window(self):
        PlayWindow(self.root)

    def show_instructions(self):
        instructions = Toplevel(self.root)
        instructions.title("Instructions")
        instructions.geometry("400x300")
        instructions.configure(bg="#90EE90")
        instructions_label = Label(instructions, text="Instructions: Solve the math problems correctly!")
        instructions_label.pack(pady=20)
        
    def show_leaderboard(self):
        leaderboard = Toplevel(self.root)
        leaderboard.title("Leaderboard")
        leaderboard.geometry("400x300")
        leaderboard.configure(bg="#90EE90")
        leaderboard_label = Label(leaderboard, text="Leaderboard")
        leaderboard_label.pack(pady=20)


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

        #score_label = Label(self.play_window, text = "Your Score: " + str(score), bg="powder blue")
        #score_label.place( x = 0, y = -150)



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
