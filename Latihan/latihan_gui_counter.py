import tkinter as tk
class Counter(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.count_label = tk.Label(self, text="0", font=("Poppins", 48), foreground='#0000FF')
        self.count_label.pack()
        
        self.count_button = tk.Button(self, text="Count", command=self.count_up, width=10)
        self.count_button.pack()
        
        self.reset_button = tk.Button(self, text="Reset", command=self.reset_count, width=10)
        self.reset_button.pack()
        
        self.count = 0
    
    def count_up(self):
        self.count += 1
        self.count_label.config(text=self.count)
    
    def reset_count(self):
        self.count = 0
        self.count_label.config(text=self.count)


window = tk.Tk() #Bikin windownya
window.geometry('200x200') 
counter = Counter(window) # window disini sebagai masternya
window.mainloop()
