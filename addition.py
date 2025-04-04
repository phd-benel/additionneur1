import tkinter as tk

def addition(a, b):
    return a + b

def calculer():
    a = int(entry1.get())
    b = int(entry2.get())
    resultat.set(str(addition(a, b)))

app = tk.Tk()
app.title("Additionneur")

entry1 = tk.Entry(app)
entry1.pack()

entry2 = tk.Entry(app)
entry2.pack()

resultat = tk.StringVar()
tk.Label(app, textvariable=resultat).pack()

tk.Button(app, text="Calculer", command=calculer).pack()

app.mainloop()
