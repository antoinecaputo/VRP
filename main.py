import math
import sys

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

    def __init__(self, _type_colis, _lieu_livraison):
        self.type_colis = _type_colis
        self.lieu_livraison = str(_lieu_livraison)


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
        lieu_livraison = _dic_lieux[random.choice(list(_dic_lieux.keys()))]
        while lieu_livraison.type_lieu is not TypeLieu.LIVRAISON:
            lieu_livraison = _dic_lieux[random.choice(list(_dic_lieux.keys()))]

        tb_colis.append(Colis(type_colis, lieu_livraison.nom_lieu))

    return tb_colis


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

# Un lieu peut être un dépot ou un point de livraison
# # Un point de livraison a des horaires d'ouverture et de fermeturee
class Lieu:

    def __init__(self, _nom_lieu, _type_lieu, _heure_ouverture, _heure_fermeture):
        self.tb_id_routes = []
        self.nom_lieu = str(_nom_lieu)
        self.type_lieu = _type_lieu
        self.heure_ouverture = _heure_ouverture
        self.heure_fermeture = _heure_fermeture


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

        datetime_str = _datetime.strftime("%Y%m%d%H%M")

        if datetime_str not in self.dic_info_trafic:
            print(datetime_str + " not in dic_info_trafic")
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

        # t (min) = v / d * (ln trafic +1)
        trafic = self.dic_info_trafic[datetime_str]
        if trafic <= 0:
            trafic = 1

        temps_trajet = vitesse / (self.longueur * math.log(1 + trafic))

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

        _nb_jours = 1
        _nb_périodes = 1080  # 6h -> 0h : 18h
        jour_actuel = 0

        while jour_actuel < _nb_jours:

            plage_horaire_actuelle = 'm'
            période_actuelle = 0

            # TODO : random --> toujours la même série de nombre

            nb_véhicules = random.randint(0, 10)

            while période_actuelle < _nb_périodes:

                # ■■■■■■■■■■ Véhicules ■■■■■■■■■■

                nb_véhicules += random.randint(-10, 10)

                if nb_véhicules < 0:
                    nb_véhicules = 0

                # ■■■■■■■■■■ Date ■■■■■■■■■■

                heure = int(période_actuelle / 60)
                minutes = période_actuelle % 60

                # début data à partir de 6h
                heure += 6

                # passer de matin à soir
                if plage_horaire_actuelle == 'm' and heure >= 12:
                    plage_horaire_actuelle = 's'

                date_info_trafic = datetime.datetime(2020, 1, jour_actuel + 1, heure, minutes)

                # ■■■■■■■■■■ Enregistrer ■■■■■■■■■■

                self.dic_info_trafic[date_info_trafic.strftime("%Y%m%d%H%M")] = nb_véhicules

                # ■■■■■■■■■■ Période suivante ■■■■■■■■■■

                période_actuelle += 1

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


"""
def my_weight(G, u, v, id_route="id_route"):

    edges_data = G.get_edges_data(u,v)
    if id_route not in edges_data:
        print("pas d'info de route")
        return
    
    global dic_routes
    route = dic_routes[edges_data[id_route]]

    return route.fctCalculerTempsTrajet()
"""

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

    # TODO : - A tester - heure ouverture fermeture aléatoire
    nb_heures_ouvert = numpy.random.randint(7, 11)
    # Création des points de livraison
    for i in range(_nb_lieux):
        ouverture = random.randint(7, 10)
        lieu = Lieu(i, TypeLieu.LIVRAISON, ouverture, ouverture + nb_heures_ouvert)
        dic_lieux[str(i)] = lieu
        # tb_lieux.append(lieu)

    # Un lieu aléatoire devient le dépot
    index_dépot = str(random.choice(list(dic_lieux.keys())))
    dépot = dic_lieux[index_dépot]
    dépot.type_lieu = TypeLieu.DEPOT
    dépot.heure_ouverture = 7
    dépot.heure_fermeture = 22
    dic_lieux[index_dépot] = dépot

    # index_lieu_aléatoire = numpy.random.randint(0, len(tb_lieux) - 1)
    # tb_lieux[index_lieu_aléatoire].type_lieu = TypeLieu.DEPOT
    # tb_lieux[index_lieu_aléatoire].heure_ouverture = 6
    # tb_lieux[index_lieu_aléatoire].heure_fermeture = 22
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
            'ouverture': lieu.heure_ouverture,
            'fermeture': lieu.heure_fermeture,
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
            'lieu_livraison': colis.lieu_livraison
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
            'ouverture': lieu.heure_ouverture,
            'fermeture': lieu.heure_fermeture,
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
            'lieu_livraison': colis.lieu_livraison
        })


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

"""
    Génération du graphe
"""

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def fctGénérerGraph(_dic_voisins):
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
    for nom_lieu, dic_lieux_voisins in _dic_voisins.items():

        for nom_lieu_voisin, tb_routes in dic_lieux_voisins.items():

            for id_route in tb_routes:

                # print(str(nom_lieu) + " - " + str(nom_lieu_voisin) + " : " + str(id_route))
                edge_data = G.edges.data("id_route")
                if (nom_lieu, nom_lieu_voisin) in edge_data:
                    if edge_data[nom_lieu, nom_lieu_voisin] is id_route:
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

                G.add_edge(nom_lieu, nom_lieu_voisin, id_route=id_route, length=route.longueur, color=edge_color)

    edges_color_map = nx.get_edge_attributes(G, 'color').values()

    if not nx.is_connected(G):
        print("not reachable nodes in graph")
        sys.exit(-1)

    nx.draw(G, node_color=nodes_color_map, edge_color=edges_color_map, cmap=plt.cm.Set1, node_size=100, font_size=10,
            with_labels=True)

    autoroute_patch = mpatches.Patch(color='blue', label='Highway')
    departementale_patch = mpatches.Patch(color='green', label='Departmental')
    communale_patch = mpatches.Patch(color='yellow', label='Communal')
    nationale_patch = mpatches.Patch(color='magenta', label='National')

    plt.legend(handles=[autoroute_patch, departementale_patch, communale_patch, nationale_patch])

    # larger figure size
    plt.figure(3, figsize=(15, 15))

    plt.savefig("graphe.png")  # save as png
    plt.show()  # display

    # H = nx.path_graph(G.number_of_nodes())
    # H.add_edges_from(G.edges())
    return G


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

index_dépot, dic_lieux, dic_routes = fctGénérerPlan(50)

dic_voisins = fctListeVoisins(dic_lieux)

tb_colis = fctGénérerColis(dic_lieux, 20)

fctGénérerJSON()

G = fctGénérerGraph(dic_voisins)


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


def fctGénérerTournée(_tb_colis, _type_véhicule):
    global index_dépot
    global dic_lieux
    global dic_voisins
    global dic_routes
    global G

    tb_colis_a_livrer = []

    type_colis = None
    if _type_véhicule is TypeVéhicule.MOTO:
        type_colis = TypeColis.LETTRE
    elif _type_véhicule is TypeVéhicule.VOITURE:
        type_colis = TypeColis.PETIT_CARTON
    elif _type_véhicule is TypeVéhicule.CAMION:
        type_colis = TypeColis.GROS_CARTON

    for colis in _tb_colis:
        if colis.type_colis is type_colis:
            tb_colis_a_livrer.append(colis)

    tb_colis_a_livrer.sort(key=lambda x: (dic_lieux[x.lieu_livraison].heure_ouverture, [x.lieu_livraison]))

    print("\n")
    for colis in tb_colis_a_livrer:
        print(str(colis.type_colis) + " au lieu " + str(colis.lieu_livraison) + " à partir de " + str(
            dic_lieux[colis.lieu_livraison].heure_ouverture) + "h")

    print("\n")

    lieu_actuel = str(index_dépot)

    #                               année, mois, num_jours, heures, minutes
    temps_actuel = datetime.datetime(2020, 1, 0 + 1, dic_lieux[lieu_actuel].heure_ouverture, 0)

    temps_trajet_itinéraire = 0

    for colis in tb_colis_a_livrer:
        destination = str(colis.lieu_livraison)
        print("Départ " + lieu_actuel + " pour aller à " + destination)
        print("Heure de départ : " + str(temps_actuel))

        itinéraire = nx.astar_path(G, lieu_actuel, destination)
        print(itinéraire)

        for i in range(len(itinéraire) - 1):

            tb_routes = dic_voisins[itinéraire[i]][itinéraire[i + 1]]

            # exception
            if tb_routes is None:
                continue

            if tb_routes[0] is None:
                continue

            route = dic_routes[tb_routes[0]]
            temps_trajet = route.fctCalculerTempsTrajet(temps_actuel, _type_véhicule)
            print("Route " + str(tb_routes[0]) + " : " + str(temps_trajet) + " minutes")
            temps_trajet_itinéraire += temps_trajet

            temps_actuel = temps_actuel + datetime.timedelta(minutes=temps_trajet)

        print("Heure d'arrivée : " + str(temps_actuel))

        lieu_actuel = destination

        if dic_lieux[lieu_actuel].heure_ouverture > temps_actuel.hour:
            print("Attente avant ouverture")
            temps_actuel.replace(hour=dic_lieux[lieu_actuel].heure_ouverture)

        print("")

    print("Retour au dépôt")
    itinéraire = nx.astar_path(G, lieu_actuel, str(index_dépot))
    for i in range(len(itinéraire) - 1):

        tb_routes = dic_voisins[itinéraire[i]][itinéraire[i + 1]]

        # exception
        if tb_routes is None:
            continue

        if tb_routes[0] is None:
            continue

        route = dic_routes[tb_routes[0]]
        temps_trajet = route.fctCalculerTempsTrajet(temps_actuel, _type_véhicule)
        print("Route " + str(tb_routes[0]) + " : " + str(temps_trajet) + " minutes")
        temps_trajet_itinéraire += temps_trajet

        temps_actuel = temps_actuel + datetime.timedelta(minutes=temps_trajet)

    print("\nTemps de trajet de l'itinéraire " + str(temps_trajet_itinéraire) + " minutes")



fctGénérerTournée(tb_colis, TypeVéhicule.CAMION)

# fctGénérerTournée(dic_lieux, index_dépot, tb_colis, TypeColis.LETTRE, dic_voisins)


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

"""
def astar(_lieu_destination):

    # heure de départ
    heure_actuelle = tb_lieux[index_dépot].heure_ouverture

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
