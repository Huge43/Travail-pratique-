import csv
import codecs
import json


class DonneesGeo:
    def __init__(self, ville, pays, latitude, longitude):
        self.ville = ville
        self.pays = pays
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"Ville: {self.ville}, Pays: {self.pays}, Latitude: {self.latitude}, Longitude: {self.longitude}"


def lireDonneesCsv(nomFichier):
    liste_donnees_geo = []
    with codecs.open(nomFichier,"r", encoding="utf-8") as f:
        lecteur_csv = csv.reader(f)
        for ligne in lecteur_csv:
            #if len(ligne) == 4:
                ville, pays, latitude, longitude = ligne[:4]  # Déballer les valeurs de la ligne
                liste_donnees_geo.append(DonneesGeo(ville, pays, latitude, longitude))
    return liste_donnees_geo


def ecrireDonneesJson(nomFichier, listeObjDonneesGeo):
    liste_dictionnaires = []
    for donnees_geo in listeObjDonneesGeo:
        dictionnaire = {
            'ville': donnees_geo.ville,
            'pays': donnees_geo.pays,
            'latitude': donnees_geo.latitude,
            'longitude': donnees_geo.longitude
        }
        liste_dictionnaires.append(dictionnaire)

    with codecs.open(nomFichier, 'w') as fichier_json:
        json.dump({'Donnees_geo.json': liste_dictionnaires}, fichier_json, indent=4)




# Lecture des données depuis un fichier CSV
liste_donnees = lireDonneesCsv("Donnes.csv")
for donnees_geo in liste_donnees:
    print(donnees_geo)

# Écriture des données dans un fichier JSON
ecrireDonneesJson("donnees_geo.json", liste_donnees)
