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

cursor.execute("SELECT idProduit FROM Produit")
products = cursor.fetchall()

for order in orders:
    # Sélectionner les lignes existantes pour cette commande
    cursor.execute("SELECT noLigne FROM LignesCommande WHERE idCommande = %s", (order[0],))
    existing_line_numbers = [row[0] for row in cursor.fetchall()]

    # Générer des numéros de ligne uniques pour cette commande
    available_line_numbers = list(set(range(1, 4)) - set(existing_line_numbers))
    line_numbers_to_generate = random.sample(available_line_numbers, k=random.randint(1, min(len(available_line_numbers), 3)))

    for line_number in line_numbers_to_generate:
        product = random.choice(products)[0]
        quantity = random.randint(1, 4)

        cursor.execute("INSERT INTO LignesCommande (idCommande, noLigne, quantite, idProduit) VALUES (%s, %s, %s, %s)",
        (order[0], line_number, quantity, product))

conn.commit()
conn.close()
