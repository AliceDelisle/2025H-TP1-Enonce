secondes = int(input("Entrez un nombre de secondes : "))

# Ne pas modifier.
annees = semaines = jours = heures = minutes = 0

# TODO: Assigner à la variable "annees" le nombre d'années
annees= round(secondes/31536000)
# TODO: Assigner à la variable "semaines" le nombre de semaines restantes
secondes_restante = secondes % 31536000
semaines = secondes_restante// 604800
# TODO: Assigner à la variable "jours" le nombre de jours restants
secondes_restante = secondes % 604800
jours= secondes_restante// 86400
# TODO: Assigner à la variable "heures" le nombre d'heures restantes
secondes_restante = secondes % 86400
heures= secondes_restante // 3600
# TODO: Assigner à la variable "minutes" le nombre de minutes restantes
secondes_restante = secondes % 3600
minutes= secondes_restante// 60
# TODO: Assigner à la variable "secondes" le nombre de secondes restantes
secondes= secondes_restante % 60 
# TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
# Exemple: print(annees, semaines, jours, heures, minutes, secondes)
print(annees, semaines, jours, heures, minutes, secondes)