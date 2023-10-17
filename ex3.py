import datetime

class Employe:
    def __init__(self, matricule, nom, prenom, dateNaissance, dateEmbauche, salaire):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.dateNaissance = dateNaissance
        self.dateEmbauche = dateEmbauche
        self.salaire = salaire

    def age(self):
        today = datetime.datetime.now()
        birth_year = self.dateNaissance.year
        age = today.year - birth_year
        return age

    def anciennete(self):
        today = datetime.datetime.now()
        embauche_year = self.dateEmbauche.year
        anciennete = today.year - embauche_year
        return anciennete

    def augmentationDuSalaire(self, anciennete):
        if anciennete < 5:
            self.salaire = self.salaire * 1.02
        elif anciennete < 10:
            self.salaire = self.salaire * 1.05
        else:
            self.salaire = self.salaire * 1.1
        
        self.salaire = round(self.salaire, 2)

        return print(self.salaire)

    def afficherEmploye(self):
        age_employe = self.age()
        anciennete_employe = self.anciennete()
        print(f"Matricule: {self.matricule}")
        print(f"Nom: {self.nom}")
        print(f"Prenom: {self.prenom}")
        print(f"Age: {age_employe} ans")
        print(f"Anciennete: {anciennete_employe} ans")
        print(f"Salaire: {self.salaire} €")

# Exemple d'utilisation de la classe Employe
dateNaissance = datetime.datetime(1990, 5, 15)
dateEmbauche = datetime.datetime(2010, 3, 20)
employe1 = Employe("12345", "Doe", "John", dateNaissance, dateEmbauche, 50000)

employe1.afficherEmploye()  
print(employe1.anciennete())
employe1.augmentationDuSalaire(10) # Augmentation de 10%
