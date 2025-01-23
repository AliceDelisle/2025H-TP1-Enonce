import math

# Constante de gravité
g = 9.8

# Demander la vitesse initiale de la boule
vitesse_initiale = float(input("qu\'elle est la vitesse initiale de la boule (m/s):"))

# Demander l'angle de lancement
angle_de_lancer = float(input("qu\'elle est l\'angle de lancement (en degré):"))
 
# Convertir l'angle en radians
angle_de_lancer_rad = (angle_de_lancer * math.pi)/180
# Calculer la distance maximale en x
distance_parcourue = (pow(vitesse_initiale,2)*math.sin(2*angle_de_lancer_rad))/g
# Afficher la distance maximale arrondie à 2 chiffres après la virgule
distance_parcourue_arondie = round(distance_parcourue,2)
print('La distance parcourue est:'+' '+ str(distance_parcourue_arondie)+ "m")
# Exemple:
# Pour une vitesse initiale de 10 m/s et un angle de 45 degrés
# La distance parcourue serait de 10.20m