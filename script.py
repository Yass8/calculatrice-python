import customtkinter


# Classe principale de la calculatrice héritant de customtkinter.CTk
class Calculator(customtkinter.CTk):

    expression = ""

    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre principale
        self.title("Calculator")
        self.geometry("300x470") 
        self.resizable(False, False)

        # Configuration du système de grille de la fenêtre principale
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Création et configuration du cadre pour afficher le résultat
        self.frame_resultat = customtkinter.CTkFrame(self)
        self.frame_resultat.grid(row=0, column=0, padx=5, pady=5, sticky="nwe")

        # Configuration du système de grille pour le cadre de résultat
        self.frame_resultat.grid_columnconfigure((0,1), weight=1)
        self.frame_resultat.grid_rowconfigure(0, weight=1)

        # Entry (affichage)
        self.entry_var = customtkinter.StringVar()
        self.entry = customtkinter.CTkEntry(self.frame_resultat, textvariable=self.entry_var, width=220, height=60, font=("Arial", 14), justify='right')
        self.entry.grid(row=0, column=0, padx=5, pady=5)
        
        # Bouton pour effacer le résultat
        self.button = customtkinter.CTkButton(self.frame_resultat, text="C", fg_color= "#be4d25", width=60, height=60, command=lambda: self.button_callback("C"))
        self.button.grid(row=0, column=1, padx=5,pady=5, sticky="e")

        # Création et configuration du cadre pour les boutons de la calculatrice
        self.frame_buttons = customtkinter.CTkFrame(self)
        self.frame_buttons.grid(row=1, column=0, padx=5, pady=5, sticky="n")

        # Configuration du système de grille pour le cadre des boutons
        self.frame_buttons.grid_columnconfigure((0, 1, 2, 4), weight=1, pad=5)
        self.frame_buttons.grid_rowconfigure((0, 1, 2, 3, 4), weight=1, pad=5)

        self.create_buttons()

    # Méthode pour créer et positionner les boutons de la calculatrice
    def create_buttons(self):
        buttons = [
            ('(', 0, 0), (')', 0, 1), ('x²', 0, 2), ('DEL', 0, 3,'#be4d25'),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3,'#2596be'),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3,'#2596be'),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3,'#2596be'),
            ('.', 4, 0), ('0', 4, 1), ('*', 4, 2,'#2596be'), ('=', 4, 3, '#96be25')
        ]

        # Boucle pour créer chaque bouton et le positionner dans la grille
        for button in buttons:
            if len(button) == 4:
                text, row, col, color = button
            else:
                text, row, col = button
                color = "#1a6985"  # Couleur par défaut

            self.create_button(text, row, col, color)

    # Méthode pour créer un bouton avec les propriétés spécifiées
    def create_button(self, text, row, col, color="#1a6985"):
        button = customtkinter.CTkButton(self.frame_buttons, text=text, fg_color=color, width=60, height=60, font=('Arial', 18), command=lambda t=text: self.button_callback(t))
        button.grid(row=row, column=col, padx=5, pady=5) 

    # Méthode de rappel pour les actions des boutons
    def button_callback(self, valeur):
        current_text = self.entry_var.get()
        
        if valeur == '=':
            self.calculate_expression(current_text)
        elif valeur == 'DEL':
            self.delete_last_character(current_text)
        elif valeur == "C":
            self.clear_expression()
        elif valeur == "x²":
            self.square_expression(current_text)
        else:
            self.append_to_expression(valeur, current_text)

    def calculate_expression(self, expression):
        if expression:
            self.expression = expression
            self.calculer()

    def delete_last_character(self, expression):
        if expression and expression != 'Syntaxe erreur':
            self.entry_var.set(expression[:-1])
            self.expression = self.entry_var.get()

    def clear_expression(self):
        self.expression = ""
        self.entry_var.set(self.expression)

    def square_expression(self, expression):
        if expression:
            try:
                value = eval(expression)
                self.entry_var.set(f"{value}*{value}")
            except Exception as e:
                self.entry_var.set("Syntaxe erreur")
                print(e)

    def append_to_expression(self, value, expression):
        if self.entry_var.get() != 'Syntaxe erreur':
            self.expression = expression + value
            self.entry_var.set(self.expression)

    def calculer(self):
        self.expression = self.entry_var.get()
        if self.expression:
            try:
                resultat = eval(self.expression)
                self.entry_var.set(str(resultat))
            except Exception as e:
                self.entry_var.set("Syntaxe erreur")
                print(e)

            
# Initialisation et démarrage de l'application
app = Calculator()
app.mainloop()
