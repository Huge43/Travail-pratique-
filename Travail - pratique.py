"""
Programme qui calcule la distance entre 2 villes
@auteurs Glodie Katanga et Louis Joseph
@matricules e2301706 et
@date 21-05-2024
"""
import csv
import codecs
import json
import math

class DonneesGeo:
    def __init__(self, ville, pays, latitude:float, longitude:float):
        self.ville = ville
        self.pays = pays
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"Ville: {self.ville}, Pays: {self.pays}, Latitude: {self.latitude}, Longitude: {self.longitude}"


def lireDonneesCsv(nomFichier):
    liste_donnees_geo = []
    with codecs.open(nomFichier,"r",encoding="utf-8") as f:
        lecteur_csv = csv.reader(f)
        next(lecteur_csv) # Sauter l'en-tête du fichier CSV
        for ligne in lecteur_csv:
            #if len(ligne) == 4:
                ville, pays, latitude, longitude = ligne[:4]  # Déballer les valeurs de la ligne
                liste_donnees_geo.append(DonneesGeo(ville, pays, float(latitude), float(longitude)))
    return liste_donnees_geo


def ecrireDonneesJson(nomFichier, listeObjDonneesGeo):
    liste_dictionnaires = []
    for donnees_geo in listeObjDonneesGeo:
        # dictionnaire pour chaque objet DonneesGeo
        dictionnaire = {
            'ville': donnees_geo.ville,
            'pays': donnees_geo.pays,
            'latitude': donnees_geo.latitude,
            'longitude': donnees_geo.longitude,
        }
        liste_dictionnaires.append(dictionnaire)

    # Écrire la liste de dictionnaires dans un fichier JSON
    with codecs.open(nomFichier, 'w') as fichier_json:
        json.dump({'données_geo': liste_dictionnaires}, fichier_json, indent=3)


# formule pour calculer la distance
def haversine_distance(lat1, lon1, lat2, lon2):
    r = 6371.0  # Rayon de la Terre en kilomètres

    # conversion des degrés en radians
    lat1 = math.radians(float(lat1))
    lon1 = math.radians(float(lon1))
    lat2 = math.radians(float(lat2))
    lon2 = math.radians(float(lon2))

    dlon = lon2 - lon1 # différence entre la longitute 1 et 2
    dlat = lat2 - lat1 # différence entre la latitude 1 et 2

    #partie interieur de la formule
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)) # calcul de l'angle central

    distance = r * c
    return distance

def trouverDistanceMin(nomfichier):
        with open(nomfichier, "r") as f:
            data = json.load(f)
            # Créer un dictionnaire avec les noms de villes comme clés pour un accès rapide
            villes = {donnees['ville']: donnees for donnees in data['données_geo']}

            print("Villes disponibles :")
            for ville in villes:
                print(ville)

            # Demander à l'utilisateur d'entrer les noms des deux villes
            ville1_nom = input("Entrez le nom de la première ville: ")
            ville2_nom = input("Entrez le nom de la deuxième ville: ")

            if ville1_nom in villes and ville2_nom in villes:
                ville1 = villes[ville1_nom]
                ville2 = villes[ville2_nom]

                # Calculer la distance entre les deux villes choisies
                distance = haversine_distance(
                    ville1['latitude'], ville1['longitude'],
                    ville2['latitude'], ville2['longitude']
                )

                # Afficher la distance calculée
                print(
                f"Distance minimale en kilomètres entre 2 villes : Ville 1 : {ville1['ville']} {ville1['pays']}"
                f" {ville1['latitude']} {ville1['longitude']} et Ville 2 : {ville2['ville']} {ville2['pays']} "
                f"{ville2['latitude']} {ville2['longitude']} Distance en kilomètres : {round(distance,3)}")

                # Écrire la distance dans un fichier CSV
                with open("distance.csv", "a", newline='', encoding='utf-8') as fichier_csv:
                    writer = csv.writer(fichier_csv)
                    writer.writerow([ville1_nom, ville2_nom, distance])

            else:
                print("Une ou les deux villes ne sont pas dans la liste.")

def menu():
    while True:
        print("Menu")
        print("1- Lire les données du fichier csv, créer les objets et afficher les données.")
        print("2- Sauvegarder les données dans un fichier .json.")
        print("3- Lire les données du fichier .json, déterminer et afficher les données associées à "
              "la distance minimale entre deux villes et sauvegarder les calculs dans distances.csv.")
        print("Entrez un numéro pour choisir une option ou appuyez sur 'q' pour quitter :")
        choix = input()
        if choix == '1':
            donnees = lireDonneesCsv('données.csv')
            for donnee in donnees:
                print(vars(donnee)) # Afficher les attributs de chaque objet DonneesGeo
            input("Appuyez sur une touche pour continuer...")
        elif choix == '2': # Vérifier si les données ont été lues avant de les écrire dans un fichier JSON
            if 'donnees' not in locals():
                print("Veuillez d'abord lire les données avec l'option 1.")
            else:
                ecrireDonneesJson("donnees_geo.json", lireDonneesCsv("données.csv"))
                print("Données sauvegardées dans donnees.json")
        elif choix == '3': # Vérifier si les données ont été lues avant de trouver la distance
            if 'donnees' not in locals():
                print("Veuillez d'abord lire les données avec l'option 1.")
            else:
                trouverDistanceMin("donnees_geo.json")
                print("Calculs de distances sauvegardés dans distances.csv")
        elif choix.lower() == 'q':
            break

menu()
