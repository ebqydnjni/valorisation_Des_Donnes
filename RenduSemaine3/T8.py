import mysql.connector
import random
from datetime import datetime, timedelta

conn = mysql.connector.connect(
    host='localhost',
    database='ecommerce',
    user='root',
    password=''
)

cursor = conn.cursor()

statuses = ['en cours', 'payée', 'livrée', 'annulée']

# Récupérer les ID des clients
cursor.execute("SELECT idClient FROM Clients")
clients = cursor.fetchall()

for client in clients:
    num_orders = random.randint(0, 5)
    
    for _ in range(num_orders):
        random_date = datetime(2020, 1, 1) + timedelta(days=random.randint(0, 975))
        status = random.choice(statuses)
        
        cursor.execute("INSERT INTO Commandes (dateCommande, statut, idClient) VALUES (%s, %s, %s)",
                       (random_date.strftime('%Y-%m-%d'), status, client[0]))

conn.commit()
conn.close()
