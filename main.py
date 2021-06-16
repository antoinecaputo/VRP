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
    GROS_CARTON = 1
    PETIT_CARTON = 2
    LETTRE = 3


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

# Un lieu peut être un dépot ou un point de livraison
# # Un point de livraison a des horaires d'ouverture et de fermeture
class Lieu:

    tb_routes = []

    def __init__(self, _type_lieu, _heure_début, _heure_fin):
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
    tb_lieux_connectés = [None] * 2

    tba_info_trafic = {}

    def __init__(self, _type_route, _longueur, _lieu1, _lieu2):
        self.type_route = _type_route
        self.longueur = _longueur
        self.tb_lieux_connectés[0] = _lieu1
        self.tb_lieux_connectés[1] = _lieu2


class TypeRoute(Enum):
    AUTOROUTE = 1  # 130
    NATIONALE = 2  # 80
    DEPARTEMENTALE = 3  # 80
    COMMUNALE = 4  # 50


"""
class InfoTrafic:
    def __init__(self, _date, _nb_véhicules):
        self.date = _date
        self.nb_véhciules = _nb_véhicules

"""
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

def fctGénérerDonnées(_nb_lieux):

    tb_lieux = {}

    # Création des points de livraison
    for i in range(97, 97+_nb_lieux):
        lieu = Lieu(TypeLieu.LIVRAISON, 9, 18)
        tb_lieux[chr(i)] = lieu

    for lieu in tb_lieux:
        while
fctGénérerDonnées(3)


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
