import datetime
import random
from enum import Enum


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

# Un colis doit être déposé dans un point de livraison spécifique
class Colis:

    def __init__(self, _type_colis, _pt_livraison):
        self.type_colis = _type_colis
        self.point_livraison = _pt_livraison


class TypeColis(Enum):
    GROS_CARTON = "gros_carton"
    PETIT_CARTON = "petit_carton"
    LETTRE = "lettre"


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

# Un lieu peut être un dépot ou un point de livraison
# # Un point de livraison a des horaires d'ouverture et de fermeture
class Lieu:

    def __init__(self, _nom_lieu, _type_lieu, _heure_début, _heure_fin):
        self.nom_lieu = str(_nom_lieu)
        self.type_lieu = _type_lieu
        self.heure_début = _heure_début
        self.heure_fin = _heure_fin


class TypeLieu(Enum):
    DEPOT = 1
    LIVRAISON = 2


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

# Un véhicule à un type et transporte des colis
class Véhicule:
    # colis = []

    def __init__(self, _type_véhicule):
        self.type_véhicule = _type_véhicule


class TypeVéhicule(Enum):
    CAMION = 1
    VOITURE = 2
    VELO = 3


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

# Une route à un type et une longueur
# Elle contient également ses informations de circulation
class Route:
    # tb_lieux_connectés = [None] * 2

    dic_info_trafic = {}

    def __init__(self, _type_route, _longueur):
        self.type_route = _type_route
        self.longueur = _longueur
        # self.tb_lieux_connectés[0] = _lieu1
        # self.tb_lieux_connectés[1] = _lieu2


class TypeRoute(Enum):
    AUTOROUTE = "AUTOROUTE"  # 130
    NATIONALE = "NATIONALE"  # 80
    DEPARTEMENTALE = "DEPARTEMENTALE"  # 80
    COMMUNALE = "COMMUNALE"  # 50


"""
class InfoTrafic:
    def __init__(self, _date, _nb_véhicules):
        self.date = _date
        self.nb_véhciules = _nb_véhicules

"""

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

"""
Génére des données de trafic d'un axe routier

Paramètres
----------
_nb_jours : int
    Sur combien de jours les données vont être générées
_nb_périodes : sound : str
    Sur combien de période les données vont être générées
    le matin et le soir de chaque journéee

Retours
----------
dict
    Le nombre de voiture pour une ANNEE-MOIS-JOURS-HEURE-MINUTES
    dic_info_trafic[date_info_trafic.strftime("%Y%m%d%H%M")] = nb_véhicules
"""


def fctGénérerTrafic(_nb_jours, _nb_périodes):
    dic_info_trafic = {}

    jour_actuel = 0

    while (jour_actuel < _nb_jours):

        plage_horaire_actuelle = 'm'
        période_actuelle = 0

        while période_actuelle < _nb_périodes:

            # ■■■■■■■■■■ Véhicules ■■■■■■■■■■

            nb_véhicules = 0

            # trafic faible/moyen/élevé
            niv_trafic = random.randint(1, 3)
            if niv_trafic == 1:
                nb_véhicules = random.randint(0, 20)
            elif niv_trafic == 2:
                nb_véhicules = random.randint(21, 50)
            elif niv_trafic == 3:
                nb_véhicules = random.randint(51, 100)

            # ■■■■■■■■■■ Date ■■■■■■■■■■

            heure = int((période_actuelle + 1) / 60)
            minutes = (période_actuelle + 1) % 60

            # matin
            if plage_horaire_actuelle == 'm':
                heure += 7

            # soir
            if plage_horaire_actuelle == 's':
                heure += 19

            date_info_trafic = datetime.datetime(2020, 1, jour_actuel + 1, heure, minutes)

            # ■■■■■■■■■■ Enregistrer ■■■■■■■■■■

            dic_info_trafic[date_info_trafic.strftime("%Y%m%d%H%M")] = nb_véhicules

            # ■■■■■■■■■■ Période suivante ■■■■■■■■■■

            période_actuelle += 1

            # Passer de la plage matin à soir
            if plage_horaire_actuelle == 'm' and période_actuelle == _nb_périodes:
                plage_horaire_actuelle = 's'
                période_actuelle = 0

        # Passer au jour suivant
        jour_actuel += 1

    return dic_info_trafic


"""
Génére des lieux reliés par des routes

Paramètres
----------
_nb_lieux : int
    Nombre de lieu à générer dans le plan
    Minimum 2, pour un dépot et un point de livraison

Retours
----------
list
    Tableau d'objets Lieu
dict
    Pour chaque nom de lieu, un tableau contenant la liste des routes de ce lieu
"""
def fctGénérerPlan(_nb_lieux):
    if _nb_lieux < 2:
        raise ValueError("Le nombre de lieux doit au minimum être 2")

    tb_lieux = []

    dic_routes_ville = {}

    # Création des points de livraison
    for i in range(_nb_lieux):
        lieu = Lieu(i, TypeLieu.LIVRAISON, 9, 18)
        tb_lieux.append(lieu)

    # Un lieu aléatoire devient le dépot
    tb_lieux[random.randint(0, len(tb_lieux) - 1)].type_lieu = TypeLieu.DEPOT

    # Génération des routes
    for lieu in tb_lieux:
        print("\nTraitement d'un lieu")

        # check if key exists in dictionary by checking if get() returned None
        if dic_routes_ville.get(lieu.nom_lieu) is None:
            dic_routes_ville[lieu.nom_lieu] = []

        pourcentage = 100

        while pourcentage >= 70:
            print("Générer une route (" + str(pourcentage) + ")")

            # type de route aléatoire
            type_route = random.choice(list(TypeRoute))
            # longueur aléatoire
            longueur_route = random.randint(1, 10)

            # voisin aléatoire, différent du lieu actuel
            voisin = lieu
            while voisin is lieu:
                voisin = tb_lieux[random.randint(0, len(tb_lieux) - 1)]

            # création de la route
            route = Route(type_route, longueur_route)

            # génération des données sur 1 jour, période de 120 unités de temps
            route.dic_info_trafic = fctGénérerTrafic(1, 120)

            dic_routes_ville[lieu.nom_lieu].append(route)

            # check if key exists in dictionary by checking if get() returned None
            if dic_routes_ville.get(voisin.nom_lieu) is None:
                dic_routes_ville[voisin.nom_lieu] = []

            dic_routes_ville[voisin.nom_lieu].append(route)

            print("Nouvelle route de " + lieu.nom_lieu + " à " + voisin.nom_lieu)
            pourcentage = random.randint(0, 100)

    return tb_lieux, dic_routes_ville


tb_lieux, dic_routes_lieu = fctGénérerPlan(10)

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Ajout des noeuds au graphe
color_map = []
for lieu in tb_lieux:
    G.add_node(lieu.nom_lieu)

    if lieu.type_lieu == TypeLieu.DEPOT:
        color_map.append(0)
    else:
        color_map.append(1)

# Ajout des arêtes au graphe
for nom_lieu in dic_routes_lieu:

    tb_routes = dic_routes_lieu[nom_lieu]
    for route in tb_routes:

        # comparer qui a la même route
        for nom_lieu_voisin in dic_routes_lieu:
            if nom_lieu is nom_lieu_voisin:
                continue

            tb_routes_voisin = dic_routes_lieu[nom_lieu_voisin]
            for route_voisin in tb_routes_voisin:
                if route is not route_voisin:
                    continue

                edge = (nom_lieu, nom_lieu_voisin)
                G.add_edge(*edge)

nx.draw(G, node_color=color_map, cmap=plt.cm.Set1, with_labels=True)
plt.savefig("graphe.png")  # save as png
plt.show()  # display
