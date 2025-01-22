# Demandez à l'utilisateur d'entrer le niveau de charge actuel de la batterie
print('Veuillez entrer votre niveau de batterie.')
niveau_de_batterie = int(input())
# Vérifiez si le niveau de charge est valide
if 0 <= niveau_de_batterie <= 100:
    print("Niveau de batterie est valide")
else:
    print("Niveau de batterie est invalide")
    exit()
# Arrondir le pourcentage à la dizaine la plus proche
niveau_de_batterie_arondi = round(niveau_de_batterie, -1)
# Calculer le nombre de barres
nombre_de_barres = niveau_de_batterie_arondi // 10
# Afficher la représentation graphique de la charge de la batterie
representation_graphique = "["
for i in range(10):
    if i < nombre_de_barres:
        representation_graphique += "❚"
    else:
        representation_graphique += " "
representation_graphique += "]"
print(representation_graphique)
print(str(niveau_de_batterie) + "%" )
# Exemple d'utilisation :
# Si l'utilisateur entre 76, la sortie sera:
# [❚❚❚❚❚❚❚❚  ]
# 76% 