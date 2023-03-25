import tkinter as tk

def calculate_bmi():
    # Get the height and weight values from the entry fields
    height = float(height_entry.get())
    weight = float(weight_entry.get())

    # Calculate the BMI
    bmi = weight / (height ** 2)

    # Update the text field with the BMI result
    result_text.delete('1.0', tk.END) # Clear any previous result
    result_text.insert(tk.END, f"Your BMI is: {bmi:.2f}")

def validate_number(input):
    try:
        float(input)
        return True
    except ValueError:
        return False

def validate_input():
    if not validate_number(height_entry.get()):
        result_text.delete('1.0', tk.END) # Clear any previous result
        result_text.insert(tk.END, "Invalid height value")
    elif not validate_number(weight_entry.get()):
        result_text.delete('1.0', tk.END) # Clear any previous result
        result_text.insert(tk.END, "Invalid weight value")
    else:
        calculate_bmi()

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create the entry fields for height and weight
height_label = tk.Label(root, text="Enter your height (m): ")
height_label.grid(row=0, column=0)
height_entry = tk.Entry(root)
height_entry.grid(row=0, column=1)

weight_label = tk.Label(root, text="Enter your weight (kg): ")
weight_label.grid(row=1, column=0)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1)

# Create the button to calculate BMI
calculate_button = tk.Button(root, text="Calculate BMI", command=validate_input)
calculate_button.grid(row=2, column=0, columnspan=2)

# Create the text field to display the results
result_text = tk.Text(root, height=2)
result_text.grid(row=3, column=0, columnspan=2)

# Start the event loop
root.mainloop()