
# Les cases vide sont représenter par 0, celle du joueur 1 par un 1, et celle du joueur 2 par un 2.
class Jeu:
    def __init__(self):
        self.plateau =  {f"niveau {i}" : {f"ligne {i}" : [0 for i in range(6)] for i in range(6)} for i in range(6)}
        self.tours = 0
    
    def ajouter_pion(self):
        pass
    
    def afficher_plateau(self):
        pass

    def tour(self):
        pass

    def start_game(self):
        pass

partie = Jeu()
partie.start_game()