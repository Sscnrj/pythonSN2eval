from bibliotheque import Livre, BddBibliotheque
from strategie_recherche import RechercheParTitre, RechercheParAuteur, RechercheParCategorie
from utilisateur import Utilisateur
from observateur import ObservateurDisponibiliteLivre

# Singleton : Création d'une instance unique de la base de données de la bibliothèque
bdd_bibliotheque = BddBibliotheque()

while True:
    print("\n--- Menu Principal ---")
    print("1. Ajouter un livre")
    print("2. Retirer un livre")
    print("3. Rechercher un livre")
    print("4. Enregistrer un utilisateur")
    print("5. Emprunter un livre")
    print("6. Retourner un livre")
    print("7. Sauvegarder l'état")
    print("8. Quitter")

    choix = input("Choisissez une option (1-8): ")

    if choix == '1':
        # Option pour ajouter un livre à la bibliothèque
        titre = input("Titre du livre: ")
        auteur = input("Auteur du livre: ")
        categorie = input("Catégorie du livre: ")
        livre = Livre(titre, auteur, categorie)
        bdd_bibliotheque.ajouter_livre(livre)
        print(f"Le livre '{titre}' a été ajouté à la bibliothèque.")

    elif choix == '2':
        # Option pour retirer un livre de la bibliothèque
        titre = input("Titre du livre à retirer: ")
        livre_a_retirer = next(
            (livre for livre in bdd_bibliotheque.livres if livre.titre.lower() == titre.lower()), None)
        if livre_a_retirer:
            bdd_bibliotheque.retirer_livre(livre_a_retirer)
            print(f"Le livre '{titre}' a été retiré de la bibliothèque.")
        else:
            print(f"Le livre '{titre}' n'a pas été trouvé dans la bibliothèque.")

    elif choix == '3':
        # Option pour rechercher un livre dans la bibliothèque
        print("1. Par titre")
        print("2. Par auteur")
        print("3. Par catégorie")
        choix_recherche = input("Choisissez le type de recherche (1-3): ")

        if choix_recherche == '1':
            terme_recherche = input("Entrez le titre du livre à rechercher : ")
            strategie_recherche = RechercheParTitre(terme_recherche)

        elif choix_recherche == '2':
            terme_recherche = input("Entrez le nom de l'auteur à rechercher : ")
            strategie_recherche = RechercheParAuteur(terme_recherche)

        elif choix_recherche == '3':
            terme_recherche = input("Entrez la catégorie à rechercher : ")
            strategie_recherche = RechercheParCategorie(terme_recherche)

        else:
            print("Option de recherche invalide.")
            continue

        # Exécuter la recherche dans la base de données
        resultats_recherche = bdd_bibliotheque.rechercher_livres(strategie_recherche)

        # Afficher les résultats de la recherche
        if resultats_recherche:
            print("\nRésultats de la recherche:")
            for livre in resultats_recherche:
                print(f"- {livre.titre} par {livre.auteur}, Catégorie: {livre.categorie}")
        else:
            print("Aucun résultat trouvé.")

    elif choix == '4':
        # Option pour enregistrer un utilisateur
        nom_utilisateur = input("Nom de l'utilisateur: ")
        prenom_utilisateur = input("Prénom de l'utilisateur: ")
        utilisateur = Utilisateur(nom_utilisateur, prenom_utilisateur)
        bdd_bibliotheque.enregistrer_utilisateur(utilisateur)
        print(f"L'utilisateur '{nom_utilisateur}' a été enregistré.")

    elif choix == '5':
        # Option pour emprunter un livre
        nom_utilisateur = input("Nom de l'utilisateur emprunteur: ")
        prenom_utilisateur = input("Prénom de l'utilisateur emprunteur: ")
        titre_livre = input("Titre du livre à emprunter: ")

        utilisateur_emprunteur = next((user for user in bdd_bibliotheque.utilisateurs if
                                       user.nom.lower() == nom_utilisateur.lower() and user.prenom.lower() == prenom_utilisateur.lower()),
                                      None)

        livre_emprunter = next((livre for livre in bdd_bibliotheque.livres if
                               livre.titre.lower() == titre_livre.lower() and livre.est_disponible),
                              None)

        if utilisateur_emprunteur and livre_emprunter:
            bdd_bibliotheque.emprunter_livre(utilisateur_emprunteur, livre_emprunter)
        else:
            print("Utilisateur non trouvé ou le livre n'est pas disponible.")

    elif choix == '6':
        # Option pour retourner un livre
        titre_livre = input("Titre du livre à retourner: ")
        livre_retourner = next(
            (livre for livre in bdd_bibliotheque.livres if livre.titre.lower() == titre_livre.lower()),
            None)
        if livre_retourner:
            bdd_bibliotheque.retourner_livre(livre_retourner)
        else:
            print("Livre non trouvé.")

    elif choix == '7':
        # Option pour sauvegarder l'état de la bibliothèque
        bdd_bibliotheque.sauvegarder_livres()
        print("L'état de la bibliothèque a été sauvegardé.")

    elif choix == '8':
        # Option pour quitter le programme
        print("Au revoir!")
        break

    else:
        # Gestion d'une option invalide
        print("Option invalide. Veuillez choisir une option de 1 à 8.")
