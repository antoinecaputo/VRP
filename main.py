import random
from enum import Enum

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

import binascii
import os


def fctUUID():
    return str(binascii.b2a_hex(os.urandom(12)), 'utf-8')


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


def fctGénérerColis(_tb_lieux, _nb_colis):
    tb_colis = []

    for i in range(_nb_colis):
        type_colis = random.choice(list(TypeColis))

        # do while
        pt_livraison = _tb_lieux[random.randint(0, len(tb_lieux)-1)]
        while pt_livraison.type_lieu is not TypeLieu.LIVRAISON:
            pt_livraison = _tb_lieux[random.randint(0, len(tb_lieux)-1)]

        tb_colis.append(Colis(type_colis, pt_livraison.nom_lieu))

    return tb_colis


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

# Un lieu peut être un dépot ou un point de livraison
# # Un point de livraison a des horaires d'ouverture et de fermeture
class Lieu:

    def __init__(self, _nom_lieu, _type_lieu, _heure_début, _heure_fin):
        self.tb_id_routes = []
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
    CAMION = "camion"
    VOITURE = "voiture"
    MOTO = "moto"


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

import datetime


# Une route à un type et une longueur
# Elle contient également ses informations de circulation
class Route:
    dic_info_trafic = {}

    def __init__(self, _type_route, _longueur):
        self.id = fctUUID()
        self.type_route = _type_route
        self.longueur = _longueur

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

    def fctGénérerTrafic(self, _nb_jours, _nb_périodes):

        jour_actuel = 0

        """
        nb_véhicules = 0
        if _route.type_route is TypeRoute.COMMUNALE:
            nb_véhicules = 1
        elif _route.type_route is TypeRoute.DEPARTEMENTALE:
            nb_véhicules = 2
        elif _route.type_route is TypeRoute.NATIONALE:
            nb_véhicules = 3
        elif _route.type_route is TypeRoute.AUTOROUTE:
            nb_véhicules = 4
        """

        # nb_véhicules += _route.longueur

        while jour_actuel < _nb_jours:

            plage_horaire_actuelle = 'm'
            période_actuelle = 0

            """
            niv_trafic = random.randint(0, nb_véhicules)
            nb_véhicules = 0
            if niv_trafic == 1:
                nb_véhicules = random.randint(0, 2)
            elif niv_trafic == 2:
                nb_véhicules = random.randint(3, 6)
            elif niv_trafic == 3:
                nb_véhicules = random.randint(6, 10)
            """

            fct_trafic = random.randint(0, 1)

            while période_actuelle < _nb_périodes:

                # ■■■■■■■■■■ Véhicules ■■■■■■■■■■

                """
                if niv_trafic == 1:
                    nb_véhicules = random.randint(0, 20)
                elif niv_trafic == 2:
                    nb_véhicules = random.randint(21, 50)
                elif niv_trafic == 3:
                    nb_véhicules = random.randint(51, 100)
                """

                nb_véhicules = 0

                if fct_trafic == 0:
                    # 5x − x²
                    nb_véhicules = 5 * période_actuelle - période_actuelle ** 2
                elif fct_trafic == 1:
                    # f(x)=3-(2+x^(3)-2 x^(2))
                    nb_véhicules = 3 - (2 + (période_actuelle ** 3) - 2 * période_actuelle ** 2)

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

                self.dic_info_trafic[date_info_trafic.strftime("%Y%m%d%H%M")] = nb_véhicules

                # ■■■■■■■■■■ Période suivante ■■■■■■■■■■

                période_actuelle += 1

                # Passer de la plage matin à soir
                if plage_horaire_actuelle == 'm' and période_actuelle == _nb_périodes:
                    plage_horaire_actuelle = 's'
                    période_actuelle = 0
                    niv_trafic = random.randint(1, 3)

            # Passer au jour suivant
            jour_actuel += 1


class TypeRoute(Enum):
    AUTOROUTE = "autoroute"  # 130
    NATIONALE = "nationale"  # 80
    DEPARTEMENTALE = "départementale"  # 80
    COMMUNALE = "communale"  # 50


def fctChercherRouteParID(_tb_routes, _id):
    for _route in _tb_routes:
        if _route.id == id:
            return _route

    return None


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

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
list
    Tableau d'objets Route
"""


def fctGénérerPlan(_nb_lieux):
    if _nb_lieux < 2:
        raise ValueError("Le nombre de lieux doit au minimum être 2")

    tb_lieux = []

    tb_routes = []

    nb_heures_ouvert = random.randint(5, 9)
    # Création des points de livraison
    for i in range(_nb_lieux):
        # TODO : - A tester - heure début fin aléatoire
        lieu = Lieu(i, TypeLieu.LIVRAISON, 7, 7 + nb_heures_ouvert)
        tb_lieux.append(lieu)

    # Un lieu aléatoire devient le dépot
    index_lieu_aléatoire = random.randint(0, len(tb_lieux) - 1)
    tb_lieux[index_lieu_aléatoire].type_lieu = TypeLieu.DEPOT
    tb_lieux[index_lieu_aléatoire].heure_début = 6
    tb_lieux[index_lieu_aléatoire].heure_fin = 22

    # Génération des routes
    for lieu in tb_lieux:
        print("\nTraitement d'un lieu")

        # Au moins une route s'il n'en existe pas encore
        if len(lieu.tb_id_routes) == 0:
            pourcentage = 100
        else:
            pourcentage = random.randint(0, 100)

        while pourcentage >= 55:
            print("Générer une route (" + str(pourcentage) + ")")

            # type de route aléatoire
            type_route = random.choice(list(TypeRoute))
            # longueur aléatoire
            longueur_route = random.randint(1, 10)

            # création de la route
            route = Route(type_route, longueur_route)
            print("ID ROUTE : " + route.id)

            # génération des données sur 1 jour, période de 120 unités de temps
            route.fctGénérerTrafic(1, 120)

            # voisin aléatoire, différent du lieu actuel
            voisin = lieu
            while voisin is lieu:
                voisin = tb_lieux[random.randint(0, len(tb_lieux) - 1)]

            lieu.tb_id_routes.append(route.id)
            voisin.tb_id_routes.append(route.id)

            tb_routes.append(route)

            print("Nouvelle route de " + lieu.nom_lieu + " à " + voisin.nom_lieu)

            pourcentage = random.randint(0, 100)

    # TODO : Parcours du plan, si tous les noeuds ne sont PAS atteignables, on recommence

    return tb_lieux, tb_routes


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

"""
    Génération du JSON
"""

import json


def fctGénérerJSON():
    lieux_JSON = []
    for lieu in tb_lieux:
        lieux_JSON.append({
            'nom_lieu': lieu.nom_lieu,
            'type_lieu': str(lieu.type_lieu),
            'début': lieu.heure_début,
            'fin': lieu.heure_fin,
            'id_routes': lieu.tb_id_routes
        })

    routes_JSON = []
    for route in tb_routes:
        routes_JSON.append({
            'id_route': route.id,
            'type_route': str(route.type_route),
            'longueur': route.longueur,
            'info_trafic': route.dic_info_trafic
        })

    # colis
    colis_JSON = []
    for colis in tb_colis:
        colis_JSON.append({
            'type_colis':str(colis.type_colis),
            'pt_livraison':colis.point_livraison
        })

    # écriture
    with open('data.json', 'w') as outfile:
        json.dump({
            'lieux': lieux_JSON,
            'routes': routes_JSON,
            'colis': colis_JSON
        }, outfile)


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

"""
    Enregistrement dans mongoDB
"""


def fctEnregistrementDB(_document):
    """

collection_trafic_stamped.insert_one({
    "_id": trafic["_id"],
    "num_arete": trafic["num_arete"],
    "date": date,
    "nb_vehicules": trafic["nb_vehicules"]
})

"""


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

"""
    Génération du graphe
"""

import networkx as nx
import matplotlib.pyplot as plt


def fctGénérerGraph():
    G = nx.Graph()

    # Ajout des noeuds au graphe
    nodes_color_map = []
    for lieu in tb_lieux:
        G.add_node(lieu.nom_lieu)

        if lieu.type_lieu == TypeLieu.DEPOT:
            nodes_color_map.append(0)
        else:
            nodes_color_map.append(1)

    # Ajout des arêtes au graphe
    for lieu in tb_lieux:

        for voisin in tb_lieux:
            if lieu is voisin:
                continue

            # comparer quels lieux ont le même ID de route
            for id_route in lieu.tb_id_routes:
                for id_route_voisin in voisin.tb_id_routes:
                    if id_route != id_route_voisin:
                        continue

                    G.add_edge(lieu.nom_lieu, voisin.nom_lieu, color='b')

                """
                route = fctChercherRouteParID(tb_routes, id_route)

                edge_color = ''
                if route.type_route is TypeRoute.DEPARTEMENTALE:
                    edge_color = 'g'
                elif route.type_route is TypeRoute.COMMUNALE:
                    edge_color = 'y'
                elif route.type_route is TypeRoute.NATIONALE:
                    edge_color = 'm'
                elif route.type_route is TypeRoute.AUTOROUTE:
                    edge_color = 'b'
                    
                """

    edges_color_map = nx.get_edge_attributes(G, 'color').values()

    nx.draw(G, node_color=nodes_color_map, edge_color=edges_color_map, cmap=plt.cm.Set1, with_labels=True)
    plt.savefig("graphe.png")  # save as png
    plt.show()  # display


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


"""
    Génération d'un itinéraire
"""

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

tb_lieux = []
tb_routes = []
tb_colis = []

tb_lieux, tb_routes = fctGénérerPlan(20)

tb_colis = fctGénérerColis(tb_lieux, 100)

fctGénérerJSON()

fctGénérerGraph()

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
