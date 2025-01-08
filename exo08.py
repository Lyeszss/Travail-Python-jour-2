class Reservation:
    def __init__(self,id,client,date,place,statut):
        self.id=id
        self.client=client
        self.date = date
        self.place = place
        self.statut = statut
    def confirmé(self,id_donné):
        if id_donné == self.id:
            self.statut = "confirmée"
        else:
            print("Cette réservation n'est pas disponible")

class CLient(Reservation):
    def __init__(self,nom,email,reservations):
        self.nom = nom
        self.email = email
        self.reservation = reservations

    def effectuer_reservation(self,id_donné,hotel):
        for i in hotel:
            if i.id == id_donné and not i.statut == "confirmée":
                i.confirmé(id_donné)
                self.reservation.append(i)
                print("Réservation confirmée")
                break               
        else:
            print("Cette réservation n'est pas disponible")


class SystemeDeReservation(Reservation):
    def __init__(self,liste_reservations):
        self.liste_reservations = liste_reservations
        
    def ajouter_reservation(self,id,client,date,place,statut):
        self.liste_reservations.append(Reservation(id,client,date,place,statut))
    
    def annuler_reservation(self,id):
        for i in self.liste_reservations:
            if i.id == id:
                i.statut = "annulée"
                print('reservations annulée')
                break


""""J'ai utilisé ChatGPT pour me générer des exemple pour testé la fonction"""

reservation1 = Reservation(1, "Alice", "2025-01-10", "Paris", "en attente")
reservation2 = Reservation(2, "Bob", "2025-02-15", "Lyon", "en attente")
reservation3 = Reservation(3, "Charlie", "2025-03-20", "Marseille", "confirmée")


systeme = SystemeDeReservation([reservation1, reservation2, reservation3])


systeme.ajouter_reservation(4, "David", "2025-04-25", "Nice", "en attente")
print("Liste des réservations après ajout :")
for r in systeme.liste_reservations:
    print(vars(r))


systeme.annuler_reservation(2)
print("Liste des réservations après annulation :")
for r in systeme.liste_reservations:
    print(vars(r))


client = CLient("Eve", "eve@example.com", [])


client.effectuer_reservation(1, systeme.liste_reservations)
print("Réservations du client après réservation :")
for r in client.reservation:
    print(vars(r))


client.effectuer_reservation(3, systeme.liste_reservations)


print("Statuts des réservations dans le système :")
for r in systeme.liste_reservations:
    print(f"ID: {r.id}, Statut: {r.statut}")
