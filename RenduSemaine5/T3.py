# liste des colonnes de la tables lignes de commandes 
import pandas as pd
datas = []
columns = ['idCommande','noligne','idProduit','quantite'] 
  
# creation de la table  
lignesCommandes = pd.DataFrame(columns) 

# affichage
print(lignesCommandes)

# transformation en fichier csv 
lignesCommandes.to_csv('lignesCommandes.csv', Index= False)
  
