class Transaction:
    def __init__(self, idSeller, idBuyer, amount, price, energyType):
        self.idSeller = idSeller
        self.idBuyer = idBuyer
        self.amount = amount
        self.price = price
        self.energyType = energyType

    def to_dict(self):
        return {
            'idSeller': self.idSeller,
            'idBuyer': self.idBuyer,
            'amount': self.amount,
            'price': self.price,
            'energyType': self.energyType
        }
    
    

    
        