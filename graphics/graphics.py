import tkinter as tk

class test_gui:
    def __init__(self, master):
        self.master = master
        self.master.title("test")
        self.text = tk.StringVar()
        self.temp = 1

        self.text.set(str(self.temp))

        self.label = tk.Label(self.master, textvariable=self.text)
        self.label.pack()

        self.button = tk.Button(self.master, text="Button", command=self.change_text)
        self.button.pack()

        self.close = tk.Button(self.master, text="Close", command=self.master.quit)
        self.close.pack()

        self.master.mainloop()

    def change_text(self):
        self.temp += 1
        self.text.set(str(self.temp))


root = tk.Tk()
gui = test_gui(root)

#test