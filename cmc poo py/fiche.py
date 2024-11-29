from func import*
from utils.operations import*
age = int(input("Quel est votre age ? : "))
print(f"Vous avez {age} ans")
age_plus_un = ajoute_un(age)  
print(f"Dans un an, vous aurez {age_plus_un} ans")
age_plus_deux = ajoute_deux(age)
print(f"Dans deux ans, vous aurez {age_plus_deux} ans")
