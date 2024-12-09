import tkinter as tk
from tkinter import messagebox

# Function to calculate the result based on the entered average
def calculate_result(moy):
    if 0 <= moy < 10:
        return "Retake"
    elif 10 <= moy <= 20:
        return "PASSED"
    else:
        return "Insert average between 0 and 20"

# Function to get the result when the "Calculate" button is clicked
def get_result():
    try:
        moy = float(entry_moy.get())
        result = calculate_result(moy)
        messagebox.showinfo("Result", f"The result is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the moy.")

# Create the main window
root = tk.Tk()
root.title("Average Result Testor")

# Set the size of the window
root.geometry("300x150")

# Calculate the position to center the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - root.winfo_reqwidth()) / 2
y = (screen_height - root.winfo_reqheight()) / 2

# Set the position of the window
root.geometry("+%d+%d" % (x, y))

# Create the interface elements
label_moy = tk.Label(root, text="Moy:", font=("Arial", 14))
label_moy.grid(row=0, column=0, padx=15, pady=5, sticky='w')

entry_moy = tk.Entry(root, font=("Arial", 14), justify='center')
entry_moy.grid(row=1, column=0, padx=45, pady=5)

button_calculate = tk.Button(root, text="test", font=("Arial", 15), command=get_result)
button_calculate.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Start the main loop
root.mainloop()
