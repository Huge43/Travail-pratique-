'''
Description du programme: DonneesGeo est une classe de données qui contient quatre valeurs de données géographiques.
Les valeurs sont les suivantes: le nom de la ville, le nom du pays, la latitude, la longitude.

@auteurs : Louis Joseph Pierre et Glodie Katanga

@matricules: e8798173 et

@date: 07-05-2024
'''

class DonneesGeo:

    def __init__(self, ville:str, pays:str, latitude:float, longitude:float):
        self.ville = ville
        self.pays= pays
        self.latitude = latitude
        self.longitude = longitude


    def __str__(self):
        return f" Ville: {self.ville} , Pays: {self.pays} , Latitude: {str(self.latitude)} , Longitude: {str(self.longitude)} "

'''
La fonction lireDonneesCsv" Cette fonction va lire un fichier de données csv passée en paramètre et  retourne une 
liste contenant les données gographique.
'''

def  lireDonneesCsv(nomFichier):
        import csv
        import codecs
        listeDonneesGeo= []
        
        entete = ['Ville', 'Pays', 'Latitude', 'Longitude']
        with codecs.open(nomFichier,  'r', encoding='utf-8') as fichier_csv:
            lecteur_csv = csv.reader(fichier_csv)
            header= csv.Sniffer().has_header(fichier_csv.read(1024))                         # saut de l'entête qui possède le champ ville avec 'uef'
            fichier_csv.seek(0)
            if header:
                next(lecteur_csv)
            for ligne in lecteur_csv:
                if len(ligne) == 4:
                    ville, pays, latitude, longitude=ligne[:4]                                                   # Déballer les valeurs de la ligne
                    listeDonneesGeo.append(DonneesGeo(ville,pays,latitude,longitude))  #  création de la liste d'objet  DonneesGeo
        return listeDonneesGeo, entete



def ecrireDonneesJson(nomFichier, listeObjDonneesGeo):
    import codecs
    import json

    listeDictDonneesGeo = []

    for DonGeo in listeObjDonneesGeo:
        dictionnaire = {
            'ville': DonGeo.ville,
            'pays': DonGeo.pays,
            'latitude': DonGeo.latitude,
            'longitude': DonGeo.longitude
        }
        listeDictDonneesGeo.append(dictionnaire)

    with codecs.open(nomFichier, 'w', encoding = 'utf-8')  as fichier_json:
        json.dump({"listeDonGeo": listeDictDonneesGeo}, fichier_json,   indent=4 )

    with codecs.open("listeDonGeo", "r", encoding="utf-8")  as f:
        listeDonGeo = json.load(f)
        print(listeDonGeo)








Dg = "Paris", "France", "48.8534951", "2.34883915"
print(Dg)
print()
listeDonneesGeo = []
listeDonneesGeo, ent  = lireDonneesCsv("Donnees.csv")
print(ent)
for donnesGeo in listeDonneesGeo:
    print(donnesGeo)
print()
print(listeDonneesGeo[2])
print(listeDonneesGeo[2].ville)


print()
print(len(listeDonneesGeo))



fjson=ecrireDonneesJson('listeDonGeo', listeDonneesGeo)

