import mysql.connector
import random

conn = mysql.connector.connect(
    host='localhost',
    database='ecommerce',
    user='root',
    password=''
)

cursor = conn.cursor()

cursor.execute("SELECT idCommande FROM Commandes")
orders = cursor.fetchall()

cursor.execute("SELECT idProduit FROM Produits")
products = cursor.fetchall()

for order in orders:
    line_numbers = random.sample(range(1, 4), k=random.randint(1, 3))  # Générer 1 à 3 numéros de ligne uniques
    
    for line_number in line_numbers:
        product = random.choice(products)[0]
        quantity = random.randint(1, 4)
        
        cursor.execute("INSERT INTO LignesCommande (noLigne, quantite, idProduit) VALUES (%s, %s, %s)",
                       (line_number, quantity, product))

conn.commit()
conn.close()
