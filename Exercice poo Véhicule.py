from datetime import date, timedelta


class Vehicule:
    def __init__(self, marque, modele, annee, prix_Location):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self._prix_Location = prix_Location

    @property
    def marque(self):
        return self.__marque

    @marque.setter
    def marque(self, nouvelleMarque):
        self.__marque = nouvelleMarque

    @property
    def modele(self):
        return self.__modele

    @modele.setter
    def modele(self, nouveauModele):
        self.__modele = nouveauModele

    @property
    def annee(self):
        return self.__annee

    @annee.setter
    def annee(self, nouvelleAnnee):
        if isinstance(nouvelleAnnee, int):
            self.__annee = nouvelleAnnee
        else:
            raise ValueError("L'année est invalide.")

    @property
    def prix_Location(self):
        return self._prix_Location

    @prix_Location.setter
    def prix_Location(self, nouvellePrixLocation):
        if nouvellePrixLocation > 0:
            self._prix_Location = nouvellePrixLocation

    def Afficher_details(self):
        print(f"° Marque: {self.__marque}\n"
              f"° Modèle: {self.__modele}\n"
              f"° Année: {self.__annee}\n"
              f"° Le prix de location: {self._prix_Location}DH")

    def Calculer_prix_location(self, duree):
        prix = self._prix_Location * duree
        if duree >= 7:
            return self.reduction_de_prix(prix)
        else:
            return prix

    def reduction_de_prix(self, prix):
        return prix - (prix * 10 / 100)


    def Augementer_tarif(self,pourcentage):
        if pourcentage > 0:
           Augementation = (self._prix_Location  * pourcentage )/ 100
           self._prix_Location += Augementation
           return (f"Le prix de location a été augmenté de {pourcentage}%\n"
                  f"Le nouveau prix de location est : {self._prix_Location}DH")
        else :
            return ("Le pourcentage d'augmentation doit être positif.")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix_Location, nombrePortes):
        super().__init__(marque, modele, annee, prix_Location)
        self.__nombrePortes = nombrePortes

    @property
    def nombrePortes(self):
        return self.__nombrePortes

    @nombrePortes.setter
    def nombrePortes(self, nouvelleNombre):
        if nouvelleNombre > 0:
            self.__nombrePortes = nouvelleNombre
        else:
            raise ValueError("Le nombre de portes doit être positif.")

    def Afficher_details(self):
        super().Afficher_details()
        print(f"° Nombre de portes: {self.__nombrePortes}")


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix_Location, cylindree):
        super().__init__(marque, modele, annee, prix_Location)
        self.__cylindree = cylindree

    @property
    def cylindree(self):
        return self.__cylindree

    @cylindree.setter
    def cylindree(self, nouvelleCylindree):
        if nouvelleCylindree > 0:
            self.__cylindree = nouvelleCylindree
        else:
            raise ValueError("La cylindrée doit être positive.")

    def Afficher_details(self):
        super().Afficher_details()
        print(f"Cyldindrée: {self.__cylindree}cm³")


class Camion(Vehicule):
    def __init__(self, marque, modele, annee, prix_Location, capacite_Chargement):
        super().__init__(marque, modele, annee, prix_Location)
        self.__capacite_Chargement = capacite_Chargement

    @property
    def capacite_Chargement(self):
        return self.__capacite_Chargement

    @capacite_Chargement.setter
    def capacite_Chargement(self, nouvelleCapacite):
        if nouvelleCapacite > 0:
            self.__capacite_Chargement = nouvelleCapacite
        else:
            raise ValueError("La capacité doit être positive.")

    def Afficher_details(self):
        super().Afficher_details()
        print(f"° Capacité de chargement: {self.__capacite_Chargement}")


class Location:
    __auto = 0

    def __init__(self, nom_client, vehicule, date_debut, date_fin, tarif_journalier):
        Location.__auto += 1
        self.__numero_location = Location.__auto
        self.__nom_client = nom_client
        self.__vehicule = vehicule
        self.__date_debut = date_debut
        self.__date_fin = date_fin
        self.__tarif_journalier = tarif_journalier

    @property
    def numero_location(self):
        return self.__numero_location

    @property
    def nom_client(self):
        return self.__nom_client

    @nom_client.setter
    def nom_client(self, nouvelleNomClient):
        self.__nom_client = nouvelleNomClient

    @property
    def vehicule(self):
        return self.__vehicule

    @vehicule.setter
    def vehicule(self, nouvelleVehicule):
        self.__vehicule = nouvelleVehicule

    @property
    def date_debut(self):
        return self.__date_debut

    @date_debut.setter
    def date_debut(self, nouvelleDateDebut):
        if isinstance(nouvelleDateDebut, date):
            self.__date_debut = nouvelleDateDebut
        else:
            raise ValueError("La date de début de location est invalide.")

    @property
    def date_fin(self):
        return self.__date_fin

    @date_fin.setter
    def date_fin(self, nouvelleDateFin):
        if isinstance(nouvelleDateFin, date):
            self.__date_fin = nouvelleDateFin
        else:
            raise ValueError("La date de fin de location est invalide.")

    @property
    def montant_total(self):
        if self.__date_debut and self.__date_fin and self.__tarif_journalier:
            duree = (self.__date_fin - self.__date_debut).days
            if duree < 0:
                raise ValueError("La date de fin doit être postérieure à la date de début.")
            return duree * self.__tarif_journalier
        else:
            return 0

    def afficher_location(self):
        return (
            f"° Numéro de location: {self.__numero_location}\n"
            f"° Nom du client: {self.__nom_client}\n"
            f"° Véhicule: {self.__vehicule.marque} {self.__vehicule.modele}\n"
            f"° Date de début: {self.__date_debut}\n"
            f"° Date de fin: {self.__date_fin}\n"
            f"° Montant total: {self.montant_total}DH"
        )
    def ProlongerLocation(self,joursSupplimentaire):
        if joursSupplimentaire > 0 :
            self.__date_fin +=timedelta(days=joursSupplimentaire)
            return (f"La durée de location a été prolongé de {joursSupplimentaire} \n"
                    f"la nouvelle date de fin est :{self.__date_fin}")

        else :
            return (f"Le nombre des jours supplimentaires doit etre positive.")

liste_Location = []

def afficher_menu():
    print("Menu :")
    print("a. Ajouter une location")
    print("b. Afficher la liste des locations")
    print("c. Rechercher une location par le numéro")
    print("d. Augmenter le prix d'une location")
    print("e. Prolonger la durée d'une location")
    print("f. Afficher le chiffre d'affaire général")
    print("g. Quitter")

choix = -1
while choix != 0:
    afficher_menu()
    try:
        choix = int(input("Donner un choix : "))
        match choix:
            case 1:
                print("Ajouter une location...")
            case 2:
                print("Afficher la liste des locations...")

            case 3:
                print("Rechercher une location par le numéro...")
            case 4:
                print("Augmenter le prix d'une location...")
            case 5:
                print("Prolonger la durée d'une location...")
            case 6:
                print("Afficher le chiffre d'affaire général...")
            case 0:
                print("Quitter le programme.")
                break

            case _:
                print("Choix invalide, veuillez réessayer.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")




voiture = Voiture("Toyota", "Corolla", 2022, 50, 4)
moto = Moto("dacia", "duster", 2009, 30, 321)
camion = Camion("Volvo", "FH", 2020, 150, 20000)


print("Avant augmentation :")
print("Détails de la voiture :")
voiture.Afficher_details()

print("\nDétails de la moto :")
moto.Afficher_details()

print("\nDétails du camion :")
camion.Afficher_details()


print("\nAugmenter les tarifs de 10%...")

voiture.Augementer_tarif(10)
moto.Augementer_tarif(10)
camion.Augementer_tarif(10)


print("\nAprès augmentation :")
print("Détails de la voiture :")
voiture.Afficher_details()

print("\nDétails de la moto :")
moto.Afficher_details()

print("\nDétails du camion :")
camion.Afficher_details()


