import json


# Définition de la classe Livre
class Livre:
    def __init__(self, titre, auteur, categorie):
        # Initialisateur de la classe Livre.
        # Il crée une nouvelle instance de Livre avec les propriétés spécifiées.
        self.titre = titre
        self.auteur = auteur
        self.categorie = categorie
        self.est_disponible = True
        self.emprunteur = None

    def __repr__(self):
        # La méthode spéciale __repr__ fournit une représentation officielle de l'objet.
        # Elle est utilisée pour créer une chaîne qui peut être utilisée pour recréer l'objet.
        return f"Livre('{self.titre}', '{self.auteur}', '{self.categorie}')"


# Définition de la classe BddBibliotheque
class BddBibliotheque:
    _instance = None

    def __new__(cls):
        # Singleton : Assure qu'il n'y a qu'une seule instance de la classe BddBibliotheque
        if cls._instance is None:
            cls._instance = super(BddBibliotheque, cls).__new__(cls)
            cls._instance.livres = []  # Liste des livres dans la bibliothèque
            cls._instance.utilisateurs = []  # Liste des utilisateurs enregistrés

        return cls._instance

    def ajouter_livre(self, livre):
        # Ajoute un livre à la liste des livres dans la bibliothèque
        self.livres.append(livre)

    def retirer_livre(self, livre):
        # Retire un livre de la liste des livres dans la bibliothèque
        self.livres.remove(livre)

    def enregistrer_utilisateur(self, utilisateur):
        # Enregistre un utilisateur dans la bibliothèque
        self.utilisateurs.append(utilisateur)

    def is_livre_disponible(self, livre):
        # Vérifie si un livre est disponible
        return livre.est_disponible

    def emprunter_livre(self, utilisateur, livre):
        # Emprunte un livre à un utilisateur
        if self.is_livre_disponible(livre):
            livre.est_disponible = False
            livre.emprunteur = utilisateur
            print(f"{utilisateur.prenom} {utilisateur.nom} a emprunté le livre '{livre.titre}'.")
        else:
            print(f"Désolé, le livre '{livre.titre}' n'est pas disponible.")

    def retourner_livre(self, livre):
        # Retourne un livre à la bibliothèque
        if livre.est_disponible:
            print(f"Le livre '{livre.titre}' est déjà disponible. Veuillez vérifier.")
        else:
            livre.est_disponible = True
            livre.emprunteur = None
            print(f"Le livre '{livre.titre}' a été retourné à la bibliothèque.")

    def rechercher_livres(self, strategie):
        # Exécute une stratégie de recherche sur la liste des livres
        return strategie.execute(self.livres)

    def sauvegarder_livres(self):
        # Sauvegarde la liste des livres dans un fichier JSON
        with open('bibliotheque.json', 'w') as file:
            livres_json = [{
                'titre': livre.titre,
                'auteur': livre.auteur,
                'categorie': livre.categorie,
                'est_disponible': livre.est_disponible
            } for livre in self.livres]
            json.dump(livres_json, file)
