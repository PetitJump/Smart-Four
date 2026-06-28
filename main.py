
# Les cases vide sont représenter par 0, celle du joueur 1 par un 1, et celle du joueur 2 par un 2.
class Jeu:
    def __init__(self):
        self.plateau: dict =  {f"niveau {i}" : {f"ligne {i}" : [0 for _ in range(6)] for i in range(6)} for i in range(6)}
        self.tours: int = 0
        self.gagant: int = 0
    
    def ajouter_pion(self, x: int, y: int, joueur: int) -> None:
        """Ajoute un pion au plateau en fonctions des pions déjà en place"""
        for k in self.plateau:
            if self.plateau[k[f"ligne {y}"][x + 1]] == 0:
                self.plateau[k[f"ligne {y}"][x + 1]] = joueur
                break

    def continuer(self) -> bool:
        """Renvoie True si il n'y a aucun gagnant, sinon False"""
        ### Vérification horizontal ###
        for pion in range(1, 3):
            for k in self.plateau:
                for y in self.plateau[k]:
                    liste: list = self.plateau[k][y]
                    if liste[1:4] == [pion, pion, pion] and (liste[0] == pion or liste[4] == pion):
                        return False # Il y a une ligne horizontal
                
                


    def afficher_gagant(self) -> str:
        print("Fonction en construction")

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