import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Clicker Game")

window.geometry("800x600")

# Create a label to display the score
score_label = tk.Label(window, text="Coins: 0")
score_label.pack()

# Create a button to increment the score
def increment_score():
    current_score = int(score_label["text"].split(": ")[1])
    new_score = current_score + 1
    score_label["text"] = f"Coins: {new_score}"

increment_button = tk.Button(window, text="Hi, I'm Sandro, click my forhead!", command=increment_score)
increment_button.pack()
increment_button.place(x=0, y=window.winfo_height()//2)
# Run the main event loop
window.mainloop()