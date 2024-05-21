'''
Description du programme: DonneesGeo est une classe de données qui contient quatre valeurs de données géographiques.
Les valeurs sont les suivantes: le nom de la ville, le nom du pays, la latitude, la longitude.

@auteurs : Louis Joseph Pierre et Glodie Katanga

@matricules: e8798173 et e2301706

@date: 07-05-2024
'''
import csv

import numpy as np


class DonneesGeo:

    def __init__(self, ville: str, pays: str, latitude: float, longitude: float):
        self.ville = ville
        self.pays = pays
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f" Ville: {self.ville} , Pays: {self.pays} , Latitude: {str(self.latitude)} , Longitude: {str(self.longitude)} "


'''
La fonction lireDonneesCsv", cette fonction va lire un fichier de données csv passée en paramètre et  retourne une 
liste contenant les données gographiques.
'''


def lireDonneesCsv(nomFichier):
    import csv
    import codecs
    listeDonneesGeo = []

    entete = ['Ville', 'Pays', 'Latitude', 'Longitude']
    with codecs.open(nomFichier, 'r', encoding='utf-8') as fichier_csv:
        lecteur_csv = csv.reader(fichier_csv)
        header = csv.Sniffer().has_header(
            fichier_csv.read(1024))  # saut de l'entête qui possède le champ ville avec 'uef'
        fichier_csv.seek(0)
        if header:
            next(lecteur_csv)
        for ligne in lecteur_csv:
            if len(ligne) == 4:
                ville, pays, latitude, longitude = ligne[:4]  # Déballer les valeurs de la ligne
                listeDonneesGeo.append(
                    DonneesGeo(ville, pays, latitude, longitude))  # création de la liste d'objet  DonneesGeo
        return listeDonneesGeo, entete


''' La fonction ecrireDonneesJson à pour but de prendre une liste de données géométriques et de produire un fichier .json '''


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

    with codecs.open(nomFichier, 'w', encoding='utf-8') as fichier_json:
        json.dump({"listeDonGeo": listeDictDonneesGeo}, fichier_json, indent=4)

    with codecs.open("listeDonGeo", "r", encoding="utf-8")  as f:
        lecteurDonGeo = json.load(f)
        print(lecteurDonGeo)


''' La fonction trouverDistanceMin entre deux villes, permet à l'usager de rentrer le nom de deux villes, de trouver dans le fichier json leurs latitudes et longitudes,
 ensuite de calculer la distance qui existe entre ces deux villes. Il faut conserver cette distance dans un fichier .CSV. '''


def trouverDistanceMin(nomFchier):
    import codecs
    import json
    import math
    import numpy as np
    import csv

    rayon = 6371

    with codecs.open("listeDonGeo", "r", encoding="utf-8") as f:
        dictionnaire = json.load(f)

        rechVille1 = str(input(
            "Nom de la première ville recherchée (ex- Paris) :  "))  # l'usager rentre la premièere ville à rechercher

        for i in range(0, len(dictionnaire["listeDonGeo"])):
            if dictionnaire["listeDonGeo"][i]["ville"] == rechVille1:
                print("Ville1 :", dictionnaire["listeDonGeo"][i]["ville"], dictionnaire["listeDonGeo"][i]["latitude"],
                      dictionnaire["listeDonGeo"][i]["longitude"])
                Ville1 = dictionnaire["listeDonGeo"][i]["ville"]
                latVille1 = dictionnaire["listeDonGeo"][i]["latitude"]
                longVille1 = dictionnaire["listeDonGeo"][i]["longitude"]
                paysVille1 = dictionnaire["listeDonGeo"][i]["pays"]

        rechVille2 = str(
            input('Nom de la deuxième ville recherchée :  '))  # l'usager rentre la deuxièeme ville à recehercher

        for i in range(0, len(dictionnaire["listeDonGeo"])):
            if dictionnaire["listeDonGeo"][i]["ville"] == rechVille2:
                print("Ville2 :", dictionnaire["listeDonGeo"][i]["ville"], dictionnaire["listeDonGeo"][i]["latitude"],
                      dictionnaire["listeDonGeo"][i]["longitude"])
                Ville2 = dictionnaire["listeDonGeo"][i]["ville"]
                latVille2 = dictionnaire["listeDonGeo"][i]["latitude"]
                longVille2 = dictionnaire["listeDonGeo"][i]["longitude"]
                paysVille2 = dictionnaire["listeDonGeo"][i]["pays"]


                # Calculer la distance entre les deux villes.
                # application de la formule de Haversine

                phi1 = np.radians(float(latVille1))
                phi2 = np.radians(float(latVille2))
                delta_phi = np.radians(float(latVille2) - (float(latVille1)))
                delta_lambda = np.radians((float(longVille2)) - (float(longVille1)))
                a = np.sin(delta_phi / 2) ** 2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2) ** 2
                res = rayon * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))

                print('Distance minimale en kilomètres entre 2 villes :  Ville 1  : ', '<', Ville1, '>', '<',
                      paysVille1, '>', '<', latVille1, '>', '<', longVille1, '>')
                print('                                               : Ville 2   : ','<', Ville2, '>', '<', paysVille2, '>', '<', latVille2, '>', '<', longVille2, '>',
                      'Distance en  kilomètres : ', np.round(res, 2))


                # création du fichier csv distances.csv, qui va conserver les données des clalculs

                donGeo = [Ville1,   Ville2,  float(np.round(res, 2)),]
                with open('distances.csv', 'a', newline='') as objet_fichier:
                    writeur = csv.writer(objet_fichier,  delimiter=',', quoting= csv.QUOTE_NONNUMERIC)
                    print(donGeo)
                    writeur.writerow(donGeo)



def menu():
    print()
    print("    1)  Lire les données du fichier csv, créer les objets et afficher les données.  ")
    print()
    print("    2)  Sauvegarder les données dans un fichier .json ")
    print()
    print("    3)  Lire les données du fichier .json, déterminer et afficher les données associées à la " "\n"
          "         distance minimale entre deux villes et sauvegarder les calculs dans distances.csv ")
    print()
    print("     Entrez un numéro pour choisir une option ou  sur  'q' pour quitter.  ")


# Programme principal
import codecs
import csv

menu()
exec1 = False
exec2 = False
choix = str(input("     Votre  choix (1-3, q) ? "))
while choix != 'q':
    if choix == '1':
        listeDonneesGeo = []
        listeDonneesGeo1, entet1 = lireDonneesCsv("Donnees.csv")
        print('Ligne de titre:  ', entet1)
        input('Appuyer sur Enter pour continuer')
        print()
        for donnesGeo in listeDonneesGeo1:
            print(donnesGeo.ville, donnesGeo.pays, donnesGeo.latitude, donnesGeo.longitude)
        exec1 = True
    elif choix == '2' and exec1:
        ecrireDonneesJson('listeDonGeo', listeDonneesGeo1)
        print('Les donnes ont été sauvegardées avec succées dans le fichier, listeDonGeo.json')
        print()
        input('Veuillez appuyer sur Enter pour continuer')
        exec2 = True
    elif choix == '3' and exec2:
        trouverDistanceMin('listeDonneesGeo')
        input('Veuillez appuyer sur Enter pour continuer')
    menu()
    choix = str(input("     Votre  choix (1-3, q) ? "))
if __name__ == '__menu__':
    menu()
