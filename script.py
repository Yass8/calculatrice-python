import customtkinter

class Calculator(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("300x470")
        self.resizable(False, False)

        self.grid_rowconfigure((0, 1), weight=1)  # configure grid system
        self.grid_columnconfigure((0, 1), weight=1)

        self.result_box = customtkinter.CTkTextbox(master=self, height=60, width=220)
        self.result_box.configure(state="disabled")
        self.result_box.grid(row=0, column=0,padx=5, sticky="w")

        self.button = customtkinter.CTkButton(self, text="C", fg_color= "#be4d25", width=60, height=60, command=lambda: self.button_callback("C"))
        self.button.grid(row=0, column=1, padx=5, sticky="e")

        self.button_del = customtkinter.CTkButton(self, text="DEL", fg_color= "#be4d25", width=60, height=60, command=lambda: self.button_callback("DEL"))
        self.button_del.grid(row=1, column=1, padx=5, pady=5, sticky="nw")
        
        self.button_division = customtkinter.CTkButton(self, text="/", fg_color= "#2596be", width=60, height=60, command=lambda: self.button_callback("/"))
        self.button_division.grid(row=1, column=1, padx=0, pady=80, sticky="n")

        self.button_soustraction = customtkinter.CTkButton(self, text="_", fg_color= "#2596be", width=60, height=60, command=lambda: self.button_callback("-"))
        self.button_soustraction.grid(row=1, column=1, padx=0, pady=153, sticky="n")

        self.button_addition = customtkinter.CTkButton(self, text="+", fg_color= "#2596be", width=60, height=60, command=lambda: self.button_callback("+"))
        self.button_addition.grid(row=1, column=1, padx=0, pady=102, sticky="s")

        self.button_egal = customtkinter.CTkButton(self, text="=", fg_color= "#96be25", width=60, height=60, command=self.button_callback_egal)
        self.button_egal.grid(row=1, column=1, padx=0, pady=28, sticky="s")

        self.frame = customtkinter.CTkFrame(self, height=150, width=240)
        self.frame.grid(row=1, column=0, padx=5, sticky="nw")

        self.frame.grid_columnconfigure((0, 1, 2), weight=1, pad=5)
        self.frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1, pad=5)

        self.button_ouv = customtkinter.CTkButton(self.frame, text="(", width=60, height=60, command=lambda: self.button_callback("("))
        self.button_ouv.grid(row=0, column=0, padx=5, pady=5)

        self.button_fer = customtkinter.CTkButton(self.frame, text=")", width=60, height=60, command=lambda: self.button_callback(")"))
        self.button_fer.grid(row=0, column=1, padx=5, pady=5)

        self.button_carre = customtkinter.CTkButton(self.frame, text="x²", width=60, height=60, command=lambda: self.button_callback("carre"))
        self.button_carre.grid(row=0, column=2, padx=5, pady=5)

        self.button_sept = customtkinter.CTkButton(self.frame, text="7", width=60, height=60, command=lambda: self.button_callback(7))
        self.button_sept.grid(row=1, column=0, padx=5, pady=5)

        self.button_huit = customtkinter.CTkButton(self.frame, text="8", width=60, height=60, command=lambda: self.button_callback(8))
        self.button_huit.grid(row=1, column=1, padx=5, pady=5)

        self.button_neuf = customtkinter.CTkButton(self.frame, text="9", width=60, height=60, command=lambda: self.button_callback(9))
        self.button_neuf.grid(row=1, column=2, padx=5, pady=5)

        self.button_quatre = customtkinter.CTkButton(self.frame, text="4", width=60, height=60, command=lambda: self.button_callback(4))
        self.button_quatre.grid(row=2, column=0, padx=5, pady=5)

        self.button_cinq = customtkinter.CTkButton(self.frame, text="5", width=60, height=60, command=lambda: self.button_callback(5))
        self.button_cinq.grid(row=2, column=1, padx=5, pady=5)

        self.button_six = customtkinter.CTkButton(self.frame, text="6", width=60, height=60, command=lambda: self.button_callback(6))
        self.button_six.grid(row=2, column=2, padx=5, pady=5)

        self.button_un = customtkinter.CTkButton(self.frame, text="1", width=60, height=60, command=lambda: self.button_callback(1))
        self.button_un.grid(row=3, column=0, padx=5, pady=5)

        self.button_deux = customtkinter.CTkButton(self.frame, text="2", width=60, height=60, command=lambda: self.button_callback(2))
        self.button_deux.grid(row=3, column=1, padx=5, pady=5)

        self.button_trois = customtkinter.CTkButton(self.frame, text="3", width=60, height=60, command=lambda: self.button_callback(3))
        self.button_trois.grid(row=3, column=2, padx=5, pady=5)

        self.button_virgule = customtkinter.CTkButton(self.frame, text=".", width=60, height=60, command=lambda: self.button_callback("."))
        self.button_virgule.grid(row=4, column=0, padx=5, pady=5)
        
        self.button_zero = customtkinter.CTkButton(self.frame, text="0", width=60, height=60, command=lambda: self.button_callback(0))
        self.button_zero.grid(row=4, column=1, padx=5, pady=5)

        self.button_mulplication = customtkinter.CTkButton(self.frame, fg_color= "#2596be", text="*", width=60, height=60, command=lambda: self.button_callback("*"))
        self.button_mulplication.grid(row=4, column=2, padx=5, pady=5)


    def button_callback(self, valeur):
        print(f"button pressed {valeur}")

    def button_callback_egal(self):
        print(f"button égal pressed")

app = Calculator()
app.mainloop()