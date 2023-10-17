class Domino:
    def __init__(self, points_A=0, points_B=0):
        self.points_A = points_A
        self.points_B = points_B

    def affichePoints(self):
        print(f"Face A : {self.points_A}, Face B : {self.points_B}")

    def valeur(self):
        return self.points_A + self.points_B

    def __repr__(self):
        return f"({self.points_A}, {self.points_B})"

domino1 = Domino(3, 5)  
domino2 = Domino(1, 4)

domino1.affichePoints()
domino2.affichePoints() 

print("Valeur de domino N°1:", domino1.valeur())  
print("Représentation de domino N°2:", repr(domino2)) 
