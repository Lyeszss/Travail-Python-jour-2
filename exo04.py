class Produit:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite
    def afficher_produit(self):
        print(f"Vous consultez les details du produit {self.nom} affiché a {self.prix}€. Nombre disponible en stock :{self.quantite}")
class Magasin(Produit):
    def __init__(self,liste_produit):
        self.liste_produit = liste_produit

    def ajouter_produit(self,new_produit):
        self.liste_produit.append(new_produit)
    
    def rechercher_produit(self,nom_produit):
        for i in self.liste_produit:
            #print("i.nom =",i.nom)
            #print("nom_produit =",nom_produit)
            if i.nom == nom_produit:
                return i.afficher_produit()
        print("Produit non trouvé !")


    def afficher_inventaire(self):
        for i in self.liste_produit:
            if i.quantite > 0:
                print(i.nom)
        
    
    def vendre_produit(self,quantité_acheté):
        for produit in self.liste_produit:
            if produit.quantite >= quantité_acheté:
                produit.quantite -= quantité_acheté
                print(f"Apres la vente de {quantité_acheté} {produit.nom} il reste {produit.quantite} en stock")
            else:
                print(f"Nous n'avons pas assez de {produit.nom} en stock pour vous")

    def vendre_produit1(self,quantité_acheté,produit):
        if produit in self.liste_produit:
            if produit.quantite >= quantité_acheté:
                produit.quantite -= quantité_acheté
                print(f"Apres la vente de {quantité_acheté} {produit.nom} il reste {produit.quantite} en stock")
            else:
                print(f"Nous n'avons pas assez de {produit.nom} en stock pour vous")


magasin1 = Magasin([])
produit1 = Produit("Baguette", 1, 30)
produit2 = Produit("Eau", 2, 100)
produit3 = Produit("Chocolat",10, 15)


magasin1.ajouter_produit(produit1)
magasin1.ajouter_produit(produit2)
magasin1.ajouter_produit(produit3)



magasin1.rechercher_produit("Eau")
magasin1.rechercher_produit("Neuille")

magasin1.afficher_inventaire()


magasin1.vendre_produit1(1,produit1)
