import tkinter as tk

def add_numbers():
    try:
        # Get the values from the entry widgets
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        # Perform the addition
        result = num1 + num2

        # Display the result in the label
        result_label.config(text=f"Result: {result}", fg="green")

        # Clear the entry fields
        entry_num1.delete(0, tk.END)
        entry_num2.delete(0, tk.END)

    except ValueError:
        # Handle the case where input is not a valid number
        result_label.config(text="Invalid input. Please enter numbers.", fg="red")

# Creating a main window with increased size
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("500x500")  # Set the size of the window

# Setting a background color
root.configure(bg="#f0f0f0")

# Adding a frame to center the content
frame = tk.Frame(root, bg="#f0f0f0")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Adding entry widgets for input
entry_num1 = tk.Entry(frame, width=10, font=("Arial", 12))
entry_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(frame, width=10, font=("Arial", 12))
entry_num2.grid(row=0, column=1, padx=10, pady=10)

# Styling the button
add_button = tk.Button(frame, text="Add", command=add_numbers, font=("Arial", 12), bg="#4CAF50", fg="white")
add_button.grid(row=1, column=0, columnspan=2, pady=10)

# Adding a label to display the result
result_label = tk.Label(frame, text="Result: ", font=("Arial", 14), bg="#f0f0f0")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Running the main loop
root.mainloop()
