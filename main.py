class DonneesGeo:
    def __init__(self,ville:str,pays:str,latitude:float,longitude:float):
        self.ville = ville
        self.pays = pays
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f'ville:{self.ville}, pays:{self.pays}, latitude:{self.latitude}, longitude:{self.longitude}'