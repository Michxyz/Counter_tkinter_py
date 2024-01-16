import tkinter as tk

class CounterApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.counter_var=int(0)  # Initialize the counter variable
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        #Defining and placing the needed widgets for the app
        self.lbl_counter=tk.Label(self, text="Counter", bg="#e0edcc").grid(row=0, column=0, padx=10, pady=10, ipadx=5, ipady=5)
        self.counter_string=tk.StringVar(value="0") # Initializing the  StringVar with value 0
        self.entry=tk.Entry(self,textvariable=self.counter_string,state="readonly").grid(row=0, column=1, padx=10, pady=10)
        self.btn_increase=tk.Button(self, text="Increase counter", bg="#e0edcc", command=self.increase_counter).grid(row=1, column=0, padx=10, pady=10)
        self.btn_decrease=tk.Button(self, text="Decrease counter", bg="#e0edcc", command=self.decrease_counter).grid(row=1, column=2, padx=10, pady=10)
        self.btn_reset_counter=tk.Button(self, text="Reset counter", bg="#e0edcc", command=self.reset_counter).grid(row=2, column=1, padx=10, pady=10)


    def increase_counter(self):
        #Increase the counter value if the user click on the button 'btn_increase' and place this value on the entry widget
        self.counter_var += 1
        self.counter_string.set(str(self.counter_var))


    def decrease_counter(self):
        #Decrease the counter value if the user click on the button 'btn_decrease' and place this value on the entry widget
        self.counter_var -= 1
        self.counter_string.set(str(self.counter_var))

    def reset_counter(self):
        #Reset the counter value to 0 and place 0 on the entry widget
        self.counter_var = int(0)
        self.counter_string.set(str(self.counter_var))
       


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("620x450")
    root.title("Counter app")
    app = CounterApp(master = root)
    app.mainloop()

