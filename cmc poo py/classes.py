class Personne:
    # Constructeur
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    # Methode d'instance 
    def se_presenter(self):
        return f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans."

    # Methode de classe 
    @classmethod
    def depuis_chaine(cls, chaine):
        nom, age = chaine.split(", ")
        return cls(nom, int(age))  

    # Methode statique 
    @staticmethod
    def est_majeur(age):
        return age >= 18


# Creation d'une instance
Soultane = Personne("Soultane", 20)

# Appel de la methode d'instance
print(Soultane.se_presenter())  

# Appel de la methode de classe
Zineb = Personne.depuis_chaine("Zineb, 17")
print(Zineb.se_presenter())  

# Appel de la methode statique
print(Personne.est_majeur(20))  
print(Personne.est_majeur(15))  



class Vehucle:
    positon = "Tanger"
    def __init__(self, km, modele):
        self.km = km
        self.modele = modele
    def afficher(self):
      print(f"Le vehicule {self.modele} a {self.km} km")
      
      
    @classmethod
    def afficher_position(cls):
      print(f"Location en {cls.positon}")
      
    @staticmethod
    def age_vehicule(annee):
      return 2024 - annee 
    
porche = Vehucle(1000, "Porsche")
porche.afficher()
Vehucle.afficher_position()
print(Vehucle.age_vehicule(2022))          