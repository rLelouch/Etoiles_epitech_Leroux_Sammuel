def star():
    ### appel
    n = int(input("Saississez la taille du bloc : "))

    '''definition des variables et autres elements utilisés h represente la hauteur et L la large de l'étoile en entier.'''

    h = 4*n+1
    L = 6*n+1

    ### cas n = 0
    if n == 0:
        return None


    ### triangle du haut
    def haut(n):
        for i in range(1,n+1):
            for j in range(1,L):
                if i+j==3*n+2 or j-i==3*n:
                    print("*", end="")
                else:
                    print(end=" ")
            print()


    ### bandes
    def bandes(n):
        for i in range(1,L):
            if i>2*n+1 and i<4*n:
                print(" ",end="")
            else:
                print("*", end="")


    ### triangle cote
    def cote(n):
        for i in range(1,2*n):
            for j in range(1,6*n+2):

                #gauche
                if i<n+1 and j==i+1:
                    print("*", end="")

                if i>=n+1 and i+j==2*n+1:
                    print("*", end="")

                #droite
                if i<n+1 and j==-i+6*n:
                    print("*", end="")

                if i==n+1 and j==i+4*n:
                    print("*", end="")

                if i>n+1 and j-i==4*n:
                    print("*", end="")

                else:
                    print(end=" ")
            print()


    ### triangle du bas
    def bas(n):


        for i in range(1,n+1):


            for j in range(1,6*n+1):


                if i+j==4*n+1 or j-i==2*n+1:
                    print("*", end="")
                else:
                    print(end=" ")
            print()


    ### Appel des fonctions
    ''' les print('\n') sont nécessaires pour que chaque fonctions n'empiètent pas sur la fonction d'après'''

    haut(n)
    bandes(n)
    print('\n')
    cote(n)
    bandes(n)
    print('\n')
    bas(n)



### affichage
print(star())





