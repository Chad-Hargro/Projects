
import random
import tkinter as tk

def generate_random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return f'#{red:02X}{green:02X}{blue:02X}'  # Convert to hexadecimal format

def generate_random_colors():
    random_colors = [generate_random_color() for _ in range(3)]
    color_labels.config(text=random_colors)
    update_color_squares(random_colors)

def update_color_squares(colors):
    for i in range(3):
        color_squares[i].config(bg=colors[i])

# Create the main window
window = tk.Tk()
window.title("Random Color Generator")
window['bg']='gray'

# Create a button to generate random colors
generate_button = tk.Button(window, text="Three Random Colors", command=generate_random_colors)
generate_button.grid(row=0, column=0, columnspan=3)  # Centered button

# Labels to display the generated colors
color_labels = tk.Label(window, text="", font=("Arial", 12), pady=10)
color_labels.grid(row=1, column=0, columnspan=3)  # Centered labels
color_labels['bg']='gray'
color_labels['fg']='white'

# Create colored squares
color_squares = []
for i in range(3):
    square = tk.Label(window, width=10, height=3, bg="white")
    square.grid(row=2, column=i)  # Centered squares
    color_squares.append(square)

# Start the GUI event loop
window.mainloop()
