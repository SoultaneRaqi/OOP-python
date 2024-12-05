class Adherent :
  def __init__(self, nom , prenom , age ):
    self.__nom = nom            #public= self.X=X
    self.__prenom = prenom      #prive= self.__X=X
    self.__age = age            #protected= self._X=X
  
  # Getters accedder aux attributs securises au niveau de la classe :
  # Setters pour la modifaction des attributs au niveau de la classe :
  
  
  """def get_nom(self):
    return self.__nom
  def set_nom(self,nom):
    self.__nom = nom     
    
  def get_prenom(self):             #Getters et setter sans decorateur
    return self.__prenom
  def set_prenom(self,prenom):
    self.__prenom = prenom
    
  def get_age(self):
    return self.__age
  def set_age(self,age):
    self.__age = age"""  
  
  
  # Getters  avec decorateur
  @property
  def nom(self):
    return self.__nom
  @property
  def prenom(self): 
    return self.__prenom                                                                                    
  @property
  def age(self):
    return self.__age  
  
  # Setters avec decorateur                       
  @nom.setter
  def nom(self,nom):
    self.__nom = nom
  @prenom.setter
  def prenom(self,prenom):
    self.__prenom = prenom
  @age.setter
  def age(self,age):
    self.__age = age
    
  # Suppression d attribut : 
  """@nom.deleter
  def nom(self):
    del self.__nom"""
  
  # deletion de l attribut : 
  # @age.deleter
  # def age(self):
  # del self.__age
  
   #Methode d affichage
  def afficher(self):
    print(f"Nom : {self.nom} , Prenom : {self.prenom} , Age : {self.age}")
   #Methode de verification d age  
  def est_majeur(self):
      x = self.__age >= 18
      if x == True:
        print("Vous etes majeur")
      else:
        print("Vous etes mineur")
        

# Creation d'une instance       
A1 =Adherent("Soultane" , "Raqi" , 19)
A1.afficher()
print(A1.est_majeur())

# Modification des attributs ( nom ) par les setters
A1.nom = "Zineb"
A1.afficher()



   