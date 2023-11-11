## Importation de la fonction random
from random import choice

# CE programme genere aleatoirement des avis en fontion du joueur et de son post 
noms = ["Sadio Mane","Aldiouma Mbaye","GANA GUEYE","NAMPALYS MENDY","PAPE MATAR SARR", "EDOUARD MENDY", "ISMAYLA SARR", "HABIB DIALLO"]
post = ["GARDIEN", "DEFENSSEUR", "MILIEUX", "ATTAQUANT"]
avis = ["Il serait un bon joueur de football.", "Il aura du mal à s'adapter.", "Il n'est pas fait pour ce poste:)"]

# Génération aléatoire  pour mes trois listes nom pos et avis
nom_aleatoire = choice(noms)
post_aleatoire = choice(post)
avis_aleatoire = choice(avis)

# Affichage de l'avis generer 
print("Nom :", nom_aleatoire)
print("post :", post_aleatoire)
print("avis :", avis_aleatoire)
