import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        interest_rate = float(interest_rate_entry.get())
        balance = float(balance_entry.get())
        months = int(months_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
        return

    result_text.delete(1.0, tk.END)  # Clear previous results
    result_text.insert(tk.END, f"Initial Balance: ${balance:.2f}\n")
    result_text.insert(tk.END, f"Annual Interest Rate: {interest_rate}%\n")
    
    total_interest = 0
    new_balance = balance

    for x in range(1, months + 1):
        monthly_interest = new_balance * (interest_rate / 100) / 12
        new_balance += monthly_interest
        total_interest += monthly_interest
    #    result_text.insert(tk.END, f"After {x} month(s): ${new_balance:.2f}\n")  
    result_text.insert(tk.END, f"\nTOTAL INTEREST: ${total_interest:.2f}\n\n")
    # total
    ttotal = total_interest + balance
    result_text.insert(tk.END, f"TOTAL AMOUNT: ${ttotal:.2f}")

# Setting up the GUI window
window = tk.Tk()
window.title("Monthly Compound Interest Calculator")

# Labels and Entry fields
tk.Label(window, text="Annual Prime Rate (%)").grid(row=0, column=0, padx=10, pady=5)
interest_rate_entry = tk.Entry(window)
interest_rate_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Initial Balance ($)").grid(row=1, column=0, padx=10, pady=5)
balance_entry = tk.Entry(window)
balance_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Number of Months").grid(row=2, column=0, padx=10, pady=5)
months_entry = tk.Entry(window)
months_entry.grid(row=2, column=1, padx=10, pady=5)

# Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_interest)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Text area to display the results
result_text = tk.Text(window, height=15, width=40)
result_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()
