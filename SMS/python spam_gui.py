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
    bg = "#121212" if is_dark_mode else "#ffffff"
    fg = "#ffffff" if is_dark_mode else "#000000"
    entry_bg = "#1e1e1e" if is_dark_mode else "#ffffff"
    entry_fg = "#ffffff" if is_dark_mode else "#000000"
    button_bg = "#292929" if is_dark_mode else "#f0f0f0"

    overlay.config(bg=bg)
    title_label.config(bg=bg, fg=fg)
    subtitle_label.config(bg=bg, fg=fg)
    result_label.config(bg=bg, fg=fg)
    text_frame.config(bg=bg)
    text_entry.config(bg=entry_bg, fg=entry_fg, insertbackground=entry_fg)
    check_button.config(bg="#007BFF", fg="white", activebackground="#0056b3")
    reset_button.config(bg="#6c757d", fg="white", activebackground="#5a6268")
    mode_button.config(bg=button_bg, fg=fg, text="☀" if is_dark_mode else "🌙")

root = tk.Tk()
root.title("🚀 SMS Spam Detector")
root.geometry("460x460")
root.resizable(False, False)

try:
    bg_image = Image.open("bg.jpg").resize((460, 460), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
except FileNotFoundError:
    print("Background image 'bg.jpg' not found.")

overlay = tk.Frame(root, bg="white")
overlay.place(relwidth=1, relheight=1)

mode_button = tk.Button(overlay, text="🌙", command=toggle_mode, font=("Arial", 10, "bold"), width=3, height=1, relief="flat", bd=1)
mode_button.place(x=420, y=10)

title_label = tk.Label(overlay, text="SMS Spam Detector", font=("Helvetica", 18, "bold"))
title_label.pack(pady=(20, 5))

subtitle_label = tk.Label(overlay, text="Paste your message below:", font=("Helvetica", 12))
subtitle_label.pack(pady=(0, 10))

text_frame = tk.Frame(overlay)
text_frame.pack(pady=5)

scrollbar = Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_entry = tk.Text(text_frame, height=6, width=48, yscrollcommand=scrollbar.set, wrap=tk.WORD)
text_entry.pack(side=tk.LEFT)
scrollbar.config(command=text_entry.yview)

check_button = tk.Button(overlay, text="Check Message", command=check_spam,font=("Arial", 12, "bold"), width=20)
check_button.pack(pady=10)

reset_button = tk.Button(overlay, text="Reset", command=reset_fields,font=("Arial", 10), width=10)
reset_button.pack(pady=2)

result_label = tk.Label(overlay, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=15)

apply_theme()
root.mainloop()
              