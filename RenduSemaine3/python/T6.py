import mysql.connector
import random
conn = mysql.connector.connect(
    host='localhost',
    database='ecommerce',
    user='root',
    password=''
)
cursor = conn.cursor()
# Obtenir une liste aléatoire de villes et régions à partir de la table 'Villes'
cursor.execute("SELECT ville, region FROM Villes")
villes = cursor.fetchall()
# Insérer des villes et régions aléatoires pour chaque client
cursor.execute("SELECT idClient FROM Clients")
clients = cursor.fetchall()
for client in clients:
    ville, region = random.choice(villes)
    cursor.execute("UPDATE Clients SET ville= %s, region = %s WHERE idClient = %s", (ville, region, client[0]))

conn.commit()
conn.close()
