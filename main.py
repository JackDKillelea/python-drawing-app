import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import Image, ImageDraw

class DrawingApp:
    def __init__(self, root):
        # Initialise the drawing app with the given root window and name
        self.root = root
        self.root.title("Jacks Drawing App")

        # Create a canvas to draw on and pack it into the root window
        self.canvas = tk.Canvas(self.root, bg='white', width=800, height=600)
        self.canvas.pack()

        # Set default colour and brush size
        self.color = "black"
        self.brush_size = 5

        # Bind mouse events to the canvas
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)
        self.canvas.bind("<KeyPress-K>", self.terminate_app)

        # Create an image to store the drawing and initialize the draw object with the white background
        self.image = Image.new("RGB", (800, 600), 'white')
        self.draw = ImageDraw.Draw(self.image)

        # Initilise the toolbar
        self.create_toolbar()

    def create_toolbar(self):
        # Create the toolbar
        toolbar = tk.Frame(self.root)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # Set up the colour button
        color_button = tk.Button(toolbar, text='Color', command=self.choose_color)
        color_button.pack(side=tk.LEFT)

        # Set up size label and default size to 5
        size_label = tk.Label(toolbar, text='Size:')
        size_label.pack(side=tk.LEFT)
        self.size_entry = tk.Entry(toolbar, width=5)
        self.size_entry.insert(0, '5')
        self.size_entry.pack(side=tk.LEFT)
        size_button = tk.Button(toolbar, text='Set Size', command=self.set_brush_size)
        size_button.pack(side=tk.LEFT)

        # Set up clear button
        clear_button = tk.Button(toolbar, text='Clear', command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT)

        # Set up save button
        save_button = tk.Button(toolbar, text='Save', command=self.save_image)
        save_button.pack(side=tk.LEFT)

    def choose_color(self):
        self.color = colorchooser.askcolor()[1]

    def set_brush_size(self):
        try:
            # Sets the brush size to the entered value
            self.brush_size = int(self.size_entry.get())
        except ValueError:
            pass

    def paint(self, event):
        # Draws movements to canvas
        x, y = event.x, event.y
        x1 = x - self.brush_size
        y1 = y - self.brush_size
        x2 = x + self.brush_size
        y2 = y + self.brush_size

        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)
        self.draw.ellipse([x1, y1, x2, y2], fill=self.color, outline=self.color)

    def reset(self, event):
        pass

    def clear_canvas(self):
        # Removes everything from the canvas
        self.canvas.delete("all")
        self.image = Image.new("RGB", (800, 600), 'white')
        self.draw = ImageDraw.Draw(self.image)

    def save_image(self):
        # Saves the current canvas as an image file, with the default filename "drawing.png"
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                   filetypes=[("PNG files", "*.png"),
                                                              ("JPEG files", "*.jpg"),
                                                              ("All files", "*.*")],
                                                 initialfile="drawing.png")
        if file_path:
            self.image.save(file_path)

    def terminate_app(self, event):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()