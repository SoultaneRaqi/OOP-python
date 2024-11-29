class Perssone :
  #Attribut de classe (partage par toutes les instances)
  nom_etablissement = "CMC Tanger" #Cet attribut est partage par toutes les instances
  def __init__(self,name ,prenom ,age):
    #Attribut d'instance (Specifique a chaque instance)
    self.name = name
    self.prenom = prenom
    self.age = age
    
  def afficher(self):  
    # Methode afficher les informations de la personne
    print(f"Nom : {self.name} , Prenom : {self.prenom} , Age : {self.age} , Etablissement : {Perssone.nom_etablissement}")

Soultane = Perssone("Soultane" , "Raqi" , 20)
"""Soultane.afficher()"""    
# Acces aux attributs d'instance 
print(f"Soultane : {Soultane.name}  {Soultane.prenom} , Age : {Soultane.age}")
# Acces aux attributs de classe
print(f"Nom etablissement de Soultane: {Perssone.nom_etablissement}")
# Modifier l'attribut de classe 
Perssone.nom_etablissement = "CMC TTH"
# Affichage apres modification de l'attribut de classe
print("\nApres la modification de l'attribut de classe :")
print(f"Nom etablissement de Soultane: {Perssone.nom_etablissement}")
