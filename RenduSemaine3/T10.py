import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    database='ecommerce',
    user='root',
    password=''
)

cursor = conn.cursor()

cursor.execute("SELECT categorieProduit FROM Produits")
categories = cursor.fetchall()

for category in categories:
    category_list = category[0].split(' | ')

    parent_id = None

    for cat in category_list:
        # Vérifier si la catégorie existe déjà
        cursor.execute("SELECT idCategories FROM Categories WHERE nomCategorie = %s AND idCategorieMere = %s", (cat, parent_id))
        cat_id = cursor.fetchone()

        if cat_id:
            parent_id = cat_id[0]
        else:
            # Insérer la catégorie uniquement si elle n'existe pas encore
            cursor.execute("INSERT INTO Categories (nomCategorie, idCategorieMere) VALUES (%s, %s)", (cat, parent_id))
            parent_id = cursor.lastrowid  # Récupérer l'ID de la nouvelle catégorie

conn.commit()
conn.close()
