'''
Description du programme: DonneesGeo est une classe de données qui contient quatre valeurs de données géographiques.
Les valeurs sont les suivantes: le nom de la ville, le nom du pays, la latitude, la longitude.

@auteurs : Louis Joseph Pierre et Glodie Katanga

@matricules: e8798173 et

@date: 07-05-2024
'''

class DonnesGeo:

    def __init__(self, ville:str, pays:str, latitude:float, longitude:float):
        self.ville = ville
        self.pays= pays
        self.latitude = latitude
        self.longitude = longitude


    def __str__(self):
        return f" [ {self.ville} + "," +  {self.pays} + "," + {str(self.latitude)} + "," +  {str(self.longitude)}] "

'''
La fonction lireDonneesCsv" Cette fonction va lire un fichier de données csv passée en paramètre et  retourne une 
liste contenant les données gographique.
'''
def  lireDonnesCsv(nomFichier):
        import csv
        import codecs
        listeDonnees = []

        with codecs.open(nomFichier,   'r', encoding="utf-8") as f:
            lecteur = csv.reader(f)
            header= csv.Sniffer().has_header(f.read(1024)) # déterminer s'il y a une entête
            f.seek(0)                                      # pour sauter l'entête
            if header:
                next(lecteur)
            for ligne in lecteur:
                listeDonnees.append(ligne)
            return listeDonnees



Dg = "Paris", "France", "48.8534951", "2.34883915"
print(Dg)
listeDonneesGeo = []
listeDonneesGeo = lireDonnesCsv("Données.csv")
print(listeDonneesGeo)
