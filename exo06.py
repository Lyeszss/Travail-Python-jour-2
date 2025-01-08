class Livre:
    def __init__(self,titre,auteur,disponible):
        self.titre = titre
        self.auteur = auteur
        self.disponible = True

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            return "Livre emprunté avec succès"
        else:
            return "Livre indisponible"
        
    def rendre(self):
        if not self.disponible:
            self.disponible = True
            return "Livre rendu avec succès"

class Utilisateur:
    def __init__(self,nom,livres_empruntes):
        self.nom = nom
        self.livres_empruntes = livres_empruntes

    def emprunter_livre(self,livre):
        if livre.disponible:
            self.livres_empruntes.append(livre)
            livre.emprunter()
            return "Livre emprunté avec succès"
        else:
            return "Livre indisponible"
        
    def rendre_livre(self,livre):
        if not livre.disponible:
            self.livres_empruntes.remove(livre)
            livre.rendre()
            return "Livre rendu avec succès"
        else:
            return "Livre déjà rendu ou n'est pas en votre possession"
    
        
class Bibliotheque:
    def __init__(self,livres):
        self.livres = livres

    def ajouter_livre(self,livre):
        self.livres.append(livre)
    
    def afficher_livres(self):
        print('Voici la liste des livres disponibles :')
        for livre in self.livres:
            if livre.disponible:
                print(f"{livre.titre} de {livre.auteur} est disponible")
    
    def gerer_emprunt(self,utilisateur,titre_livre):
        for livre_bibliotheque in self.livres:
            if livre_bibliotheque.titre == titre_livre and livre_bibliotheque.disponible:
                utilisateur.emprunter_livre(livre_bibliotheque)
                print(f"Le Livre {livre_bibliotheque.titre} a été emprunté avec succès")
            elif livre_bibliotheque.titre == titre_livre and not livre_bibliotheque.disponible:
                utilisateur.rendre_livre(livre_bibliotheque)
                print(f"Le Livre {livre_bibliotheque.titre} a été rendu avec succès")
    


livre1 = Livre("Les Misérable","Victor Hugo",True)
livre2 = Livre("Le Comte de Monte Cristo","Alexandre Dumas",True)
livre3 = Livre("Le Petit Chaperon Rouge","Charles Perrault",True)
Utilisateur1 = Utilisateur("Lyes",[])
Utilisateur2 = Utilisateur('Lecteur',[])
bibliotheque = Bibliotheque([])
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.ajouter_livre(livre3)
bibliotheque.afficher_livres()
bibliotheque.gerer_emprunt(Utilisateur1,"Les Misérable")
bibliotheque.gerer_emprunt(Utilisateur2,'Le Petit Chaperon Rouge')
bibliotheque.afficher_livres()
bibliotheque.gerer_emprunt(Utilisateur2,'Le Petit Chaperon Rouge')
bibliotheque.afficher_livres()


        