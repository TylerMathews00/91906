from tkinter import *
from tkinter import messagebox
import random

score = 0

def validate_input(char):
    return char.isdigit()

class WindowOne:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.root.configure(bg="#90EE90")
        self.root.title("Math For Kids")

        self.create_widgets()

    def create_widgets(self):
        play_button = Button(self.root, text="Play", command=self.open_play_window, height=3, width=10)
        play_button.place(x=180, y=180)

        exit_button = Button(self.root, text="Exit", command=self.root.destroy)
        exit_button.pack(anchor=W, padx=10, pady=10)

        instructions_button = Button(self.root, text="Instructions", command=self.show_instructions)
        instructions_button.pack(anchor=W, padx=10, pady=10)

        leaderboard_button = Button(self.root, text="Leaderboard", command=self.show_leaderboard)
        leaderboard_button.pack(anchor=W, padx=10, pady=10)

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
    def __init__(self, root):
        self.root = root
        self.play_window = Toplevel(self.root)
        self.play_window.geometry("500x700")
        self.play_window.configure(bg="#90EE90")
        self.num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.create_widgets()
        self.start_timer()

    def create_widgets(self):
        self.num1 = random.choice(self.num)
        self.num2 = random.choice(self.num)

        self.question_label = Label(self.play_window, text=f"{self.num1} + {self.num2}", font=("Arial", 24))
        self.question_label.place(relx=0.3, rely=0.2)

        self.answer_entry = Entry(self.play_window, font=("Arial", 18))
        self.answer_entry.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.1)

        submit_button = Button(self.play_window, text="Submit", command=self.submit_answer)
        submit_button.place(relx=0.35, rely=0.55, relwidth=0.34, relheight=0.1)

        self.score_label = Label(self.play_window, text=f"Your Score: {score}", bg="powder blue")
        self.score_label.place(relx=0.0, rely=0.85)

        # Timer label
        self.timer_label = Label(self.play_window, text="05:00", font=("Arial", 24), bg="light yellow")
        self.timer_label.place(relx=0.4, rely=0.1)

    def start_timer(self):
        self.time_remaining = 120  # 5 minutes in seconds
        self.update_timer()

    def update_timer(self):
        if self.time_remaining > 0:
            minutes = self.time_remaining // 60
            seconds = self.time_remaining % 60
            self.timer_label.config(text=f"{minutes:02}:{seconds:02}")
            self.time_remaining -= 1
            self.play_window.after(1000, self.update_timer)
        else:
            self.end_game()

    def end_game(self):
        messagebox.showinfo("Time's Up", f"Time's up! Your final score is: {score}")
        self.play_window.destroy()
        self.open_registration_window()

    def submit_answer(self):
        global score
        answer = self.answer_entry.get()
        if answer.isdigit() and int(answer) == self.num1 + self.num2:
            result_label = Label(self.play_window, text="Correct!", fg="green", font=("Arial", 16))
            score += 1
        else:
            result_label = Label(self.play_window, text="Wrong!", fg="red", font=("Arial", 16))
        result_label.place(relx=0.35, rely=0.75)
        self.score_label.config(text=f"Your Score: {score}")
        
        # Clear the answer entry
        self.answer_entry.delete(0, END)
        
        # Generate a new question
        self.num1 = random.choice(self.num)
        self.num2 = random.choice(self.num)
        self.question_label.config(text=f"{self.num1} + {self.num2}")

    def open_registration_window(self):
        RegistrationWindow(self.root)

class RegistrationWindow:
    def __init__(self, root):
        self.root = root
        self.registration_window = Toplevel(self.root)
        self.registration_window.geometry("400x300")
        self.registration_window.configure(bg="#90EE90")
        self.registration_window.title("Register Your Score")

        self.create_widgets()

    def create_widgets(self):
        username_label = Label(self.registration_window, text="Enter Username")
        username_label.pack(pady=10)

        self.username_textbox = Entry(self.registration_window)
        self.username_textbox.pack(pady=5)

        age_label = Label(self.registration_window, text="Enter Age")
        age_label.pack(pady=10)

        self.age_textbox = Entry(self.registration_window, validate="key")
        self.age_textbox['validatecommand'] = (self.registration_window.register(validate_input), '%S')
        self.age_textbox.pack(pady=5)

        register_button = Button(self.registration_window, text="Register", command=self.data_file, bg="SpringGreen4")
        register_button.pack(pady=20)

    def data_file(self):
        username_info = self.username_textbox.get()
        age_info = self.age_textbox.get()
        score_info = score
        if not username_info:
            messagebox.showerror("Input Error", "Username cannot be empty.")
            return

        if not age_info.isdigit() or not (5 <= int(age_info) <= 100):
            messagebox.showerror("Input Error", "Please enter a valid age input bewtween 5-100")
            return

        with open("score.txt", "w") as file:
            file.write(f"Username: {username_info}\n")
            file.write(f"Age: {age_info}\n")
            file.write(f"Score: {score_info}\n")
        messagebox.showinfo("Success", f"Data saved successfully!\nUser: {username_info}, Age: {age_info}, Score: {score_info}")
        self.registration_window.destroy()

root = Tk()
app = WindowOne(root)
root.mainloop()

