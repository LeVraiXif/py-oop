class Pile:
    def __init__(self):
        self.elements = []

    @property
    def top(self):
        if not self.elements:
            return None
        return self.elements[-1]

    def empiler(self, element):
        self.elements.append(element)

    def depiler(self):
        if self.elements:
            self.elements.pop()

    def __str__(self):
        return "Pile: " + str(self.elements)

class Disque:
    def __init__(self, taille):
        self.taille = taille

    @property
    def taille_disque(self):
        return self.taille

    def __str__(self):
        return "Disque de taille " + str(self.taille)

# Exemple d'utilisation
ma_pile = Pile()
ma_pile.empiler(10)
ma_pile.empiler(20)
print("Sommet de la pile:", ma_pile.top)  # Affiche : Sommet de la pile: 20
ma_pile.depiler()
print(ma_pile)  # Affiche : Pile: [10]

mon_disque = Disque(5)
print(mon_disque.taille_disque)  # Affiche : 5
print(mon_disque)  # Affiche : Disque de taille 5
