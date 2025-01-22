# Demandez à l'utilisateur d'entrer le niveau de charge actuel de la batterie
print('veuillez entrée votre niveau de batterie.')
niveau_de_batterie = int(input())
# Vérifiez si le niveau de charge est valide
if 0 <= niveau_de_batterie <= 100:
    print('niveau de baterie est valide')
else: print('niveau de baterie est invalide')
# Arrondir le pourcentage à la dizaine la plus proche
niveau_de_batterie_arondi= round(niveau_de_batterie,-1)
# Calculer le nombre de barres
nombre_de_barres = niveau_de_batterie_arondi // 10
# Afficher la représentation graphique de la charge de la batterie
for i in range(1,2):
    if niveau_de_batterie_arondi % 10 == 0:
        print('['+ nombre_de_barres* '❚' + (10- nombre_de_barres)* '' + ']')
        
     
print(niveau_de_batterie + '%')


    


# Exemple d'utilisation :
# Si l'utilisateur entre 76, la sortie sera :
# [❚❚❚❚❚❚❚❚     ]
# 76 % de charge de la batterie