class Article:
    def __init__(self,nom,prix,quantité_en_stock):
        self.nom = nom
        self.prix = prix
        self.quantité_en_stock = quantité_en_stock

    def retirer_stock(self,quantité_acheté):          
            if self.quantité_en_stock >= quantité_acheté:
                self.quantité_en_stock -= quantité_acheté
            else:
                 print("Quantité insuffisante en stock")

carrote = Article('Carrote',10,500)
carrote.retirer_stock(5000)
