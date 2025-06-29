import tkinter as tk
from tkinter import ttk, messagebox
from bmi_app.bmi_logic import calculate_bmi, classify_bmi
from bmi_app.storage import save_bmi_record, get_user_history
from bmi_app.plotter import show_bmi_graph

def run_app():
    root = tk.Tk()
    root.title("Advanced BMI Calculator")
    root.geometry("480x400")
    root.configure(bg="#1e1e1e")  # Dark glassy background
    root.resizable(False, False)

    # Style setup
    style = ttk.Style()
    style.theme_use("clam")

    style.configure("TFrame", background="#1e1e1e")
    style.configure("TLabel", background="#1e1e1e", foreground="#f5f5f5", font=("Segoe UI", 10))
    style.configure("TEntry", fieldbackground="#2e2e2e", foreground="#ffffff", padding=5)
    style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)

    # Main frame
    frame = ttk.Frame(root, padding="30 30 30 20", style="TFrame")
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Labels
    ttk.Label(frame, text="Name:").grid(row=0, column=0, sticky="w", pady=5)
    ttk.Label(frame, text="Weight (kg):").grid(row=1, column=0, sticky="w", pady=5)
    ttk.Label(frame, text="Height (m):").grid(row=2, column=0, sticky="w", pady=5)

    # Entry Fields
    name_entry = ttk.Entry(frame, width=30)
    weight_entry = ttk.Entry(frame, width=30)
    height_entry = ttk.Entry(frame, width=30)

    name_entry.grid(row=0, column=1, pady=5)
    weight_entry.grid(row=1, column=1, pady=5)
    height_entry.grid(row=2, column=1, pady=5)

    # Result label
    result_label = ttk.Label(frame, text="", font=("Segoe UI", 10, "bold"))
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    # Calculate and Save function
    def calculate_and_save():
        name = name_entry.get().strip()
        try:
            weight = float(weight_entry.get())
            height = float(height_entry.get())/100

            if not name:
                raise ValueError("Name is required.")
            if weight <= 0 or height <= 0:
                raise ValueError("Weight and height must be positive values.")

            bmi = calculate_bmi(weight, height)
            category = classify_bmi(bmi)
            result_label.config(
                text=f"Your BMI: {bmi:.2f} ({category})", foreground="#00FFAB"
            )
            save_bmi_record(name, weight, height, bmi, category)

        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    # View History function
    def view_history():
        name = name_entry.get().strip()
        if not name:
            messagebox.showwarning("Missing Name", "Please enter your name to view history.")
            return

        user_df = get_user_history(name)
        if user_df is None or user_df.empty:
            messagebox.showinfo("No Data", f"No history found for {name}.")
        else:
            show_bmi_graph(user_df, name)

    # Buttons
    calc_btn = ttk.Button(frame, text="Calculate & Save", command=calculate_and_save)
    calc_btn.grid(row=4, column=0, columnspan=2, pady=10)

    view_btn = ttk.Button(frame, text="View BMI History", command=view_history)
    view_btn.grid(row=5, column=0, columnspan=2, pady=5)

    root.mainloop()
