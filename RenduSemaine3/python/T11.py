import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    database='ecommerce',
    user='root',
    password=''
)

cursor = conn.cursor()

# Récupération des données de la table Product en utilisant une jointure avec Categories
cursor.execute("SELECT idProduit, nomProduit, prix, poidsExpedition, idCategories FROM products P JOIN categories c ON c.nomCategorie = TRIM(SUBSTRING_INDEX(P.categorieProduit, '|', -1))")
result = cursor.fetchall()

# Insertion des données dans la table produit
insert_query = "INSERT INTO produit (idProduit, nomProduit, prix, poids, idCategories) VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE nomProduit=VALUES(nomProduit), prix=VALUES(prix), poids=VALUES(poids), idCategories=VALUES(idCategories)"

for row in result:
    # Vérification si l'idProduit existe déjà dans la table produit
    check_query = "SELECT idProduit FROM produit WHERE idProduit = %s"
    cursor.execute(check_query, (row[0],))
    existing_row = cursor.fetchone()

    if not existing_row:
        # Si l'idProduit n'existe pas, alors on peut l'insérer
        cursor.execute(insert_query, row)

conn.commit()
conn.close()
