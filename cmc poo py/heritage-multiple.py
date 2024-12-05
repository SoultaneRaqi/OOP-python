class Perssone:
  def __init__(self,nom ,cin ,dateNaissance):
    self.nom = nom
    self.cin = cin
    self.dateNaissance = dateNaissance
  
  def age(self):
    print ( f"Age : {2024 - self.dateNaissance} ans")
    
class EtreVivant:
  def __init__(self,taille , poids):
    self.taille = taille
    self.poids = poids
  def mesures(self):
    print (f"Taille : {self.taille} cm , Poids : {self.poids} kg") 
    
class Etudiant(Perssone , EtreVivant):
  def __init__(self,nom ,cin ,dateNaissance ,taille ,poids, notePoo, noteAlgo):
    Perssone.__init__(self,nom ,cin ,dateNaissance)
    EtreVivant.__init__(self,taille ,poids)
    self.notePoo = notePoo
    self.noteAlgo = noteAlgo
  def moyenne(self):
    print (f"Votre moyenne : {float(self.notePoo + self.noteAlgo) / 2}") 
  def informations(self):
    super().mesures()
    super().age()
    self.moyenne() 
            
        
Soultane = Etudiant("Soultane" , "ka5555" , 2004 , 174 , 70 , 19.25 , 18)
Soultane.informations()    