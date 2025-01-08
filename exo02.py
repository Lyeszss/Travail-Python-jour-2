class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
    def calculer_age(self,année_actuelle):
        print(f"Votre voiture est actuellement agé de {année_actuelle - self.annee}")
    def est_vielle(self,année_actuelle):
        if année_actuelle - self.annee > 10:
            return True
        else:
            return False
voiture_1 = Voiture("Ford","Fusion",2020,250000) 
voiture_1.calculer_age(2025)
print(voiture_1.est_vielle(2025))

voiture_2 = Voiture("Peugeot","206",2000,400000)
voiture_2.calculer_age(2025)
print(voiture_2.est_vielle(2025))

        