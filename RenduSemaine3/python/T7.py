import mysql.connector
import random
import string
try :
    conn = mysql.connector.connect(
        host='localhost',
        database='ecommerce',
        user='root',
        password=''
    )

    cursor = conn.cursor()

    # Récupérer la liste des ID des clients
    cursor.execute("SELECT idClient FROM Clients")
    clients = cursor.fetchall()

    # Générer et attribuer des mots de passe aléatoires à chaque client
    for client in clients:
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        cursor.execute("UPDATE Clients SET mdp = %s WHERE idClient = %s", (password, client[0]))
        
except MC.Error as err:
    print("[ERREUR]", err)

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.commit()
        cursor.close()
        conn.close()


