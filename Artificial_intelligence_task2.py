import tkinter as tk
from tkinter import messagebox
import re
import string

faqs = [
    {"question": "What is artificial intelligence?", "answer": "AI is the simulation of human intelligence in machines."},
    {"question": "How does machine learning work?", "answer": "ML uses algorithms to analyze data and learn patterns."},
    {"question": "What is deep learning?", "answer": "Deep learning is a subset of machine learning using neural networks."},
    {"question": "What are applications of AI?", "answer": "AI is used in healthcare, finance, robotics, and more."}
]

def preprocess(text):
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    return set(text.split())


def get_answer(user_question):
    user_text = user_question.lower().strip()

    if user_text in ["hi", "hello", "how are you", "hey"]:
        return "I'm just a bot, but I'm here and ready to help you! 😊"

    user_words = preprocess(user_text)
    max_overlap = 0
    best_answer = "Hmm... I'm not sure about that. Try asking about AI or machine learning!"

    for faq in faqs:
        faq_words = preprocess(faq["question"])
        overlap = len(user_words & faq_words)
        if overlap > max_overlap:
            max_overlap = overlap
            best_answer = faq["answer"]

    return best_answer

def respond():
    user_q = user_entry.get()
    if not user_q.strip():
        messagebox.showwarning("Warning", "Please enter a question.")
        return
    answer = get_answer(user_q)
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"You: {user_q}\nBot: {answer}\n\n")
    chat_log.config(state=tk.DISABLED)
    user_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Friendly FAQ Chatbot")
root.geometry("700x450")

chat_log = tk.Text(root, state=tk.DISABLED, width=90, height=20, wrap=tk.WORD, bg="#f4f4f4")
chat_log.pack(padx=10, pady=10)

user_entry = tk.Entry(root, width=90)
user_entry.pack(padx=10, pady=5)

send_btn = tk.Button(root, text="Ask", command=respond)
send_btn.pack(pady=5)

root.mainloop()

