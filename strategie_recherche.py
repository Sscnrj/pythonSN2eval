from abc import ABC, abstractmethod


class StrategieRecherche(ABC):
    @abstractmethod
    def execute(self, livres):
        # Méthode abstraite à implémenter dans les classes dérivées.
        # Elle spécifie comment une stratégie de recherche doit être exécutée.
        pass


# Implémentation d'une stratégie de recherche par titre
class RechercheParTitre(StrategieRecherche):
    def __init__(self, titre):
        self.titre = titre

    def execute(self, livres):
        # La méthode execute() est implémentée pour la recherche par titre.
        # Elle retourne une liste des livres dont le titre correspond au titre spécifié.
        return [livre for livre in livres if self.titre.lower() == livre.titre.lower()]


# Implémentation d'une stratégie de recherche par auteur
class RechercheParAuteur(StrategieRecherche):
    def __init__(self, auteur):
        self.auteur = auteur

    def execute(self, livres):
        # La méthode execute() est implémentée pour la recherche par auteur.
        # Elle retourne une liste des livres dont l'auteur correspond à l'auteur spécifié.
        return [livre for livre in livres if self.auteur.lower() == livre.auteur.lower()]


# Implémentation d'une stratégie de recherche par catégorie
class RechercheParCategorie(StrategieRecherche):
    def __init__(self, categorie):
        self.categorie = categorie

    def execute(self, livres):
        # La méthode execute() est implémentée pour la recherche par catégorie.
        # Elle retourne une liste des livres dont la catégorie correspond à la catégorie spécifiée.
        return [livre for livre in livres if self.categorie.lower() == livre.categorie.lower()]

