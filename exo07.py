from abc import ABC, abstractmethod

class Employe(ABC):
    @abstractmethod
    def calculer_salaire(self):
        pass

class EmployeMensuel(Employe):
    def __init__(self,nom,salaire_base):
        self.nom = nom
        self.salaire_base = salaire_base
    def calculer_salaire(self):
        return self.salaire_base
    

class EmployeHoraire(Employe):
    def __init__(self,nom,salaire_base,heures_travaille):
        self.nom = nom
        self.salaire_base = salaire_base
        self.heures_travaille = heures_travaille
    def calculer_salaire(self):
        return self.salaire_base * self.heures_travaille

class Entreprise:
    def __init__(self,liste_employé):
        self.liste_employé = liste_employé
    def calculer_masse_salariale(self):
        total = 0
        for employé in self.liste_employé:
            total += employé.calculer_salaire()
        return total
        
Tom = EmployeHoraire('Tom',80,34)
Pierre = EmployeMensuel('Pierre',2500)
entreprise = Entreprise([Tom,Pierre])
print(entreprise.calculer_masse_salariale())