import tkinter as tk
from buff_scraper import pricegrabber
root = tk.Tk()
root.title("Buff Price")
root.geometry('250x150')
id = None

label1 = tk.Label(root, text='Enter your STEAMID64', font=('Arial', 14))
label1.grid(padx=10, pady=10)

data = tk.StringVar()

textbox1 = tk.Entry(root, textvariable=data)
textbox1.grid(padx=20, pady=2)

def idgrabber():
    id = data.get()
    price = pricegrabber(id)
    newWindow = tk.Toplevel(root)
    label2 = tk.Label(newWindow, text = price)
    label2.grid(padx=50, pady=50)
    textbox1.delete(0, tk.END)



button1 = tk.Button(root, text='Enter', command=idgrabber)
button1.grid(padx=20, pady=20)























root.mainloop()