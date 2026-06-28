
# Les cases vide sont représenter par 0, celle du joueur 1 par un 1, et celle du joueur 2 par un 2.
class Jeu:
    def __init__(self):
        self.plateau =  {f"niveau {i}" : {f"ligne {i}" : [0 for _ in range(6)] for i in range(6)} for i in range(6)}
        self.tours, self.gagant = 0, 0
    
    def ajouter_pion(self, x, y):
        pass
    

    def continuer(self):
        return True

    def afficher_gagant(self):
        print("Fonction en construction")


    def game(self):
        i = 1
        while self.continuer():
            i += 1
            print(f"Joueur {i % 2 + 1} veuillez choisir une coordonée")
            x = int(input("x = "))
            y = int(input("y = "))
            print("\n\n\n")
            self.ajouter_pion(x, y)
        self.afficher_gagant()
        

partie = Jeu()
partie.game()