from random import randint
from math import ceil
#jeu du demineur
#Un table des lettres de l'alphabet pour construire la grille
cases_afficher = []
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#utilise le niveau pour generer la girlle de hashtag ou la position des bombes pour le niveau 2
def grille_hashtag(taille):
    #grille vide initialiser avec des hashtag
    grille=[]
    #on genere la grille de hashtag
    for i in range(taille):
        grille.append([])
        for j in range(taille):
            grille[i].append("#")
    return grille
def affichage_grille(grille):
    #variable pour contenir le numero des colonnes
    ln_numb="  "
    #variable chaine de caractere pour contenir les tirets
    tiret="    "
    for i in range(len(grille)):
        #variable de ligne de nombre
        ln_numb +="   "+str(i+1)
        tiret +="----"
    print(ln_numb) 
    print(tiret) 
    for i in range(len(grille)):
         #variable de ligne commençant par les lettres de l'alphabet
         ln=alphabet[i]+"  |"
         for j in range(len(grille)):
            ln += " "+str(grille[i][j])+" |"
         print(ln)
         print(tiret)
#fonction pour recuperer les coordonnées des positions   
def get_user_input(grille):
    print("Entrer une position")
    row = input("Abscisse : ")
    row = row.upper()
    try:
            col = int ( input("Ordonnée : ") )
    except ValueError:
            print("Le type de valeur entreé pour les ordonnées n'est pas vailide" )
            col = 0
    cols = []
    for i in range(1,len(grille)+1):
        cols.append(i)
    while row not in alphabet[:len(grille)] or col not in cols or grille[alphabet.index(row)][col-1] == "*":
        print("----\nPosition non valide \n")
        row = input("Entrer une nouvelle lettre des abscisses : ")
        row = row.upper()
        try:
            col = int ( input("Entrer un nouveau chiffre pour les ordonnées : ") )
        except ValueError:
            print("Le type de valeur entreé pour les ordonnées n'est pas vailide" )
            col = 0    
    return [alphabet.index(row) , col-1 ]
#recuperer le position des bombes
def get_bombs_position(niveau):
    positions_bombs = []
    file = " "
    if niveau == 0 :
         file = "bombs.txt"
    if niveau == 1  :
         file = "bombs_niveau1.txt"
    if niveau == 2  :
         file = "bombs_niveau2.txt"
    with open(file ,"r") as f:
        for line in f:
            #tableau pour recuperer le x et y de la position
            pos=[]
            #on recupere la position en chaine et on supprime les espace inutiles
            line = line.strip()
            #on recupere le x de la position
            pos.append(int(tuple(line)[0]))
            #on recupere le y de la position
            pos.append(int(tuple(line)[2]))
            #on les ajoute dans le tableau des positions
            positions_bombs.append(pos)
    return positions_bombs
#fonction pour trouver toutes les les cases adjacentes d'une position(case)
def find_adjacent_cases(pos,taille):
    #taille = len(grille)
    cases = []
    # les cases adjacentes des cases qui sont sur les coins
    if pos[0] == 0 and pos[1] == 0 :
        case1 = pos[:]
        case1[1] += 1 
        case2 = pos[:]
        case2[0] += 1
        case3 = pos[:]
        case3[0] += 1
        case3[1] += 1
        cases.append(case1)
        cases.append(case2)
        cases.append(case3)
    elif pos[0] == taille - 1 and pos[1] == taille - 1 :
        case1 = pos[:]
        case1[1] -= 1 
        case2 = pos[:]
        case2[0] -= 1
        case3 = pos[:]
        case3[0] -= 1
        case3[1] -= 1
        cases.append(case1)
        cases.append(case2)
        cases.append(case3)
    elif pos[0] == taille - 1 and pos[1] == 0:
        case1 = pos[:]
        case1[1] += 1 
        case2 = pos[:]
        case2[0] -= 1
        case3 = pos[:]
        case3[0] -= 1
        case3[1] += 1
        cases.append(case1)
        cases.append(case2)
        cases.append(case3)
    elif pos[0] == 0 and pos[1] == taille - 1:
        case1 = pos[:]
        case1[1] -= 1 
        case2 = pos[:]
        case2[0] += 1
        case3 = pos[:]
        case3[0] += 1
        case3[1] -= 1
        cases.append(case1)
        cases.append(case2)
        cases.append(case3)
    #les cotes adjacents des cases de la premiere colonne (sauf les cas des des positions 0,0 et 0,taille de la grille - 1)
    elif pos[0] == 0 and pos[1] != taille - 1 and pos[1] != 0:
        case1 = pos[:]
        case1[1] -= 1 
        case2 = pos[:]
        case2[0] += 1
        case3 = pos[:]
        case3[0] += 1
        case3[1] -= 1
        case4 = pos[:]
        case4[1] += 1
        case4 = pos[:]
        case4[1] += 1
        case5 = pos[:]
        case5[0] += 1
        case5[1] += 1
        cases.append(case1)
        cases.append(case2)
        cases.append(case3) 
        cases.append(case4) 
        cases.append(case5) 
    #les cotes adjacents des cases de la derniere  colonne
    elif pos[0] == taille - 1 and pos[1] != taille - 1 and pos[1] != 0:
        case1 = pos[:]
        case1[1] += 1 
        case2 = pos[:]
        case2[0] -= 1
        case3 = pos[:]
        case3[0] -= 1
        case3[1] += 1
        case4 = pos[:]
        case4[1] -= 1
        case5 = pos[:]
        case5[0] -= 1
        case5[1] -= 1
        cases.append(case1)
        cases.append(case2)
        cases.append(case3) 
        cases.append(case4) 
        cases.append(case5) 
    #les cotes adjacents qui sont sur la premieres ligne
    elif pos[1] == 0 and pos[0] != taille - 1 and pos[0] != 0:
        case1 = pos[:]
        case1[1] += 1 
        case2 = pos[:]
        case2[0] += 1
        case3 = pos[:]
        case3[0] += 1
        case3[1] += 1
        case4 = pos[:]
        case4[0] -= 1
        case5 = pos[:]
        case5[0] -= 1
        case5[1] += 1
        cases.append(case1)
        cases.append(case2)
        cases.append(case3) 
        cases.append(case4) 
        cases.append(case5) 
    #les cotés adjacents qui sont sur la derniere ligne
    elif pos[1] == taille - 1 and pos[0] != taille - 1 and pos[0] != 0:
        case1 = pos[:]
        case1[0] -= 1 
        case2 = pos[:]
        case2[0] += 1
        case3 = pos[:]
        case3[0] -= 1
        case3[1] -= 1
        case4 = pos[:]
        case4[0] += 1
        case4[1] -= 1
        case5 = pos[:]
        case5[1] -= 1
        cases.append(case1)
        cases.append(case2)
        cases.append(case3) 
        cases.append(case4) 
        cases.append(case5)
    #les cotes ajacents des cases au milieu
    else :
        #pos[0] != 0 and pos[1] != 0 and pos[0] != 4 and pos[1] != taille - 1
        case1 = pos[:]
        case1[0] += 1
        case2 = pos[:]
        case2[0] -= 1
        case3 = pos[:]
        case3[1] +=1 
        case4 = pos[:]
        case4[1] -= 1  
        case5 = pos[:]
        case5[0] -= 1
        case5[1] += 1
        case6 = pos[:]
        case6[0] += 1
        case6[1] -= 1
        case7 = pos[:]
        case7[0] += 1
        case7[1] += 1
        case8 = pos[:]
        case8[0] -= 1
        case8[1] -= 1
        cases.append(case1)
        cases.append(case2)
        cases.append(case3) 
        cases.append(case4) 
        cases.append(case5)
        cases.append(case6)
        cases.append(case7)
        cases.append(case8) 
    return cases
#fonction pour recuperer les positions ajacentes de tous les bombes 
def get_all_bomb_adjacent_position_for_file(niveau):
    bombs_positions = get_bombs_position(niveau)
    all_ajacent_cases = []
    for pos in bombs_positions:
       all_ajacent_cases.append(find_adjacent_cases(pos,9))
    return all_ajacent_cases
#creation d'une nouvelle grille avec la position des bombes
def grille_positions(taille, niveau):
    #grille vide initialiser a 0
    bombs_postions = get_bombs_position(niveau)
    grille=[]
    for i in range(taille):
        grille.append([])
        for j in range(taille):
            grille[i].append(0)
    #les positions adjacentes des bombes
    position_adjacentes = get_all_bomb_adjacent_position_for_file(niveau)
    for i in range(len(grille)):
        for j in range( len(grille)):
            for positions in position_adjacentes:
                if [i,j] in positions and [i,j] not in bombs_postions:
                    grille[i][j] +=1
                if [i,j] in bombs_postions:
                    grille[i][j] = "B"
    return grille 
#fonction pour verifier la postion du user dans la grille
def check_position(pos,grille,niveau):
    bombs_position =  get_bombs_position(niveau)
    if pos in bombs_position:
         return 0
    #je compte le nombre de case vide
    nb_case_vide = 0
    for i in range(len(grille)):
        for j in range(len(grille)):
            if grille[i][j] != "B":
                nb_case_vide += 1
    #on retourne 1 pour indiquer que le jeu continu (on part au round suivant)
    return nb_case_vide
def show_case_in_grille(pos,grille_valeur,grille_hashtag):
    grille_hashtag[pos[0]][pos[1]] = grille_valeur[pos[0]][pos[1]]
    return grille_hashtag
def show_case_limitrophes(pos,grille_valeur,grille_hashtag):
    case_trouver = 0
    cases_ajacentes =  find_adjacent_cases(pos,len(grille_valeur))

    #print( cases_ajacentes)

    for i in range( len( cases_ajacentes )) :
        if grille_valeur[cases_ajacentes[i][0]][cases_ajacentes[i][1]] == 0 :
            grille_hashtag[ cases_ajacentes[i][0]][cases_ajacentes[i][1]] = " "
            grille_valeur[cases_ajacentes[i][0]][cases_ajacentes[i][1]] = "*"
            case_trouver += 1
        elif  grille_valeur[cases_ajacentes[i][0]][cases_ajacentes[i][1]] != 0 and grille_valeur[cases_ajacentes[i][0]][cases_ajacentes[i][1]] != "*" :
            grille_hashtag[ cases_ajacentes[i][0]][cases_ajacentes[i][1]] = grille_valeur[cases_ajacentes[i][0]][cases_ajacentes[i][1]]
            cases_afficher.append(cases_ajacentes[i])
            case_trouver += 1
        elif  grille_valeur[cases_ajacentes[i][0]][cases_ajacentes[i][1]] == "*":
                grille_hashtag[ cases_ajacentes[i][0]][cases_ajacentes[i][1]] = " "
                case_trouver += 1
              
    case_trouver += 1
    grille_hashtag[pos[0]][pos[1]] = " "
    grille_valeur[pos[0]][pos[1]] = "*"       

    return [case_trouver,grille_valeur]
def niveau_1_2(niveau,taille,fichier):
         liste_num_aleatoire = []
         grille_pos=[]
         #on recupere la taille de la grille donner par le joueur
         try:
              taille = int(input("Entrer la taille de la Grille : "))
         except ValueError:
            print("Valeur invalide")
         while taille <= 1 :
            try:
                taille = int(input("Entrer une nouvelle taille pour la Grille : "))
            except ValueError:
                print("Valeur invalide")              
        #on genere la grille de toutes les positions
         for i in range(taille):
            for j in range(taille):
                grille_pos.append("{},{}".format(i,j))
        #on genere un fichier qui contiendra les positions aleatoires
         with open(fichier ,"w") as f:
              #on genere un nombre aléatoire entre 0 et (taille*taille)/5
              num = ceil((taille*taille)/5)
              num_random = randint(0,len(grille_pos) - 1)
              liste_num_aleatoire.append(num_random)
              for i in range(1,num):
                    num_random = randint(0,len(grille_pos) - 1 )
                    while num_random in  liste_num_aleatoire:
                          num_random = randint(0,num)
                    liste_num_aleatoire.append(num_random)
              for i in range(len(liste_num_aleatoire)):
                   f.write("{}\n".format(grille_pos[liste_num_aleatoire[i]]))
         g = grille_positions(taille,niveau)
         affichage_grille(g)
         return [g,niveau,taille]
def round (grille,niveau,taille):
    grille_p = grille
    grille_ht = grille_hashtag(taille)
    case_trouver = 0
    round = 1
    case_ajacentes_aux_bombes = get_all_bomb_adjacent_position_for_file(niveau)
    bomb_position = get_bombs_position(niveau)
    affichage_grille(grille_ht)
    print ("round ",round,"!")
    pos = get_user_input(grille)
    nb_case_vide = check_position(pos,grille,niveau)
    etat_jeu = check_position(pos,grille,niveau)
   
    if etat_jeu == 0:
            grille_ht[pos[0]][pos[1]] = "B"
            affichage_grille(grille_ht)
            print("\nVous avez perdu !")
            print("Fin du programme\n----")
            return 0
    if etat_jeu != 0:
            for i in range(len(case_ajacentes_aux_bombes)):
                    if pos in case_ajacentes_aux_bombes[i]:
                        #fonction pour devoiler la case adjacente à la bombe
                        grille_hs = show_case_in_grille(pos,grille_p,grille_ht)
                        case_trouver += 1
                        affichage_grille(grille_hs)
                        cases_afficher.append(pos)
                        break
    if grille[pos[0]][pos[1]] == 0:
                        case_trouver += show_case_limitrophes(pos,grille_p,grille_ht)[0]
                        grille_p = show_case_limitrophes(pos,grille_p,grille_ht)[1]
                        affichage_grille(grille_ht)
                        #print(case_trouver)
    if case_trouver == nb_case_vide:
                    #affichage_grille(grille_ht)
                    print("\nBravo,vous avez gagner!\n---")
    print ("vous avez trouver ",case_trouver,"/",nb_case_vide," case ")

    if niveau != 2 :     
        while etat_jeu != 0:
                round += 1
                print("\nRound ",round,"!\n---")
                affichage_grille(grille_ht)
                pos = get_user_input(grille)
                for i in range(len(case_ajacentes_aux_bombes)):
                    if pos in case_ajacentes_aux_bombes[i] and pos not in bomb_position:
                        #fonction pour devoiler la case adjacente à la bombe
                        grille_hs = show_case_in_grille(pos,grille_p,grille_ht)
                        case_trouver += 1
                        affichage_grille(grille_hs)
                        cases_afficher.append(pos)
                        break
                if grille[pos[0]][pos[1]] == 0:
                        case_trouver += show_case_limitrophes(pos,grille_p,grille_ht)[0]
                        grille_p = show_case_limitrophes(pos,grille_p,grille_ht)[1]
                        affichage_grille(grille_ht)

                if case_trouver == nb_case_vide:
                    #affichage_grille(grille_hs)
                    print("\nBravo,vous avez gagner!\n---")
                    return 0
                etat_jeu = check_position(pos,grille,niveau)
                if etat_jeu == 0:
                    grille_ht[pos[0]][pos[1]] = "B"
                    affichage_grille(grille_ht)
                    print("\nVous avez perdu !")
                    print("Fin du programme\n----")
                    return 0
                print ("vous avez trouver ",case_trouver,"/",nb_case_vide," case ")
    else:
         while etat_jeu != 0 :
              
         
            bombs = {}
            grille_p =  grille_positions(taille, niveau)    
            round += 1
            print("\nRound ",round -1 ,"! Reussi \n---")
            print("Une nouvelle grille est générée !\n")
          

            #les cases occupé c'est ou on ne peut pas mettre de bombe
            cases_occupe = []
            #case vide ce sont les case vide , cad qui ont déjà été decouvert
            case_decouvert = []
            for i in range(len(grille)):
                for j in range(len(grille)):
                    if grille_ht[i][j] == " ":
                            cases_occupe.append([i,j])
                    elif [i,j] in cases_afficher:
                            cases_occupe.append([i,j])
                            case_decouvert.append([i,j])                  
            #on calcule le nombre de bombe
            num = ceil((taille*taille)/5)
            #on génère la position des bombes de tel sorte qu'ils ne soient pas dans le tableau des positions/cases occupées
            position = ""
            positions = []
            with open("bombs_niveau2.txt","w") as f:
                    for i in range(num):
                        abscisse = randint(0,len(grille)-1)
                        ordonne = randint(0,len(grille)-1)
                        position = [abscisse,ordonne]
                        while position in cases_occupe or  position in positions or position in cases_afficher:
                            abscisse = randint(0,len(grille)-1)
                            ordonne = randint(0,len(grille)-1)
                            position = [abscisse,ordonne]
                        f.write("{},{}\n".format(abscisse,ordonne))
                        positions.append(position)
            #je génère une grille de position  des bombes
            bomb_position = get_bombs_position(niveau)
            case_ajacentes_aux_bombes = get_all_bomb_adjacent_position_for_file(niveau) 
            for i in range(num):
                bombs[ (bomb_position[i][0],bomb_position[i][1])] = "B" 
            
            for i in range(len(grille)):
                for j in range(len(grille)):
                    
                    if  [i,j] in cases_occupe:
                        if grille_p[i][j] == 0 or grille_p[i][j] == "*":
                              grille_ht[i][j] = " "
                        elif [i,j]  in case_decouvert and grille_p[i][j] != 0 and grille_p[i][j] != "B" and grille_p[i][j] != "*":
                             grille_ht[i][j] =  grille_p[i][j]
                        
                  
                              
            print(bombs)
           
            affichage_grille(grille_ht)

            pos = get_user_input(grille)

            for i in range(len(case_ajacentes_aux_bombes)):
                    if pos in case_ajacentes_aux_bombes[i] and pos not in bomb_position:
                        #fonction pour devoiler la case adjacente à la bombe
                        grille_ht = show_case_in_grille(pos,grille_p,grille_ht)
                        case_trouver += 1
                        affichage_grille(grille_ht)
                        cases_afficher.append(pos)
                        break
            if grille[pos[0]][pos[1]] == 0:
                        case_trouver += show_case_limitrophes(pos,grille_p,grille_ht)[0]
                        grille_p = show_case_limitrophes(pos,grille_p,grille_ht)[1]
                        affichage_grille(grille_ht)

            if case_trouver >= nb_case_vide:
                    #affichage_grille(grille_hs)
                    print("\nBravo,vous avez gagner!\n---")
                    for i in range(len(grille)):
                         for j in range(len(grille)):
                              if grille_p[i][j] == 0 :
                                   grille_p[i][j] =" " 
                    return 0
            etat_jeu = check_position(pos,grille,niveau)
            if etat_jeu == 0:
                    grille_ht[pos[0]][pos[1]] = "B"
                    affichage_grille(grille_ht)
                    print("\nVous avez perdu !")
                    print("Fin du programme\n----")
                    return 0
          
            print ("vous avez trouver ",case_trouver,"/",nb_case_vide," case ")
def menu():
    taille = 0
    niveau = 0
    #affichage presentation du jeu
    print(" \n\n Bienvenu dans le jeu du demineur en console.\n Essayez de trouver toutes les cases sans Bombes.\n Bonne chance !\n ---")
    #variable du niveau de difficulté
    print("Note :\n Les positions des cases doivent etre sous la forme d'une lettre de l'alphabet  \n pour  les abscisses suivie d'un chiffre pour les ordonnées.\n")
    print("  Exemple  \n    Abscisse : A\n    Ordonnée : 1\n")
    print("Choisissez le niveau de difficulté.\nNiveau facile : 0 \nNiveau moyen : 1 \nNiveau difficile 2\n ---\n")
    niveau = -1 #initialisation pour entrer dans la boucle
    while(niveau not in [0,1,2]):
        try:
            niveau=int(input("Selectionner votre niveau : "))
            print(" ") #juste pour aller à la ligne
            if niveau not in[0,1,2]:
                print("Ce numero de niveau n'existe pas , veillez entrer un nouveau svp!\n")
        except ValueError:
            print("Veillez entre un niveau de jeu valide svp!\n")
    if niveau == 0:
        taille = 9
        g = grille_positions(taille,niveau)
        affichage_grille(g)
        round (g,niveau,taille)
    if niveau == 1 :
         #je cree des variables intermediaire pour faciluter la comprehension du code
         data = niveau_1_2(niveau,taille,"bombs_niveau1.txt")
         g = data[0]
         niveau = data[1]
         taille = data[2]
         round (g,niveau,taille)
    if niveau == 2 :
         #je cree des variables intermediaire pour faciluter la comprehension du code
         data = niveau_1_2(niveau,taille,"bombs_niveau2.txt")
         g = data[0]
         niveau = data[1]
         taille = data[2]
         round (g,niveau,taille)  

menu()

