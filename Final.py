# Date: 29/08/2024
# Author: Tyler Mathews
# Purpose: To create a math game so children can improve their math skills
# Target Audience: Children or adults


from tkinter import * # Import GUI
from tkinter import messagebox # Import Messagebox
import random # Import Randomizer
import os # Import os

def validate_input(value): # Validate the input for negative values
    if value == "" or value == "-" or value.isdigit() or (value[0] == '-' and value[1:].isdigit()):
        return True
    return False

class Window_one:  # Create the first window
    def __init__(self, root):
        self.root = root  # Opens Tk()
        self.root.geometry("600x600")  # Creates the geometry
        self.root.configure(bg="#87CEEB") # Make the background colour light blue
        self.root.title("Math For Kids") # Title of the window

        self.create_widgets()

    def create_widgets(self): # Function for widgets
        plays_button = Button(self.root, text="Play", command=self.open_play_window, height=3, width=15, # Commands to open the button 
                             font=('Arial', 15, 'bold'), fg="black") # Buttons to open the game window
        plays_button.grid(row=0, column=0, padx=20, pady=20, columnspan=2, sticky="nsew") # Play placements 

        instructions_button = Button(self.root, text="Instructions", command=self.show_instructions, # Commands the program open the instructions
                                     height=3, width=10, fg="black") # Buttons to open the instructions window
        instructions_button.grid(row=1, column=0, padx=20, pady=20, sticky="nsew") # The buttons grids rows 

        leaderboards_button = Button(self.root, text="Leaderboard", command=self.show_leaderboard, # Commands the program to open the leaderboard
                                    height=3, width=10, fg="black") # Buttons to open the leaderboard window 
        leaderboards_button.grid(row=1, column=1, padx=20, pady=20, sticky="nsew") # Leaderboards placement on the window screen 

        exits_button = Button(self.root, text="Exit", command=self.root.destroy, height=3, width=15, # Commands the program to exit the program
                              fg="SpringGreen4") # Buttons to exit the program
        exits_button.grid(row=2, column=0, padx=20, pady=20, columnspan=2, sticky="nsew") # Exit buttons placement 
        
        self.root.grid_columnconfigure(0, weight=1) # The Configurations of grids rows numbers 0
        self.root.grid_columnconfigure(1, weight=1) # Configure the grids rows number 1
        self.root.grid_rowconfigure(0, weight=1) # Grid rows number one
        self.root.grid_rowconfigure(1, weight=1) # Grid rows number 2
        self.root.grid_rowconfigure(2, weight=1) # Grid rows number 3
        
        

    def open_play_window(self): # Open the game window from play button
        game_window(self.root)

    def show_instructions(tk): # Instructions window
        instructions = Toplevel(tk.root) # Open the Instructions window
        instructions.title("Instructions Manual") # Title for window
        instructions.geometry("400x400") # Change the geometry
        instructions.configure(bg="#87CEEA") # Background colour to light blue
        instructions_label = Label(instructions, text="Answer questions within a time limit press Play to begin",
                                   font=("Arial", 12), bg="#87CEEA")
        instructions_label.pack(pady=10) # Change label postion

    def show_leaderboard(self): # Leaderboards windows
        self.leaderboard_window = Toplevel(self.root) # Open the windows
        self.leaderboard_window.title("Leaderboard of all scores") # Change the title of the windows
        self.leaderboard_window.geometry("400x600") # Change the geometrys
        self.leaderboard_window.configure(bg = "#87CEEB") # Change background colour to light blues

        leaderboard_label = Label(self.leaderboard_window, text="Leaderboard", font=("Arial", 16), bg = "#87CEEA") # Labels the leaderboard
        leaderboard_label.pack(pady = 10) # Placement of leaderboards label

        try:
            with open("score.txt", "r") as file: # Open file for data
                scores = file.read()
        except FileNotFoundError:
            scores = "No scores available."

        clear_button = Button(self.leaderboard_window, text="Clear Leaderboard", command=self.clear_leaderboard, bg="#FF4500", fg="SpringGreen4") # Creates button to clear the leaderboards
        clear_button.pack(pady=10) # Set postion

    def clear_leaderboard(self): # Function to clear leaderboards
        with open("score.txt", "w") as file: # Open file for datas
            file.write("") 

        self.leaderboard_label.config(text="no scores available") # Shows the user that no scores are available
        messagebox.showinfo("leaderboard cleared", "Every score have been cleared") # Give message to the user


class game_window: # Game window
    def __init__(self, root): 
        self.root = root
        self.play_window = Toplevel(self.root) # Open the game window
        self.play_window.geometry("700x400") # Change the geometry
        self.play_window.configure(bg="#FFDEAD") # Change the background colour to orange

        self.num = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 0] # List all possible numbers the user may encounter
        self.operations = ['+', '-', '*', '/'] # Random signs for the user to come across
        self.question_count = 0 # Starting question count
        self.max_questions = 10 # Question limit
        self.score = 0  # Start score here

        self.create_widgets()
        self.start_timer()

    def create_widgets(self): # Widgets for game window
        self.generate_question() # generate questions

        self.question_label = Label(self.play_window, text=self.question_text, font=("Arial", 24), bg="#FFDEAD") # Questions label to support the user 
        self.question_label.grid(row=0, column=0, columnspan=3, pady=20) # Place the question label in a nice spot

        vcmd = (self.play_window.register(validate_input), '%P') # Validates input
        self.answer_entry = Entry(self.play_window, font=("Arial", 18), validate="key", validatecommand=vcmd) # Create the answer entry box for the user to add an input entry
        self.answer_entry.grid(row=1, column=1, padx=10, pady=20) # Place the answer entry in the program which is reasonable

        submit_button = Button(self.play_window, text="Submit", command=self.submit_answer, height=2, width=4, 
                                fg="hot pink") # Create the submit button
        submit_button.grid(row=2, column=1, padx=10, pady=20)

        self.score_label = Label(self.play_window, text=f"Your Score: {self.score}", bg="#FFDEAD", font=("Arial", 18)) # Score label 
        self.score_label.grid(row=3, column=0, columnspan=3, pady=20) 

        self.timer_label = Label(self.play_window, text="02:00", font=("Arial", 24), bg="#FF6347", fg="white") # Timer label
        self.timer_label.grid(row=0, column=2, pady=10, padx=20)

        self.question_count_label = Label(self.play_window, text=f"Question: {self.question_count + 1}/{self.max_questions}", font=("Arial", 14), bg="#FFDEAD") # Question label
        self.question_count_label.grid(row=1, column=0, padx=20, pady=10)


    def start_timer(self): # Function to start the timer
        self.time_remaining = 120 # Time until game ends (2min)
        self.update_timer() 

    def update_timer(self): # Function to update the timer
        if self.time_remaining > 0:
            minutes = self.time_remaining // 60
            seconds = self.time_remaining % 60
            self.timer_label.config(text=f"{minutes:02}:{seconds:02}")
            self.time_remaining -= 1
            self.play_window.after(1000, self.update_timer)
        else:
            self.end_game() # If timer is 0 game ends

    def generate_question(self): # Function to generate questions
        self.num1 = random.choice(self.num) # Random first number
        self.num2 = random.choice(self.num) # Random second number
        self.operation = random.choice(self.operations) # Random sign

        if self.operation == '/':
            self.num1 *= self.num2 # If division 

        self.question_text = f"{self.num1} {self.operation} {self.num2}" # Text for the questions
        self.correct_answer = eval(self.question_text) # To make sure the answers are correct

    def end_game(self): # Function to end the game 
        messagebox.showinfo("Time's Up", f"Time's up! Your final score is: {self.score}") # Message box letting the user know the game has ended
        self.play_window.destroy() # Destroys the window
        self.open_registration_window() # Opens the regristration window

    def submit_answer(self): # Function for the submit answer
        answer = self.answer_entry.get() 

        if answer == "":
            messagebox.showerror("Input Error", "Please enter an answer.") # Error message for blank input
            return
        
        try:
            answer = int(answer)

            if answer == self.correct_answer:
                result_label = Label(self.play_window, text="Correct!", fg="green", font=("Arial", 16), bg="#FFDEAD") # Tell the user they are correct
                self.score += 1
            else:
                result_label = Label(self.play_window, text="Wrong!", fg="red", font=("Arial", 16), bg="#FFDEAD") # Tell the user they are incorrect

            result_label.grid(row=4, column=0, columnspan=3, pady=20)
            self.score_label.config(text=f"Your Score: {self.score}")
            
            self.question_count += 1 # Add question number
            self.question_count_label.config(text=f"Question: {self.question_count + 1}/{self.max_questions}")

            if self.question_count < self.max_questions:
                self.answer_entry.delete(0, END)
                self.generate_question()
                self.question_label.config(text=self.question_text)
            else:
                self.end_game() # Ends the game

        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.") # Message box for invalid input

    def open_registration_window(self): # Function to open the regristration window
        registration_window(self.root, self.score)

class registration_window: # Registration window
    def __init__(self, root, score):
        self.root = root
        self.registration_window = Toplevel(self.root) # Opens the regristration window
        self.registration_window.geometry("400x300") # Set the size of the window
        self.registration_window.configure(bg="#87CEEB") # Change background colour to light blue
        self.registration_window.title("Register Your Score") # Change the title

        self.score = score
        self.create_widgets() 

    def create_widgets(self): # Function to create the widgets
        username_label = Label(self.registration_window, text="Enter Username", font=("Arial", 12), bg="#87CEEB") # Username label
        username_label.grid(row=0, column=0, padx=20, pady=10)

        self.username_textbox = Entry(self.registration_window) # Create the username textbox
        self.username_textbox.grid(row=0, column=1, padx=20, pady=10)

        age_label = Label(self.registration_window, text="Enter Age", font=("Arial", 12), bg="#87CEEB") # Create the age label
        age_label.grid(row=1, column=0, padx=20, pady=10)

        self.age_textbox = Entry(self.registration_window, validate="key") # Age text box
        self.age_textbox['validatecommand'] = (self.registration_window.register(validate_input), '%S') # Validate the input for the age textbox
        self.age_textbox.grid(row=1, column=1, padx=20, pady=10)

        register_button = Button(self.registration_window, text="Register", command=self.data_file, bg="#32CD32", fg="SpringGreen4") # Create the registration button
        register_button.grid(row=2, column=0, columnspan=2, pady=20)

    def data_file(self): # Function for the data file
        username_info = self.username_textbox.get()
        age_info = self.age_textbox.get()
        score_info = self.score

        if not username_info.isalpha():
            messagebox.showerror("Input Error", "Username cannot be empty, and must contain letters .") # Create the error message for invalid entries
            return

        if not age_info.isdigit() or not (5 <= int(age_info) <= 100): 
            messagebox.showerror("Input Error", "Please enter a valid age input between 5-100.") # Create error message for boundary limits
            return

        with open("score.txt", "a") as file: # Save the information to a data file
            file.write(f"Username: {username_info}\n") # Save the informations for the users name
            file.write(f"Age: {age_info}\n") # Save informations of the age of the user
            file.write(f"Score: {score_info}\n") # Save the score of users information
            file.write("-" * 20 + "\n")

        messagebox.showinfo("Success", f"data saved successfully\nUser: {username_info}, Age: {age_info}, Score: {score_info}") # Message box telling the user their details
        self.registration_window.destroy() # Destroys the registration window

root = Tk()
app = Window_one(root)
root.mainloop()
