class Etudiant:
    def __init__(self, nom, prenom, note_nsi, note_maths, note_phy):
        self.nom = nom
        self.prenom = prenom
        self.note_nsi = note_nsi
        self.note_maths = note_maths
        self.note_phy = note_phy

    def __str__(self):
        return f"Nom: {self.nom}, Prénom: {self.prenom}, NSI: {self.note_nsi}, Maths: {self.note_maths}, Physique: {self.note_phy}"

    def moyenne(self):
        return (self.note_nsi + self.note_maths + self.note_phy) / 3

    def __lt__(self, other):
        return self.moyenne() < other.moyenne()

E1 = Etudiant("SARR", "Junior", 18, 18, 15)
E2 = Etudiant("FUSIL", "Morgan", 17, 15, 16)
E3 = Etudiant("BEYA", "Noa", 14, 19, 18)
E4 = Etudiant("BONNET", "Anne", 5, 7, 9)

print(E1)
print(E2)
print(E3)
print(E4)

print(E1 < E2)  
