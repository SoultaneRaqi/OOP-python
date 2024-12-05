class EtreVivant:
    def __init__(self, taille, poid):
        self.taille = taille
        self.poid = poid

    def mesures(self):
        print(f"Taille : {self.taille} cm , Poids : {self.poid} kg")

class Personne(EtreVivant):
    def __init__(self, nom, cin, dateNaissance, taille, poid):
        # Appel  constructeur de EtreVivant
        super().__init__(taille, poid)
        self.nom = nom
        self.cin = cin
        self.dateNaissance = dateNaissance

    def age(self):
        print(f"Age : {2024 - self.dateNaissance} ans")

class Etudiant(Personne):
    def __init__(self, nom, cin, dateNaissance, taille, poid, notePoo, noteAlgo):
        # Appel  constructeur de Personne
        super().__init__(nom, cin, dateNaissance, taille, poid)
        self.notePoo = notePoo
        self.noteAlgo = noteAlgo
        
    def moyenne(self):
        print(f"Votre moyenne : {(self.notePoo + self.noteAlgo) / 2}")
        
    def informations(self):
        self.mesures()  # Appel  methode de EtreVivant
        self.age()      # Appel  methode de Personne
        self.moyenne()  # Methode  Etudiant



Soultane = Etudiant("Soultane", "ka5555", 2004, 174, 70, 19.25, 18)
Soultane.informations()
