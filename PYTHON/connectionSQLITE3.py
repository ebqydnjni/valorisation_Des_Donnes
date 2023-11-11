
import sqlite3

try:
        # creation de la variables connection 
    connection = sqlite3.connect("ecommerce")
    ## creation de la variables cursor 
    cursor = connection.cursor()

    ## Pour inserer les requets sql 
    cursor.execute("SELECT * FROM products")

    ## req
    req = cursor.fetchone("SELECT * FROM products")
    ## Pour afficher un element specifique      
    print(f"le resultat est : {cursor.fetchon }")
    ## pour afficher tout la tables 
    req.fetchall()

    ## Appliquer le changement pour valider les changement apporter a la BD
    connection.commit()
except  Exception as e:
    print("[ERREUR]",e) 
    ## Pour revenir a la dernier commit 
    connection.rollback()
    
finally : 
    ## Fermer la connection a la base 
    connection.close()



