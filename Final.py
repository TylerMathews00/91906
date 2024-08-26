from tkinter import *
from tkinter import messagebox
import random

def validate_input(current_value):
    if current_value == "" or current_value == "-" or current_value.isdigit() or (current_value[0] == '-' and current_value[1:].isdigit()):
        return True
    return False

class WindowOne:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.root.configure(bg="#87CEEB")
        self.root.title("Math For Kids")

        self.create_widgets()

    def create_widgets(self):
        play_button = Button(self.root, text="Play", command=self.open_play_window, height=3, width=15,
                             font=('Arial', 15, 'bold'), bg="#FFA07A", fg="black")
        play_button.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

        exit_button = Button(self.root, text="Exit", command=self.root.destroy, height=3, width=10, bg="#FF6347", fg="SpringGreen4")
        exit_button.grid(row=3, column=1, padx=20, pady=20)

        instructions_button = Button(self.root, text="Instructions", command=self.show_instructions,
                                     height=3, width=10, bg="#FFD700", fg="black")
        instructions_button.grid(row=3, column=0, padx=20, pady=20)

        leaderboard_button = Button(self.root, text="Leaderboard", command=self.show_leaderboard,
                                    height=3, width=10, bg="#98FB98", fg="black")
        leaderboard_button.grid(row=2, column=0, columnspan=2, pady=20)

    def open_play_window(self):
        PlayWindow(self.root)

    def show_instructions(self):
        instructions = Toplevel(self.root)
        instructions.title("Instructions")
        instructions.geometry("400x300")
        instructions.configure(bg="#87CEEB")
        instructions_label = Label(instructions, text="Instructions: Solve math problems within the time limit.", font=("Arial", 12), bg="#87CEEB")
        instructions_label.pack(pady=20)

    def show_leaderboard(self):
        self.leaderboard_window = Toplevel(self.root)
        self.leaderboard_window.title("Leaderboard")
        self.leaderboard_window.geometry("600x400")
        self.leaderboard_window.configure(bg="#87CEEB")

        leaderboard_label = Label(self.leaderboard_window, text="Leaderboard", font=("Arial", 16), bg="#87CEEB")
        leaderboard_label.pack(pady=20)

        try:
            with open("score.txt", "r") as file:
                scores = file.read()
        except FileNotFoundError:
            scores = "No scores available."

        self.leaderboard_label = Label(self.leaderboard_window, text=scores, font=("Arial", 12), bg="#87CEEB")
        self.leaderboard_label.pack(pady=10)

        clear_button = Button(self.leaderboard_window, text="Clear Leaderboard", command=self.clear_leaderboard, bg="#FF4500", fg="SpringGreen4")
        clear_button.pack(pady=20)

    def clear_leaderboard(self):
        with open("score.txt", "w") as file:
            file.write("")
        
        self.leaderboard_label.config(text="No scores available.")
        messagebox.showinfo("Leaderboard Cleared", "All scores have been cleared!")

class PlayWindow:
    def __init__(self, root):
        self.root = root
        self.play_window = Toplevel(self.root)
        self.play_window.geometry("500x700")
        self.play_window.configure(bg="#FFDEAD")

        self.num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.operations = ['+', '-', '*', '/']
        self.question_count = 0
        self.max_questions = 10
        self.score = 0  # Initialize score here

        self.create_widgets()
        self.start_timer()

    def create_widgets(self):
        self.generate_question()

        self.question_label = Label(self.play_window, text=self.question_text, font=("Arial", 24), bg="#FFDEAD")
        self.question_label.grid(row=0, column=0, columnspan=3, pady=20)

        vcmd = (self.play_window.register(validate_input), '%P')
        self.answer_entry = Entry(self.play_window, font=("Arial", 18), validate="key", validatecommand=vcmd)
        self.answer_entry.grid(row=1, column=1, padx=10, pady=20)

        submit_button = Button(self.play_window, text="Submit", command=self.submit_answer, bg="#90EE90", fg="black")
        submit_button.grid(row=2, column=1, padx=10, pady=20)

        self.score_label = Label(self.play_window, text=f"Your Score: {self.score}", bg="#FFDEAD", font=("Arial", 18))
        self.score_label.grid(row=3, column=0, columnspan=3, pady=20)

        self.timer_label = Label(self.play_window, text="02:00", font=("Arial", 24), bg="#FF6347", fg="white")
        self.timer_label.grid(row=0, column=2, pady=10, padx=20)

        self.question_count_label = Label(self.play_window, text=f"Question: {self.question_count + 1}/{self.max_questions}", font=("Arial", 14), bg="#FFDEAD")
        self.question_count_label.grid(row=1, column=0, padx=20, pady=10)

    def start_timer(self):
        self.time_remaining = 120
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

    def generate_question(self):
        self.num1 = random.choice(self.num)
        self.num2 = random.choice(self.num)
        self.operation = random.choice(self.operations)

        if self.operation == '/':
            self.num1 *= self.num2

        self.question_text = f"{self.num1} {self.operation} {self.num2}"
        self.correct_answer = eval(self.question_text)

    def end_game(self):
        messagebox.showinfo("Time's Up", f"Time's up! Your final score is: {self.score}")
        self.play_window.destroy()
        self.open_registration_window()

    def submit_answer(self):
        answer = self.answer_entry.get()

        if answer == "":
            messagebox.showerror("Input Error", "Please enter an answer.")
            return
        
        try:
            answer = int(answer)

            if answer == self.correct_answer:
                result_label = Label(self.play_window, text="Correct!", fg="green", font=("Arial", 16), bg="#FFDEAD")
                self.score += 1
            else:
                result_label = Label(self.play_window, text="Wrong!", fg="red", font=("Arial", 16), bg="#FFDEAD")

            result_label.grid(row=4, column=0, columnspan=3, pady=20)
            self.score_label.config(text=f"Your Score: {self.score}")
            
            self.question_count += 1
            self.question_count_label.config(text=f"Question: {self.question_count + 1}/{self.max_questions}")

            if self.question_count < self.max_questions:
                self.answer_entry.delete(0, END)
                self.generate_question()
                self.question_label.config(text=self.question_text)
            else:
                self.end_game()

        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")

    def open_registration_window(self):
        RegistrationWindow(self.root, self.score)

class RegistrationWindow:
    def __init__(self, root, score):
        self.root = root
        self.registration_window = Toplevel(self.root)
        self.registration_window.geometry("400x300")
        self.registration_window.configure(bg="#87CEEB")
        self.registration_window.title("Register Your Score")

        self.score = score
        self.create_widgets()

    def create_widgets(self):
        username_label = Label(self.registration_window, text="Enter Username", font=("Arial", 12), bg="#87CEEB")
        username_label.grid(row=0, column=0, padx=20, pady=10)

        self.username_textbox = Entry(self.registration_window)
        self.username_textbox.grid(row=0, column=1, padx=20, pady=10)

        age_label = Label(self.registration_window, text="Enter Age", font=("Arial", 12), bg="#87CEEB")
        age_label.grid(row=1, column=0, padx=20, pady=10)

        self.age_textbox = Entry(self.registration_window, validate="key")
        self.age_textbox['validatecommand'] = (self.registration_window.register(validate_input), '%S')
        self.age_textbox.grid(row=1, column=1, padx=20, pady=10)

        register_button = Button(self.registration_window, text="Register", command=self.data_file, bg="#32CD32", fg="SpringGreen4")
        register_button.grid(row=2, column=0, columnspan=2, pady=20)

    def data_file(self):
        username_info = self.username_textbox.get()
        age_info = self.age_textbox.get()
        score_info = self.score

        if not username_info.isalpha():
            messagebox.showerror("Input Error", "Username cannot be empty, and must contain letters .")
            return

        if not age_info.isdigit() or not (5 <= int(age_info) <= 100):
            messagebox.showerror("Input Error", "Please enter a valid age input between 5-100.")
            return

        with open("score.txt", "a") as file:
            file.write(f"Username: {username_info}\n")
            file.write(f"Age: {age_info}\n")
            file.write(f"Score: {score_info}\n")
            file.write("-" * 20 + "\n")

        messagebox.showinfo("Success", f"Data saved successfully!\nUser: {username_info}, Age: {age_info}, Score: {score_info}")
        self.registration_window.destroy()

root = Tk()
app = WindowOne(root)
root.mainloop()
