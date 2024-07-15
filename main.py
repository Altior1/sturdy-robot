#!/usr/bin/python3
""" Le jeu est un snake, tout ce qu'il y a de plus basique"""
################################# les importations ################################""
import pyxel
import random

WIDTH=500
HEIGHT=500
TAILLE_PIX=5

################################### les classes #########################################
class Boule:
    """les boules sont des bonus allongeant la taille du serpent"""
    def __init__(self) -> None:
        self.x=0
        self.y=0

    def update(self):
        pass

    def draw(self):
        pass


class Obstacle:
    """ les obstacles apparraissent à une certaine fréquence pour augmenter la difficulté """
    def __init__(self) -> None:
        pass

    def upgrade(self):
        pass

    def draw():
        pass


class Joueur:
    """ la classe gérant les actions du joueur"""
    def __init__(self) -> None:
        pass

    def upgrade(self):
        pass

    def draw(self):
        pass
############################ la classe principal du jeu #######################################
class Snake:
    """ la classe du jeu. Contient les méthodes pour représenter l'avancé
    de la partie
    """
    def __init__(self) -> None:
        pyxel.init(WIDTH,HEIGHT,title="snaaake",fps=55)
        pyxel.colors.from_list([0x000000,0x999999,0x000099,0x552266])
        pyxel.run(self.update,self.draw)
        
    def update(self):
        """la méthode qui influe sur les variables"""
        if 
    def draw(self):
        """ la méthode qui permet l'affichage"""
        pass
    
Snake()