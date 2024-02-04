import math
import time
import random

#exercice 8 fonction
def temperatures() :
    print("Exercie 8 :")
    choix_temp_c_ou_f = input("Entrer c pour convertir des degres celsius en fahrenheit ou f pour convertir des degres fahrenheit en celsuis : ")
    if choix_temp_c_ou_f == "c" :
        temp_c = eval(input("Entrez une valeur en celsius (°C) : "))
        print(f"{1.8 * temp_c + 32}")
    if choix_temp_c_ou_f == "f" :
        temp_f = eval(input("Entrez une valeur en fahrenheit (F°) : "))
        print(f"{(temp_f - 32) * 1.8}")



choix_exercice = 0
while choix_exercice != "stop" :
    print("\033[35mBonjour et bienvenue \ndans les exercices python de l'option informatique réalisés par Maxence Bailly\033[0m")
    choix_exercice = input("\033[34mEntrez le numéro d'exercice parmis les suivants : \n-1 disque \n-2 planete \n-3 volume \n-4 multiple_de_3 \n-5 planetes_v2 \n-6 multiplications \n-7 voyelles \n-8 temperatures \n-9 rebours \n-10 loto \n>>>Entrez donc un numéro : \033[0m")

#exercice 1
    if choix_exercice == "1" :
            print("Exercice 1 :")
            demande_nombre_disque = input("Entrez une valeur pour connaître le périmètre, la surface si celui-ci était un rayon de disque tout en cm : ")
            try :
                demande_nombre_disque = int(demande_nombre_disque) 
            except ValueError as test :  
                print("\033[31mERREUR : Entrez un chiffres et non pas des lettres\033[0m")
                quit()
            print(f"Le périmètre de votre disque est : {2*demande_nombre_disque*math.pi:.2f} cm et sa surface est {demande_nombre_disque*demande_nombre_disque*math.pi:.2f} cm²")

#exercice 2 et 5
    elif choix_exercice in ["2", "5"] :
            print("Exercice 2 et 5 :") 
            demande_chiffre_planete = input("Entrez un chiffre pour connaitre à quelle planete correspond t'il dans notre systeme solaire : ")
            try :
                demande_chiffre_planete = int(demande_chiffre_planete) 
            except ValueError as test :
                print("\033[31mERREUR : Entrez un chiffres et non pas des lettres\033[0m")
                quit()
            if demande_chiffre_planete not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] :
                print("Désoler mais vous aller trop loin dans la galaxis")
            else :
                planetes = ["Aucune planete mais il y à le Soleil qui est notre étoile", 
                            "Mercure", 
                            "Venus", 
                            "Terre", 
                            "Mars", 
                            "Jupiter", 
                            "Saturne", 
                            "Uranus", 
                            "Neptune", 
                            "Non non plus maintenant, Pluton est une planète naine désormais"]
                print(f"La planete est : {planetes[demande_chiffre_planete]}")

#exercice 3
    elif choix_exercice == "3" :
        print("Exercice 3 :")
        demande_nombre_longueur = eval(input("Entrez une longueur : "))
        demande_nombre_largeur = eval(input("Entrez une largeur : "))
        demande_nombre_profondeur = eval(input("Entrez une profondeur : "))
        print(f"Le volume de votre boîte fais : {demande_nombre_longueur*demande_nombre_largeur*demande_nombre_profondeur} cm cube")

#exercice 4
    elif choix_exercice == "4" :
        print("Exercie 4 :")
        demande_de_multiple_3 = eval(input("Entrez un nombre pour savoir si il est un multiple de 3 : "))
        multiple_de_3 = demande_de_multiple_3 % 3
        if multiple_de_3 != 0 :
            print(f"Le nombre {demande_de_multiple_3} n'est pas un multiple de 3")
        else :
            print(f"Le nombre {demande_de_multiple_3} est un multiple de 3")

#exercice 6
    elif choix_exercice == "6" :
        print("Exercie 6 :")
        demande_de_table = eval(input("Entrez un nombre ou un chiffre pour connaître sa table : "))
        for table in range(11) :
            print(f"{demande_de_table} x {table} = {demande_de_table*table}")
            table += 1

#exercie 7
    elif choix_exercice == "7" :
        print("Exercie 7 :")
        voyelles = ['a','e','y','u','i','o']
        s = input("Entrez une prase ou mot pour connaitre combien y'a t'il de voyelles dans celui ci : ")
        longueur_chaine_voyelles = len(s)
        nombre_voyelles = 0
        for i in range(0,longueur_chaine_voyelles):
            if (s[i] in voyelles):
                nombre_voyelles = nombre_voyelles + 1
        print(f"Il y a {nombre_voyelles} voyelles")

#exercie 8
    elif choix_exercice == "8" :
        temperatures()

#exercice 9
    elif choix_exercice == "9" :
        print("Exercie 9 :")
        rebours = 10
        while rebours != 0 :
            print(f"{rebours}")
            time.sleep(1)
            rebours -= 1

#exercice 10
    elif choix_exercice == "10" :
        print("Exercie 10 :")
        numero_1 = random.randint(1, 49)
        numero_2 = random.randint(1, 49)
        numero_3 = random.randint(1, 49)
        numero_4 = random.randint(1, 49)
        numero_5 = random.randint(1, 49)
        numero_6 = random.randint(1, 10)
        print(f"Les numéros sont : {numero_1} {numero_2} {numero_3} {numero_4} {numero_5} {numero_6}")
#arrêt du programme
    elif choix_exercice == "stop" :
        print("Vous venez d'arrêter le programme, à bientôt")
    
    else :
        print("\033[31mERREUR : Vous n'avez pas entrez un bon numéro d'exercice ou stop veuillez réessayer\033[0m")

