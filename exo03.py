class Animal:
    def __init__(self,nom,espece):
        self.nom = nom
        self.espece = espece
    def parler(self):
        print("Je suis un animal.")

class Chien(Animal):
    def __init__(self, nom):
        super().__init__(nom, "Chien")
    
    def parler(self):
        print("Wouf")

class Chat(Animal):
    def __init__(self, nom):
        super().__init__(nom, "Chat")
    
    def parler(self):
        print("Miaou")

Chat1 = Chat("Garfield")
Chat1.parler()

class Zoo:
    def __init__(self,liste_animaux):
        self.liste_animaux = []

    def ajouter_animal(self,animal):
        self.liste_animaux.append(animal)
    
    def faire_parler_tout_le_monde(self):
        for animal in self.liste_animaux:
            animal.parler()

Zoo1 = Zoo([])
Zoo1.ajouter_animal(Chat1)
Zoo1.ajouter_animal(Chien('Rex'))
Zoo1.ajouter_animal(Animal("Mufasa","Lion"))

Zoo1.faire_parler_tout_le_monde()