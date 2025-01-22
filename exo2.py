# Demandez à l'utilisateur d'entrer le niveau de charge actuel de la batterie
print('veuillez entrée votre niveau de baterie.')
niveau_de_baterie= int(input())
# Vérifiez si le niveau de charge est valide
if 0 <=niveau_de_baterie  <= 100:
    'niveau de baterie est valide'
else: 'niveau de baterie est invalide'
# Arrondir le pourcentage à la dizaine la plus proche
niveau_de_baterie_arondi= round(niveau_de_baterie,-1)
# Calculer le nombre de barres
nombre_de_barre = niveau_de_baterie_arondi // 10
# Afficher la représentation graphique de la charge de la batterie
espace= ''
for i in range(1,2):
    if niveau_de_baterie_arondi %10 == 0:
        print('['nombre_de_barre * '❚'+ espace']\n 'niveau_de_baterie + '%')
        
    else: print('['(nombre_de_barre%10)*espace']\n 'niveau_de_baterie + '%') 
     



    


# Exemple d'utilisation :
# Si l'utilisateur entre 76, la sortie sera :
# [❚❚❚❚❚❚❚❚     ]
# 76 %