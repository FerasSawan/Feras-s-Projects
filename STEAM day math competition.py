import random
import tkinter as tk
from tkinter import messagebox
from tkinter import font

class MultiplicationQuizGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiplication Quiz")
        self.correct_count = 0
        self.timer_running = False
        self.time_limit = 30
        self.question_label = None
        self.answer_entry = None
        self.start_button = None
        self.timer_label = None
        self.result_label = None

        self.create_widgets()

    def create_widgets(self):
        self.root.geometry("600x500")  # Adjust the window size

        # Create a larger font for labels, entry field, and buttons
        label_font = font.Font(size=16)
        entry_font = font.Font(size=14)
        button_font = font.Font(size=14)

        self.question_label = tk.Label(self.root, text="Press Start to begin the quiz!", font=label_font)
        self.question_label.pack(pady=30)

        self.answer_entry = tk.Entry(self.root, font=entry_font)
        self.answer_entry.pack(pady=20)
        self.answer_entry.bind('<Return>', lambda event: self.check_answer())

        self.start_button = tk.Button(self.root, text="Start", command=self.start_quiz, font=button_font)
        self.start_button.pack(pady=10)

        self.timer_label = tk.Label(self.root, text="Time left: 0", font=label_font)
        self.timer_label.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=label_font)
        self.result_label.pack(pady=10)

    def generate_question(self):
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        return num1, num2

    def ask_question(self):
        num1, num2 = self.generate_question()
        self.current_answer = num1 * num2
        self.question_label.config(text=f"What is {num1} multiplied by {num2}?")
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.focus()

    def check_answer(self):
        user_answer = self.answer_entry.get()
        try:
            user_answer = int(user_answer)
            if user_answer == self.current_answer:
                self.correct_count += 1
                self.result_label.config(text="Correct!", fg="green")
            else:
                self.result_label.config(text="Incorrect!", fg="red")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a valid integer.", fg="red")

        self.root.after(1000, self.ask_question)

    def update_timer(self):
        if self.timer_running and self.time_limit > 0:
            self.time_limit -= 1
            self.timer_label.config(text=f"Time left: {self.time_limit}")
            if self.time_limit == 0:
                self.end_quiz()
        self.root.after(1000, self.update_timer)

    def start_quiz(self):
        self.start_button.config(state=tk.DISABLED)
        self.timer_running = True
        self.update_timer()
        self.ask_question()

    def end_quiz(self):
        self.timer_running = False
        self.answer_entry.config(state=tk.DISABLED)
        messagebox.showinfo("Quiz Ended", f"You answered {self.correct_count} questions correctly in 30 seconds.")
        self.root.quit()

if __name__ == '__main__':
    root = tk.Tk()
    app = MultiplicationQuizGUI(root)
    root.mainloop()
