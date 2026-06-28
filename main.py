
# Les cases vide sont représenter par 0, celle du joueur 1 par un 1, et celle du joueur 2 par un 2.
class Jeu:
    def __init__(self):
        self.plateau: dict =  {f"niveau {i}" : {f"ligne {i}" : [0 for _ in range(6)] for i in range(6)} for i in range(6)}
        self.tours: int = 0
        self.gagant: int = 0
    
    def ajouter_pion(self, x: int, y: int, joueur: int) -> None:
        """Ajoute un pion au plateau en fonctions des pions déjà en place"""
        for k in self.plateau:
            if self.plateau[k][f"ligne {y}"][x + 1] == 0:
                self.plateau[k][f"ligne {y}"][x + 1] = joueur
                break

    def continuer(self) -> bool:
        """Renvoie True si il n'y a aucun gagnant, sinon False"""
        
        for pion in range(1, 3):
            for nv in self.plateau: # Parcour par niveau

                ### Vérification horizontal ###
                for y in self.plateau[nv]: # Parcour par ligne
                    liste: list = self.plateau[nv][y]
                    if liste[1:4] == [pion]*3 and (liste[0] == pion or liste[4] == pion):
                        self.gagant = pion # On définit le gagnant (cela nous servira dans la méthode 'afficher_gagnant()')
                        return False # Il y a une ligne horizontal
                ### Vérification vertical ###
                rendu = [[], [], [], [], []] # On initialise
                for ligne in self.plateau[nv]:
                    for i in range(5):
                        rendu[i].append(self.plateau[nv][ligne][i])
                for liste in rendu:
                    if liste[1:4] == [pion]*3 and (liste[0] == pion or liste[4] == pion):
                        self.gagant = pion # On définit le gagnant (cela nous servira dans la méthode 'afficher_gagnant()')
                        return False # Il y a une ligne vertical
        return True
                    

    def afficher_gagant(self) -> str:
        print(f"La partie est fini, le gagant est le joueur {self.gagant}")

    def game(self) -> None:
        i = 1
        while self.continuer():
            i += 1
            print(f"Joueur {i % 2 + 1} veuillez choisir une coordonée")
            x = int(input("x = "))
            y = int(input("y = "))
            print("\n\n\n")
            self.ajouter_pion(x, y, (i % 2 + 1))
        self.afficher_gagant()
        

partie = Jeu()
partie.game()