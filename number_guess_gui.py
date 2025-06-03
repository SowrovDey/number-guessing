import tkinter as tk
from tkinter import messagebox
from random import randint

class NumberGuessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎲 Number Guessing Game 🎲")
        self.root.geometry("400x350")
        self.root.configure(bg="#222244")
        self.number = randint(1, 100)
        self.cnt = 0
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Guess the Number!", font=("Arial", 20, "bold"), fg="#FFD700", bg="#222244")
        self.title_label.pack(pady=10)

        self.instruction = tk.Label(self.root, text="Enter a number between 1 and 100", font=("Arial", 12), fg="#00FFCC", bg="#222244")
        self.instruction.pack(pady=5)

        self.entry = tk.Entry(self.root, font=("Arial", 16), width=10, justify='center')
        self.entry.pack(pady=10)
        self.entry.focus()

        self.guess_btn = tk.Button(self.root, text="Guess", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", command=self.check_guess)
        self.guess_btn.pack(pady=5)

        self.feedback = tk.Label(self.root, text="", font=("Arial", 14), bg="#222244")
        self.feedback.pack(pady=10)

        self.missdetect = tk.Label(self.root, text="", font=("Arial", 12), fg="#FF6347", bg="#222244")
        self.missdetect.pack(pady=5)

        self.ringpredict = tk.Label(self.root, text="", font=("Arial", 12), fg="#FFD700", bg="#222244")
        self.ringpredict.pack(pady=5)

        self.counter = tk.Label(self.root, text="Attempts: 0", font=("Arial", 12), fg="#00FFCC", bg="#222244")
        self.counter.pack(pady=5)

        self.reset_btn = tk.Button(self.root, text="New Game", font=("Arial", 12), bg="#2196F3", fg="white", command=self.reset_game)
        self.reset_btn.pack(pady=10)

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            self.feedback.config(text="Please enter a valid number!", fg="#FF6347")
            return
        guess = int(guess)
        self.cnt += 1
        self.counter.config(text=f"Attempts: {self.cnt}")
        diff = abs(guess - self.number)
        if guess == self.number:
            self.feedback.config(text=f"🎉 Correct! You guessed it in {self.cnt} tries!", fg="#00FF00")
            self.missdetect.config(text="")
            self.ringpredict.config(text="")
            messagebox.showinfo("Congratulations!", f"You guessed the number in {self.cnt} attempts!")
        else:
            if guess < self.number:
                self.feedback.config(text="Too Low!", fg="#FF6347")
            else:
                self.feedback.config(text="Too High!", fg="#FF6347")
            self.missdetect.config(text=f"Missed by {diff}")
            if diff <= 5:
                self.ringpredict.config(text="🔥 You're very close! 🔥")
            elif diff <= 10:
                self.ringpredict.config(text="🌟 Getting warmer!")
            else:
                self.ringpredict.config(text="")
        self.entry.delete(0, tk.END)

    def reset_game(self):
        self.number = randint(1, 100)
        self.cnt = 0
        self.counter.config(text="Attempts: 0")
        self.feedback.config(text="", fg="#FFD700")
        self.missdetect.config(text="")
        self.ringpredict.config(text="")
        self.entry.delete(0, tk.END)
        self.entry.focus()

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessApp(root)
    root.mainloop()
