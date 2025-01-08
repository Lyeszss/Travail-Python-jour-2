class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
    def afficher_details(self):
        print(f"Vous consultez les details de votre {self.marque} {self.modele} d'année {self.annee} avec {self.kilometrage} de kilomètrage")
    def augmenter_kilometrage(self,nb):
        if self.kilometrage + nb < 0:
            print("Le kilometrage ne peut pas être inférieur à 0")
        else:
            self.kilometrage += nb
            print(f"Le kilometrage de votre voiture est maintenant de ",self.kilometrage)

voiture_1 = Voiture("Ford","Fusion","2010",250000) 
voiture_1.augmenter_kilometrage(10000)
voiture_1.afficher_details()

voiture_2 = Voiture("Peugeot","206","2000",400000)
voiture_2.augmenter_kilometrage(10000000)
voiture_2.afficher_details()