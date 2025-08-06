import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
SPAM_KEYWORDS = ["win", "free", "lottery", "cash", "prize", "congratulations", "click", "claim", "urgent", "money"]

def check_spam():
    """Check if the entered message is spam based on keywords"""
    message = text_entry.get("1.0", tk.END).strip().lower()
    
    if any(word in message for word in SPAM_KEYWORDS):
        result_label.config(text="🚨 SPAM DETECTED! 🚨", fg="red")
    else:
        result_label.config(text="✅ Not Spam", fg="green")

root = tk.Tk()
root.title("SMS Spam Detector")
root.geometry("400x300")
root.resizable(False, False)

bg_image = Image.open("bg.jpg")  
bg_image = bg_image.resize((400, 300), Image.LANCZOS)  
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  

title_label = tk.Label(root, text="SMS Spam Detector", font=("Arial", 16, "bold"))
title_label.pack(pady=10)                          

title_label = tk.Label(root, text="Paste Your MSG Here", font=("bold"))
title_label.pack(pady=8)

text_entry = tk.Text(root, height=5, width=40)
text_entry.pack(pady=10)

check_button = tk.Button(root, text="Check Message", command=check_spam, bg="blue", fg="white", font=("Arial", 12))
check_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#ffffff")
result_label.pack(pady=10)

root.mainloop()