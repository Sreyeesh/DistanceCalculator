import tkinter as tk
import tkinter.messagebox


class DistanceConverter:
    def __init__(self, root):
        self.root = root
        root.title("Distance Converter")

        self.root.geometry("400x100")

        self.label1 = tk.Label(text="Kilometers:")
        self.label1.grid(row=0, column=0)

        self.e1_value = tk.StringVar()
        self.entry1 = tk.Entry(textvariable=self.e1_value)
        self.entry1.grid(row=0, column=1)

        self.label2 = tk.Label(text="Miles:")
        self.label2.grid(row=0, column=2)

        self.e2_value = tk.StringVar()
        self.entry2 = tk.Entry(textvariable=self.e2_value)
        self.entry2.grid(row=0, column=3)
        self.entry2.bind("<Return>", self.convert_distance)

        self.e1_value.trace("w", self.convert_kilometers_to_miles)
        self.e2_value.trace("w", self.convert_miles_to_kilometers)

    def convert_miles_to_kilometers(self, *args):
        try:
            miles = float(self.e2_value.get())
            kilometers = miles * 1.60934
            self.e1_value.set(kilometers)
        except ValueError:
            self.e1_value.set("")

    def convert_kilometers_to_miles(self, *args):
        try:
            kilometers = float(self.e1_value.get())
            miles = kilometers / 1.60934
            self.e2_value.set(miles)
        except ValueError:
            self.e2_value.set("")

    def convert_distance(self, *args):
        pass

    def quit_app(self, event=None):
        result = tkinter.messagebox.askyesno("Quit", "Are you sure you want to quit?")
        if result:
            self.root.destroy()


root = tk.Tk()
app = DistanceConverter(root)
root.bind("<Escape>", app.quit_app)
root.mainloop()
