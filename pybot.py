import random as rd
from datetime import datetime
from zoneinfo import ZoneInfo
import tkinter as tk
from tkinter import scrolledtext


def time_greeting():
    tz_india = ZoneInfo('Asia/Kolkata')
    current_time = datetime.now(tz_india)
    hour = current_time.hour

    if 12 <= hour <= 18:
        return "Good Afternoon"
    elif 0 <= hour < 12:
        return "Good Morning"
    else:
        return "Good Evening"


def bot_response(user):
    user = user.lower()

    if user in ["hi", "hello", "hey"]:
        greeting = (
            "Hey there!",
            "Hello",
            "Hello, this is PyBot",
            "Hi, I'm PyBot. I will help you with Python doubts"
        )
        return rd.choice(greeting)

    elif user in ["what is python", "what is python?"]:
        return (
            "Python is a popular, high-level programming language. "
            "It is easy to read, free, open-source, and widely used."
        )

    elif user in [
        "what is variable", "variable?",
        "what is variable in python", "what is variable in python?"
    ]:
        return (
            "A variable is a container used to store data in memory.\n"
            "Example:\n"
            "city = 'New York'\n"
            "population = 8419000"
        )

    elif user in ["what is function", "what is function?"]:
        return (
            "A function is a block of code that runs when called.\n"
            "Example:\n"
            "def fun():\n"
            "    print('Hello from a function')"
        )

    elif user in ["what is syntax", "what is syntax?"]:
        return (
            "Syntax refers to the rules of writing code.\n"
            "Example:\n"
            "print('Hello World')"
        )

    else:
        return "Sorry, I don't understand that yet."


def send_message(event=None):
    user_msg = user_entry.get()
    if user_msg.strip() == "":
        return

    chat_box.insert(tk.END, f"You: {user_msg}\n")
    response = bot_response(user_msg)
    chat_box.insert(tk.END, f"PyBot: {response}\n\n")

    user_entry.delete(0, tk.END)
    chat_box.yview(tk.END)


window = tk.Tk()
window.title("PyBot")
window.geometry("500x500")

chat_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Arial", 11))
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_box.insert(tk.END, f"PyBot: {time_greeting()}\n")
chat_box.insert(tk.END, "PyBot: Hi! Ask me anything about Python\n\n")

user_entry = tk.Entry(window, font=("Arial", 12))
user_entry.pack(padx=10, pady=5, fill=tk.X)

send_btn = tk.Button(window, text="Send", command=send_message)
send_btn.pack(pady=5)

window.bind('<Return>', send_message)

window.mainloop()
