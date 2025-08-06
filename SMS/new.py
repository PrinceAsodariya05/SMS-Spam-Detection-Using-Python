import tkinter as tk
from tkinter import messagebox, Scrollbar
from PIL import Image, ImageTk
import re

SPAM_KEYWORDS = ["win", "free", "lottery", "cash", "prize", "congratulations", "click", "claim", "urgent", "money"]

is_dark_mode = False

def check_spam():
    message = text_entry.get("1.0", tk.END).strip().lower()
    if any(re.search(rf"\b{word}\b", message) for word in SPAM_KEYWORDS):
        result_label.config(text="🚨 SPAM DETECTED! 🚨", fg="#FF4C4C")
        messagebox.showwarning("Spam Alert", "This message contains spam-related words.")
    else:
        result_label.config(text="✅ Not Spam", fg="#4CAF50")
        messagebox.showinfo("All Clear", "Message is clean.")

def reset_fields():
    text_entry.delete("1.0", tk.END)
    result_label.config(text="")

def toggle_mode():
    global is_dark_mode
    is_dark_mode = not is_dark_mode
    apply_theme()

def apply_theme():
    bg_color = "#1e1e1e" if is_dark_mode else "#ffffff"
    fg_color = "#ffffff" if is_dark_mode else "#000000"
    entry_bg = "#2e2e2e" if is_dark_mode else "#ffffff"
    entry_fg = "#ffffff" if is_dark_mode else "#000000"

    root.config(bg=bg_color)
    title_label.config(bg=bg_color, fg=fg_color)
    subtitle_label.config(bg=bg_color, fg=fg_color)
    text_frame.config(bg=bg_color)
    text_entry.config(bg=entry_bg, fg=entry_fg, insertbackground=entry_fg)
    result_label.config(bg=bg_color, fg=fg_color)
    mode_button.config(bg=bg_color, fg=fg_color, text="☀" if is_dark_mode else "🌙")

root = tk.Tk()
root.title("🚀 SMS Spam Detector")
root.geometry("440x440")
root.resizable(False, False)

try:
    bg_image = Image.open("bg.jpg")
    bg_image = bg_image.resize((440, 440), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
except FileNotFoundError:
    print("bg.jpg not found. Background image skipped.")

mode_button = tk.Button(root, text="🌙", command=toggle_mode, font=("Arial", 10, "bold"),width=3, height=1, relief="solid", bd=1)
mode_button.place(x=400, y=10) 

title_label = tk.Label(root, text="SMS Spam Detector", font=("Helvetica", 18, "bold"), bg="white")
title_label.pack(pady=10)

subtitle_label = tk.Label(root, text="Paste your message below:", font=("Helvetica", 12), bg="white")
subtitle_label.pack(pady=5)

text_frame = tk.Frame(root, bg="white")
text_frame.pack(pady=5)

scrollbar = Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_entry = tk.Text(text_frame, height=6, width=48, yscrollcommand=scrollbar.set, wrap=tk.WORD, bg="white", fg="black")
text_entry.pack(side=tk.LEFT)
scrollbar.config(command=text_entry.yview)

check_button = tk.Button(root, text="Check Message", command=check_spam,bg="#007BFF", fg="white", font=("Arial", 12), width=20)
check_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset", command=reset_fields,bg="#6c757d", fg="white", width=10)
reset_button.pack()

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="white")
result_label.pack(pady=15)

apply_theme()
root.mainloop()