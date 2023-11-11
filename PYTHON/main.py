
from getpass import getpass
from mysql.connector  import connect, Error

try:
    with connect(
        user = input("Saisir le nom d'utilisateur: \n"),
        password = getpass("Enter your password: \n"), 
        host= input ("saisir l'adresse de l'hôte: \n"), 
        database= input ("saisir le nom de la base de donnée à laquelle vous voulez vous connecter: \n")
    ) as connection:
        print(connection)
except Error as e:
    print(e)