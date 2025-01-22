import math

a = int(input("Entrez a, non nul: "))
b = int(input("Entrez b: "))
c = int(input("Entrez c: "))

# Calculer le discriminant et assigner la valeur dans la variable "delta"
# delta = ...
delta = (b**2 - 4*a*c)
# Déterminer la condition (bool) qui correspond à aucune solution de l'équation et mettre la valeur dans la variable "naPasDeSolution"
# naPasDeSolution = ...
if delta < 0 :
    naPasDeSolution = delta
if naPasDeSolution:
    # ces ligne de code seront executé si il y'a aucune racine
    # afficher sur l'écran "Aucune racine"
    # print("Aucune racine")
    print('Aucune racine')
    pass
elif delta == 0:
    # Déterminer la condition (bool) qui correspond à une unique solution de l'équation et mettre la valeur dans "aUneSeuleSolution"
    # aUneSeuleSolution = ...
    aUneSeuleSolution = delta
    if aUneSeuleSolution:
        # ces ligne de code seront executé si il y'a une seule racine
        # afficher sur l'écran "Une seule racine"
        # print("Une seule racine")
        # assigner a la variable x1 la valeur de la racine
        # x1 = ...
        # print(x1)
        print('une seule racine')
        x1= (-b + math.sqrt(delta))/2*a
        print(x1)
        pass
elif delta > 0 :
        # Déterminer la condition (bool) qui correspond à deux solutions de l'équation et mettre la valeur dans "aDeuxSolutions"
        # aDeuxSolutions = ..
        aDeuxSolutiions= delta
        if aDeuxSolutions:
            # afficher sur l'écran "Deux racines"
            # print("Deux racines")
            # calculer la prmiere racine, assigner la a "x1"
            # x1 = ...
            # calculer la deuxieme racine, assigner la a "x2"
            # x2 = ...
            # print(x1, x2)
            print('deux racine')
            x1= (-b + math.sqrt(delta))/2*a
            x2= (-b - math.sqrt(delta))/2*a
            print(x1,x2)
            pass

# Exemple d'utilisation:
# Pour a = 1, b = -3, c = 2
# delta = 1
# Deux racines
# x1 = 1.0, x2 = 2.0
