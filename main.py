import math

import numpy
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


def fctGénérerColis(_dic_lieux, _nb_colis):
    tb_colis = []

    for i in range(_nb_colis):
        type_colis = random.choice(list(TypeColis))

        # random.choice(list(dic_lieux.keys()))

        # do while
        pt_livraison = _dic_lieux[random.choice(list(_dic_lieux.keys()))]
        while pt_livraison.type_lieu is not TypeLieu.LIVRAISON:
            pt_livraison = _dic_lieux[random.choice(list(_dic_lieux.keys()))]

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
        # self.id = fctUUID()
        self.type_route = _type_route
        self.longueur = _longueur

    def fctCalculerTempsTrajet(self, _datetime, _type_véhicule):

        if str(_datetime) not in self.dic_info_trafic:
            return None

        vitesse = 0
        if self.type_route is TypeRoute.AUTOROUTE:
            if _type_véhicule is (TypeVéhicule.MOTO or TypeVéhicule.VOITURE):
                vitesse = 130
            elif _type_véhicule is TypeVéhicule.CAMION:
                vitesse = 100
        elif self.type_route is TypeRoute.NATIONALE:
            vitesse = 80
        elif self.type_route is TypeRoute.DEPARTEMENTALE:
            vitesse = 80
        elif self.type_route is TypeRoute.COMMUNALE:
            vitesse = 80

        # t = v / d * (ln trafic +1)
        temps_trajet = vitesse / (self.longueur * (math.log(self.dic_info_trafic[str(_datetime)]) + 1))

        return temps_trajet

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
            niv_trafic = numpy.random.randint(0, nb_véhicules)
            nb_véhicules = 0
            if niv_trafic == 1:
                nb_véhicules = numpy.random.randint(0, 2)
            elif niv_trafic == 2:
                nb_véhicules = numpy.random.randint(3, 6)
            elif niv_trafic == 3:
                nb_véhicules = numpy.random.randint(6, 10)
            """
            # TODO : random --> toujours la même série de nombre
            random.seed()

            # fct_trafic = random.randint(0, 1)
            nb_véhicules = random.randint(0, 10)

            while période_actuelle < _nb_périodes:

                # ■■■■■■■■■■ Véhicules ■■■■■■■■■■

                """
                if niv_trafic == 1:
                    nb_véhicules = numpy.random.randint(0, 20)
                elif niv_trafic == 2:
                    nb_véhicules = numpy.random.randint(21, 50)
                elif niv_trafic == 3:
                    nb_véhicules = numpy.random.randint(51, 100)
                """
                random.seed()
                nb_véhicules += random.randint(-10, 10)

                if nb_véhicules < 0:
                    nb_véhicules = 0

                """
                if fct_trafic == 0:
                    # 5x − x²
                    nb_véhicules = 5 * période_actuelle - période_actuelle ** 2
                elif fct_trafic == 1:
                    # f(x)=3-(2+x^(3)-2 x^(2))
                    nb_véhicules = 3 - (2 + (période_actuelle ** 3) - 2 * période_actuelle ** 2)
                """
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
                    niv_trafic = numpy.random.randint(1, 3)

            # Passer au jour suivant
            jour_actuel += 1


class TypeRoute(Enum):
    AUTOROUTE = "autoroute"  # 130
    NATIONALE = "nationale"  # 80
    DEPARTEMENTALE = "départementale"  # 80
    COMMUNALE = "communale"  # 50


def fctListeVoisins(_dic_lieux):
    dic_voisins_lieu = {}

    # complexité polynomiale !!

    for lieu in _dic_lieux.values():

        # initialisation dictionnaire des voisins du lieu actuel
        if lieu.nom_lieu not in dic_voisins_lieu:
            dic_voisins_lieu[lieu.nom_lieu] = {}

        # parcours des route du lieu actuel
        for id_route in lieu.tb_id_routes:

            # comparaison avec d'autres lieux qui ont les mêmes routes
            for voisin in _dic_lieux.values():

                if lieu is voisin:
                    continue

                # les deux lieux n'ont pas la même route
                if id_route not in voisin.tb_id_routes:
                    continue

                # initialisation du dictionnaire des voisins du voisin actuel
                if voisin.nom_lieu not in dic_voisins_lieu:
                    dic_voisins_lieu[voisin.nom_lieu] = {}

                # initialisation du tableau des routes du lieu actuel
                if voisin.nom_lieu not in dic_voisins_lieu[lieu.nom_lieu]:
                    dic_voisins_lieu[lieu.nom_lieu][voisin.nom_lieu] = []

                # initialisation du tableau des routes du voisin actuel
                if lieu.nom_lieu not in dic_voisins_lieu[voisin.nom_lieu]:
                    dic_voisins_lieu[voisin.nom_lieu][lieu.nom_lieu] = []

                # ajout de la route au lieu actuel
                if id_route not in dic_voisins_lieu[lieu.nom_lieu][voisin.nom_lieu]:
                    dic_voisins_lieu[lieu.nom_lieu][voisin.nom_lieu].append(id_route)

                # ajout de la route au voisin actuel
                if id_route not in dic_voisins_lieu[voisin.nom_lieu][lieu.nom_lieu]:
                    dic_voisins_lieu[voisin.nom_lieu][lieu.nom_lieu].append(id_route)

    return dic_voisins_lieu


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

    # tb_lieux = []
    dic_lieux = {}

    # tb_routes = []
    id_route = 0
    dic_routes = {}

    nb_heures_ouvert = numpy.random.randint(5, 9)
    # Création des points de livraison
    for i in range(_nb_lieux):
        # TODO : - A tester - heure début fin aléatoire
        lieu = Lieu(i, TypeLieu.LIVRAISON, 7, 7 + nb_heures_ouvert)
        dic_lieux[i] = lieu
        # tb_lieux.append(lieu)

    # Un lieu aléatoire devient le dépot
    index_dépot = random.choice(list(dic_lieux.keys()))
    dépot = dic_lieux[index_dépot]
    dépot.type_lieu = TypeLieu.DEPOT
    dépot.heure_début = 6
    dépot.heure_fin = 22
    dic_lieux[index_dépot] = dépot

    # index_lieu_aléatoire = numpy.random.randint(0, len(tb_lieux) - 1)
    # tb_lieux[index_lieu_aléatoire].type_lieu = TypeLieu.DEPOT
    # tb_lieux[index_lieu_aléatoire].heure_début = 6
    # tb_lieux[index_lieu_aléatoire].heure_fin = 22
    # index_dépot = index_lieu_aléatoire

    # Génération des routes
    for nom_lieu in dic_lieux:
        print("\nTraitement d'un lieu")

        # Au moins une route s'il n'en existe pas encore
        if len(dic_lieux[nom_lieu].tb_id_routes) == 0:
            pourcentage = 100
        else:
            pourcentage = numpy.random.randint(0, 100)

        while pourcentage >= 55:
            print("Générer une route (" + str(pourcentage) + ")")

            # type de route aléatoire
            type_route = random.choice(list(TypeRoute))
            # longueur aléatoire
            longueur_route = numpy.random.randint(1, 10)

            # création de la route
            route = Route(type_route, longueur_route)

            # génération des données sur 1 jour, période de 120 unités de temps
            route.fctGénérerTrafic(1, 120)

            # voisin aléatoire, différent du lieu actuel
            nom_voisin = nom_lieu
            while nom_voisin is nom_lieu:
                nom_voisin = random.choice(list(dic_lieux.keys()))

            dic_lieux[nom_lieu].tb_id_routes.append(str(id_route))
            dic_lieux[nom_voisin].tb_id_routes.append(str(id_route))

            dic_routes[str(id_route)] = route
            print("Nouvelle route n°" + str(id_route) + " de " + str(nom_lieu) + " à " + str(nom_voisin))

            id_route += 1

            pourcentage = numpy.random.randint(0, 100)

    # TODO : Parcours du plan, si tous les noeuds ne sont PAS atteignables, on recommence

    return index_dépot, dic_lieux, dic_routes


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

"""
    Génération du JSON
"""

import json


def fctGénérerJSON():
    lieux_JSON = []
    for lieu in dic_lieux.values():
        lieux_JSON.append({
            'nom_lieu': lieu.nom_lieu,
            'type_lieu': str(lieu.type_lieu),
            'début': lieu.heure_début,
            'fin': lieu.heure_fin,
            'id_routes': lieu.tb_id_routes
        })

    routes_JSON = []
    for id_route in dic_routes:
        route = dic_routes[id_route]

        routes_JSON.append({
            'id_route': id_route,
            'type_route': str(route.type_route),
            'longueur': route.longueur,
            'info_trafic': route.dic_info_trafic
        })

    # colis
    colis_JSON = []
    for colis in tb_colis:
        colis_JSON.append({
            'type_colis': str(colis.type_colis),
            'pt_livraison': colis.point_livraison
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

from pymongo import MongoClient


def fctEnregistrementDB(_tb_lieux, _dic_routes, _tb_colis):
    client = MongoClient('localhost', 27017)
    db = client['DataProject']

    collection = db['lieux']

    for nom_lieu, lieu in dic_lieux.items():
        collection.insert_one({
            'nom_lieu': nom_lieu,
            'type_lieu': str(lieu.type_lieu),
            'début': lieu.heure_début,
            'fin': lieu.heure_fin,
            'id_routes': lieu.tb_id_routes
        })

    collection = db['routes']

    for id_route, route in _dic_routes.items():
        collection.insert_one({
            'id_route': id_route,
            'type_route': str(route.type_route),
            'longueur': route.longueur,
            'info_trafic': route.dic_info_trafic
        })

    collection = db['colis']

    for colis in tb_colis:
        collection.insert_one({
            'type_colis': str(colis.type_colis),
            'pt_livraison': colis.point_livraison
        })


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
    for lieu in dic_lieux.values():
        G.add_node(lieu.nom_lieu)

        if lieu.type_lieu == TypeLieu.DEPOT:
            nodes_color_map.append(0)
        else:
            nodes_color_map.append(1)

    # Ajout des arêtes au graphe
    for lieu in dic_lieux.values():

        for voisin in dic_lieux.values():
            if lieu is voisin:
                continue

            # comparer quels lieux ont le même ID de route
            for id_route in lieu.tb_id_routes:
                for id_route_voisin in voisin.tb_id_routes:
                    if id_route != id_route_voisin:
                        continue

                    route = dic_routes[id_route]

                    edge_color = ''
                    if route.type_route is TypeRoute.DEPARTEMENTALE:
                        edge_color = 'g'
                    elif route.type_route is TypeRoute.COMMUNALE:
                        edge_color = 'y'
                    elif route.type_route is TypeRoute.NATIONALE:
                        edge_color = 'm'
                    elif route.type_route is TypeRoute.AUTOROUTE:
                        edge_color = 'b'

                    G.add_edge(lieu.nom_lieu, voisin.nom_lieu, color=edge_color)

    edges_color_map = nx.get_edge_attributes(G, 'color').values()

    nx.draw(G, node_color=nodes_color_map, edge_color=edges_color_map, cmap=plt.cm.Set1, with_labels=True)
    plt.savefig("graphe.png")  # save as png
    plt.show()  # display


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


"""
    Génération d'un itinéraire
"""

"""
    Comment diviser les colis par nombre de camion ?
    
    Lettres --> Moto
    Petits colis --> voiture
    Gros colis --> camion
    
    Liste des colis du même type avec une moyenne de poids la plus basse
    Essayer plusieurs combinaisons : pb du voyageur --> complexité polinomyale !!
    
    
    Pt départ : dépot (h ouverture du dépot)
    
"""

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

# tb_lieux = []
dic_routes = {}
tb_colis = []

index_dépot, dic_lieux, dic_routes = fctGénérerPlan(20)

tb_colis = fctGénérerColis(dic_lieux, 20)

fctGénérerJSON()

fctGénérerGraph()

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

dic_voisins = fctListeVoisins(dic_lieux)


def fctGénérerTournée(_tb_lieux, _index_dépot, _tb_colis, _type_colis):
    tb_colis_a_livrer = []

    # compl llinéaire
    for colis in _tb_colis:
        if colis.type_colis is _type_colis:
            tb_colis_a_livrer.append(colis)

    lieu_actuel = _tb_lieux[_index_dépot]

    # chercher a minimiser l'ordre


# print(dic_voisins)

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

def djikstra(_tb_lieux, _dic_voisins, _tb_lieux_livraisons, _index_dépot):
    lieu_actuel = _tb_lieux[_index_dépot]
    tb_lieux_visité = []

    itinéraire_trouvé = False

    while not itinéraire_trouvé:
        tb_lieux_visité.append(lieu_actuel)

        # Recherche de la route la plus rapide parmis les voisins


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

"""
def astar(_lieu_destination):

    # heure de départ
    heure_actuelle = tb_lieux[index_dépot].heure_début

    open_list = []
    closed_list = []

    open_list.append(tb_lieux[index_dépot])

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node is _lieu_destination:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1),
                                 (1, 1)]:  # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                        len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)


"""

"""
GENETIQUE
while len(tb_lieux_livraison) > 0:
v = 0
vmin = 0
c = tb_lieux_livraison[0]
fmin = 0  # le sous fitness

v += 1

# while v < nb_véhicules:

# liste des lieux a déservir

# déterminer les chemin pour se rendre a chaque lieux
"""
