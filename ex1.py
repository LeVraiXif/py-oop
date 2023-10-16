class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

personne = Personne("Albert", 27)

print(f'Le nom de la personne est {personne.nom}')
print(f'L\'age de la personne est {personne.age}')
