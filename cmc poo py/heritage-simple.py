
class Utilisateur:
    def __init__(self, nom: str, age: int) :
        self.nom_user = nom
        self.age_user = age

    def salutation(self) :
        print(f"Bonjour {self.nom_user}, tu as {self.age_user} ans")


class Client(Utilisateur):
    def __init__(self, nom: str, age: int, mail: str) :
        super().__init__(nom, age)
        self.mail = mail
    def salutation2(self) :
        super().salutation() 
        print( f" et ton mail est {self.mail}")
        
        
client1 = Client("Soultane", 19, "4s4zI@gmail.com")
client1.salutation2()


