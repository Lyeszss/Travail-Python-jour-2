class Personnage:
    def __init__(self,nom,points_de_vie,force):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.force = force

    def attaquer(self,cible):
        cible.points_de_vie -= self.force

class Guerrier(Personnage):
    def __init__(self,nom,points_de_vie,force,bonus_force = 10):
        super().__init__(nom,points_de_vie,force)
        self.force += bonus_force

class Mage(Personnage):
    def __init__(self,nom,points_de_vie,force,attaque_magique = 20):
        super().__init__(nom,points_de_vie,force)
        force += attaque_magique

class Combat(Personnage):
    def __init__(self, personnage1, personnage2):
        self.personnage1 = personnage1
        self.personnage2 = personnage2

    def lancer_combat(self):
        while self.personnage1.points_de_vie >= 0 and self.personnage2.points_de_vie >= 0:
            self.personnage1.attaquer(self.personnage2)
            self.personnage2.attaquer(self.personnage1)
            print(f"Il reste {self.personnage1.points_de_vie} a {self.personnage1.nom} et {self.personnage2.points_de_vie} a {self.personnage2.nom}")
            if self.personnage1.points_de_vie <= 0:
                print(f"{self.personnage2.nom} a gagné !")
                
            elif self.personnage2.points_de_vie <= 0:
                print(f"{self.personnage1.nom} a gagné !")

Guerrier1 = Guerrier('Brutus',100,10)
Mage1 = Mage('Yang',85,15)
Combat1 = Combat(Guerrier1,Mage1)
Combat1.lancer_combat()