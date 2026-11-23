import tkinter as tk
import ast

# Create main window
root = tk.Tk()

# Window title
root.title("Amina's Calculator")

# Window size
root.geometry("320x450")

# Window background
root.configure(bg="#FFF3E0")


# Create calculator display
display = tk.Entry(
    root,
    font=("Arial", 26,"bold"),
    justify="right",
    bg="#FFFFFF",
    fg="black",
    borderwidth=2
)

display.pack(padx=15, pady=20, fill="x", ipady=10)

# Button click function

def safe_calculate(expression):

    tree = ast.parse(expression, mode="eval")

    def calculate(node):
        if isinstance(node, ast.Expression):
            return calculate(node.body)

        elif isinstance(node, ast.Constant) and type(node.value) in (int, float):
             return node.value

        elif isinstance(node, ast.BinOp):
            left = calculate(node.left)
            right = calculate(node.right)

        if isinstance(node.op, ast.Add):
            return left + right
        elif isinstance(node.op, ast.Sub):
            return left - right
        elif isinstance(node.op, ast.Mult):
            return left * right
        elif isinstance(node.op, ast.Div):
            if right == 0:
                raise ValueError("Cannot divide by zero")
            return left / right

        elif isinstance(node, ast.UnaryOp):
             number = calculate(node.operand)

        if isinstance(node.op, ast.USub):
            return -number
        elif isinstance(node.op, ast.UAdd):
            return number

        raise ValueError("Invalid expression")
    return calculate(tree)
def button_click(value):        
    if value == "C":
        display.delete(0, tk.END)

    elif value == "=":
        try:
            result = safe_calculate(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))

        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")

    else:
        display.insert(tk.END, value)


# Create button frame
button_frame = tk.Frame(root, bg="#FFF3E0")
button_frame.pack(padx=10, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    row_frame = tk.Frame(button_frame, bg="#FFF3E0")
    row_frame.pack()

    for text in row:
        button = tk.Button(
            row_frame,
            text=text,
            font=("Arial", 18),
            width=5,
            height=2,
            bg="#FF8C00",
            activebackground="#FFA500",
            activeforeground="white",
            relief="solid",
            bd=1,
            highlightthickness=0,
            fg="white",
            command=lambda value=text: button_click(value)
        )
        button.pack(side="left", padx=3, pady=3)   
# Run the application
root.mainloop()
