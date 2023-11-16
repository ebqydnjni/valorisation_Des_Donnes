-- Active: 1698010070526@@127.0.0.1@3306@ecommerce

### Quel sont les clients qui on fait plus de commandes ?
   SELECT c.idClient, c.prenom, c.nom, COUNT(co.idCommande) AS NombreCommandes
   FROM Clients c
   JOIN Commandes co ON c.idClient = co.idClient
   GROUP BY c.idClient
   ORDER BY NombreCommandes DESC
   LIMIT 5;
   

###  nombre de commande fait par un client :
   SELECT * FROM Commandes WHERE idClient = '5f10e9D33fC5f2b';
   

### liste des categ_produits avec le nbr de produit pour chaque categorie
   SELECT c.nomCategorie, COUNT(p.idProduit) AS NombreProduits
   FROM Categories c
   LEFT JOIN Produit p ON c.idCategories = p.idCategories
   GROUP BY c.nomCategorie;
   

### Quel est la moyenne des prix des ADD produit pour chaque categories  ?
   SELECT c.nomCategorie, AVG(p.prix) AS PrixMoyen
   FROM Categories c
   JOIN Produit p ON c.idCategories = p.idCategories
   GROUP BY c.nomCategorie;
   
###  les 20 produits les plus vendue 
   SELECT p.nomProduit, SUM(lc.quantite) AS TotalQuantiteVendue
   FROM Produit p
   JOIN LignesCommande lc ON p.idProduit = lc.idProduit
   GROUP BY p.nomProduit
   ORDER BY TotalQuantiteVendue DESC
   LIMIT 20;
   

###  identifier le ou les  clients qui ont  acheter un produit connaissant la categorie  
SELECT c.idClient, c.prenom, c.nom, co.idCommande, ca.nomCategorie
FROM Clients c
JOIN Commandes co ON c.idClient = co.idClient
JOIN LignesCommande lc ON co.idCommande = lc.idCommande
JOIN Produit p ON lc.idProduit = p.idProduit
JOIN Categories ca ON p.idCategories = ca.idCategories
WHERE ca.nomCategorie = 'Fuse & Perler Beads';
    

###  la liste des commande à une periode donnes 
SELECT * FROM Commandes WHERE dateCommande BETWEEN '2021-03-19' AND '2022-03-21';
    
### la Liste des produits dont le poids est supérieur  à 8
 SELECT * FROM Produit WHERE poids > 8;
    

###  Nombre de commandes selon le statut 
SELECT statut, COUNT(*) AS NombreCommandesParStatut
FROM Commandes
GROUP BY statut;
    

### liste des Clients n'ayant pas encore effectué de commandes   
SELECT c.idClient, c.prenom, c.nom
FROM Clients c
LEFT JOIN Commandes co ON c.idClient = co.idClient
WHERE co.idCommande IS NULL;
    

### Liste des produits dans une catégorie spécifique triée par prix décroissant :
    
SELECT p.nomProduit, p.prix
FROM Produit p
JOIN Categories c ON p.idCategories = c.idCategories
WHERE c.nomCategorie = 'Arts, Crafts & Sewing'
ORDER BY p.prix DESC;
    

