import random
## Je crer une liste de 100 nombres aléatoires compris entre 0 et 1
maliste = []
## mes valeur son compris entre 0 et 100
for n in range (0,100) :
    i = random.randint(0,100)
    maliste.append(i)

print(maliste)
