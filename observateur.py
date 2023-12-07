class Observer:
    def mettre_a_jour(self, message):
        # Méthode abstraite à implémenter dans les classes dérivées.
        pass


# Implémentation d'une classe d'observateur spécifique ObservateurDisponibiliteLivre
class ObservateurDisponibiliteLivre(Observer):
    def __init__(self, utilisateur):
        # Initialisateur de la classe ObservateurDisponibiliteLivre
        self.utilisateur = utilisateur

    def mettre_a_jour(self, message):
        # Implémentation de la méthode mettre_a_jour pour informer l'utilisateur de la disponibilité du livre.
        # Cette méthode est appelée lorsque l'état observé change (dans ce cas, la disponibilité d'un livre).
        print(f"Monsieur/Madame {self.utilisateur.nom}, le livre '{message}' est maintenant disponible. Vous pouvez l'emprunter.")

