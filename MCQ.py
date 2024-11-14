import tkinter as tk
from tkinter import messagebox
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["Harper Lee", "Mark Twain", "J.K. Rowling", "Ernest Hemingway"],
        "answer": "Harper Lee"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippo"],
        "answer": "Blue Whale"
    },
    {
        "question": "What is the boiling point of water?",
        "options": ["50°C", "75°C", "100°C", "125°C"],
        "answer": "100°C"
    }
]
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MCQ Test")
        self.question_index = 0
        self.score = 0
        self.user_answer = tk.StringVar()

        self.create_widgets()
        self.display_question()
    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", font=('Arial', 14))
        self.question_label.pack(pady=20)
        self.option_buttons = []
        for _ in range(4):
            button = tk.Radiobutton(self.root, text="", variable=self.user_answer, value="", font=('Arial', 12))
            button.pack(anchor="w")
            self.option_buttons.append(button)
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=20)
    def display_question(self):
        question_data = questions[self.question_index]
        self.question_label.config(text=question_data["question"])
        self.user_answer.set(None)

        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].config(text=option, value=option)
    def submit_answer(self):
        selected_answer = self.user_answer.get()
        if selected_answer == questions[self.question_index]["answer"]:
            self.score += 1
        self.question_index += 1
        if self.question_index < len(questions):
            self.display_question()
        else:
            messagebox.showinfo("Result", f"Your score: {self.score}/{len(questions)}")
            self.root.destroy()
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
