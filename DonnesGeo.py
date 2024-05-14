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
        return f" [ {self.ville} ,  {self.pays} ,  {str(self.latitude)} ,  {str(self.longitude)}] "

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
            header= csv.Sniffer().has_header(fichier_csv.read(1024))     # saut de l'entête qui possède le champ ville avec 'uef'
            fichier_csv.seek(0)
            if header:
                next(lecteur_csv)

            for ligne in lecteur_csv:
                listeDonneesGeo.append(ligne)
        return listeDonneesGeo



def ecrireDonneesJson(nomFichier, listeObjDonneesGeo):
    import json
    listeDictDonneesGeo = {}
    cle= ['Ville','Pays','Latitude', 'Longitude']
    valeur = listeObjDonneesGeo

    lst0 =['Ville']
    lst2 =['Pays']
    lst3 = ['Latitude']
    lst4 = ['Longitude']
    lstC = lst0 + lst2 + lst3 + lst4

    print(lstC)
    Dict4 = {}
    Dict0 = {}
    Dict1 = {}
    Dict2 = {}
    Dict3 = {}
    Dict4 =lstC                               #  doit être des slices pour être utilisé dans la boucle remplir le dictionnaire



    Dict0[(cle[0])] = ['Paris']                             #  les clés Ville, Pays, latitude, Logitude sont initialisés
    Dict0[(cle[1])]= ['France' ]                          #  avec les informations de la ville de Paris
    Dict0[(cle[2])]=['48.8534951']
    Dict0[(cle[3])] =['2.34883915']


    for i in range (1,(len(valeur)-1)):                           # pour remplir le  dictonnaire
        for j in range (len(cle)):
            Dict0[(cle[j])].append(valeur[i][j])

    print(Dict4)
    print(Dict0)
    print(Dict0['Ville'][0], ['Pays'][0],)                  # erreur ne produit pas le résultat espéré, pays devrait être France et non pays










Dg = "Paris", "France", "48.8534951", "2.34883915"
print(Dg)
print()
listeDonneesGeo = []
listeDonneesGeo = lireDonneesCsv("Donnees.csv")
print(listeDonneesGeo)
essai =ecrireDonneesJson("Donnees.csv", listeDonneesGeo)