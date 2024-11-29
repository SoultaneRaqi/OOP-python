import random
import math 
import sys
import os
import time
import calendar
import urllib.request
import re
import profile


# Exemple avec le module random :

print("Exemple avec le module random : Generer un nombre aleatoire")
random_number = random.randint(1, 10)
print("Le nombre aleatoire est : " , random_number)

# Exemple avec le module math :

print("\nExemple avec le module math : Calculer le cosinus d'un angle (en radians)")
angle= math.pi /4  #45 degres
cos_value = math.cos(angle)
print("Le cosinus de l'angle est : ", cos_value)

# Exemple avec le module sys :

print("\nExemple avec le module sys : Afficher la version de Python")
print("La version de Python est : ", sys.version)

# Exemple avec le module os :

print("\nExemple avec le module os : Afficher le chemin du repertoire courant")
current_directory = os.getcwd()
print("Le chemin du repertoire courant est : ", current_directory)

# Exemple avec le module time :

print("\nExemple avec le module time : Afficher l'heure actuelle")
current_time = time.strftime("%H:%M:%S" , time.localtime())
print("L'heure actuelle est : ", current_time)

# Exemple avec le module calendar :

print("\nExemple avec le module calendar : Afficher le calendrier du mois de decembre 2024")
calendar_month = calendar.month(2024, 12)
print( calendar_month)

# Exemple avec le module urllib.request (urlib.request en Python 3) :

print("\nExemple avec urllib2 : Telecharger une page web")
url = 'https://www.example.com'
response = urllib.request.urlopen(url)
html_content = response.read()
print("Le contenu de la page web est : ", html_content[:200]) # Afficher les 200 premiers caracteres

# Exemple avec le module re :

print("\nExemple avec le module re : Rechercher un mot dans un texte")
text = "Hello, world!"
pattern = re.compile(r"world")
matches = pattern.findall(text)
print("Mots trouvees : ", matches)

# Exemple avec le module profile :

print("\nExemple avec le module profile : Mesurer le temps d'execution d'un fonction")
def slow_function():
  time.sleep(2)
  
profile.run('slow_function()')  

