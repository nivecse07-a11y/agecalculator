from tkinter import *
from datetime import date
import itertools

# --- Main window ---
root = Tk()
root.geometry('500x500')
root.resizable(0, 0)
root.title('🌟 Age Calculator 🌟')

# --- Gradient background animation using Canvas ---
canvas = Canvas(root, width=500, height=500, highlightthickness=0)
canvas.pack(fill="both", expand=True)

colors = ["#FFDEE9", "#B5FFFC", "#DAD4EC", "#F3E7E9", "#FEE3BC", "#F8E8EE"]
color_cycle = itertools.cycle(colors)

def animate_bg():
    current_color = next(color_cycle)
    canvas.config(bg=current_color)
    root.after(500, animate_bg)  # change every 500ms

animate_bg()

# --- Frame to hold widgets (on top of Canvas) ---
frame = Frame(canvas, bg="#ffffff", bd=2, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor="center")

# --- Statement label (for results or errors) ---
statement = Label(frame, text="", font=("Arial", 14), bg="white", fg="#333")
statement.grid(row=6, column=0, columnspan=2, pady=20)

# --- Name input ---
Label(frame, text="Name:", font=("Arial", 14), bg="white").grid(row=0, column=0, padx=10, pady=10, sticky=E)
nameValue = StringVar()
Entry(frame, textvariable=nameValue, width=25, font=("Arial", 14), bg="#f0f8ff").grid(row=0, column=1, padx=10, pady=10)

# --- DOB input ---
Label(frame, text="Date:", font=("Arial", 14), bg="white").grid(row=1, column=0, padx=10, pady=10, sticky=E)
dayEntry = Entry(frame, width=25, font=("Arial", 14), bg="#f0f8ff")
dayEntry.grid(row=1, column=1, padx=10, pady=10)

Label(frame, text="Month:", font=("Arial", 14), bg="white").grid(row=2, column=0, padx=10, pady=10, sticky=E)
monthEntry = Entry(frame, width=25, font=("Arial", 14), bg="#f0f8ff")
monthEntry.grid(row=2, column=1, padx=10, pady=10)

Label(frame, text="Year:", font=("Arial", 14), bg="white").grid(row=3, column=0, padx=10, pady=10, sticky=E)
yearEntry = Entry(frame, width=25, font=("Arial", 14), bg="#f0f8ff")
yearEntry.grid(row=3, column=1, padx=10, pady=10)

# --- Function to calculate age ---
def ageCalc():
    statement.config(text="", fg="#333")
    today = date.today()

    try:
        birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    except:
        statement.config(text="❌ Invalid date! Please recheck.", fg="red")
        return

    years = today.year - birthDate.year
    months = today.month - birthDate.month
    days = today.day - birthDate.day

    if days < 0:
        months -= 1
        prev_month = (today.month - 1) or 12
        prev_year = today.year if today.month != 1 else today.year - 1
        days += (date(prev_year, (prev_month + 1 if prev_month < 12 else 1), 1) - date(prev_year, prev_month, 1)).days

    if months < 0:
        months += 12
        years -= 1

    statement.config(
        text=f"🎉 {nameValue.get()} is {years} years, {months} months, and {days} days old!",
        fg="#00796B"
    )

# --- Button to calculate ---
Button(
    frame, text="Calculate Age", command=ageCalc,
    font=("Arial", 14, "bold"), width=18, bg="#4CAF50", fg="white",
    activebackground="#66BB6A", relief="raised", cursor="hand2"
).grid(row=5, column=0, columnspan=2, pady=20)

root.mainloop()
