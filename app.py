import tkinter as tk

def convert_distance():
    miles = float(e1_value.get()) * 0.621371
    t1.delete("1.0", tk.END)
    t1.insert(tk.END, str(miles))

window = tk.Tk()
window.title("Kilometer to Mile Converter")

l1 = tk.Label(text="Enter Kilometers:")
l1.grid(row=0, column=0)

e1_value = tk.StringVar()
e1 = tk.Entry(textvariable=e1_value)
e1.grid(row=0, column=1)

b1 = tk.Button(text="Convert", command=convert_distance)
b1.grid(row=0, column=2)

t1 = tk.Text(height=1, width=20)
t1.grid(row=1, column=1)

window.mainloop()
