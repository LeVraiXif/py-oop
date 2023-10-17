class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def afficher(self):
        print(f"Nom: {self.nom}, Âge: {self.age}")

class Etudiant(Personne):
    def __init__(self, nom, age, filiere):
        super().__init__(nom, age)  # Appel du constructeur de la classe parente
        self.filiere = filiere

    def afficher(self):
        super().afficher()  # Appel de la méthode afficher de la classe parente
        print(f"Filière: {self.filiere}")

# Exemple d'utilisation
personne1 = Personne("Alice", 30)
personne1.afficher()  

etudiant1 = Etudiant("Bob", 20, "Informatique")
etudiant1.afficher()  
