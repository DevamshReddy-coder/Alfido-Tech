import tkinter as tk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def run_command_line_calculator():
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            break

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
        else:
            print("Invalid input")

def run_gui_calculator():
    def on_button_click(value):
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current + value)

    def clear_entry():
        entry.delete(0, tk.END)

    def calculate():
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    
    window = tk.Tk()
    window.title("Calculator")

    
    entry = tk.Entry(window, width=20, borderwidth=5)
    entry.grid(row=0, column=0, columnspan=4)

    
    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
    ]

    
    row_val = 1
    col_val = 0
    for button in buttons:
        tk.Button(window, text=button, padx=20, pady=20, command=lambda b=button: on_button_click(b) if b != '=' else calculate()).grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    
    window.mainloop()

def main():
    print("Choose the calculator type:")
    print("1. Command-Line Calculator")
    print("2. GUI Calculator")

    choice = input("Enter choice (1/2): ")

    if choice == '1':
        run_command_line_calculator()
    elif choice == '2':
        run_gui_calculator()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
