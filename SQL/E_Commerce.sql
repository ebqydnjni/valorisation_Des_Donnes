-- Active: 1698010070526@@127.0.0.1@3306@ecommerce
CREATE DATABASE ecommerce;
USE ecommerce;

CREATE TABLE Clients(
   idClient VARCHAR(70),
   prenom VARCHAR(50),
   nom VARCHAR(50),
   email VARCHAR(50),
   telephone VARCHAR(50),
   dateNaissance DATE,
   mdp VARCHAR(50),
   ville_ VARCHAR(50) NOT NULL,
   pays VARCHAR(50) NOT NULL,
   PRIMARY KEY(idClient)
);

CREATE TABLE Commandes(
   idCommande VARCHAR(50),
   dateCommande DATE,
   statut VARCHAR(60),
   idClient VARCHAR(70) NOT NULL,
   PRIMARY KEY(idCommande),
   FOREIGN KEY(idClient) REFERENCES Clients(idClient)
);

CREATE TABLE Categories(
   idCategories INT,
   nomCategorie VARCHAR(50) NOT NULL,
   idCategorieMere INT NOT NULL,
   PRIMARY KEY(idCategories),
   FOREIGN KEY( idCategorieMere) REFERENCES Categories(idCategories)
);

CREATE TABLE Produit(
   idProduit INT,
   nomProduit VARCHAR(50) NOT NULL,
   prix INT NOT NULL,
   poids DECIMAL(15,2) NOT NULL,
   idCategories INT NOT NULL,
   PRIMARY KEY(idProduit),
   FOREIGN KEY(idCategories) REFERENCES Categories(idCategories)
);

CREATE TABLE LignesCommande(
   idCommande VARCHAR(50),
   noLigne INT,
   quantite INT NOT NULL,
   idProduit INT NOT NULL,
   PRIMARY KEY(idCommande, noLigne),
   FOREIGN KEY(idCommande) REFERENCES Commandes(idCommande),
   FOREIGN KEY(idProduit) REFERENCES Produit(idProduit)
);
