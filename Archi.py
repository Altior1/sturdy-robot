import pyxel

#les constantes
HEIGHT=400
WIDTH=400
SAUT=20


#l'objet joueur
class Player:
    def __init__(self):
        self.pv=0
        self.attaque=0
        self.vitesse=10
        self.posX=0
        self.posY=0

    def update(self):
        if pyxel.btnp(pyxel.KEY_UP,repeat=10) and self.posY>0:
            self.posY-=self.vitesse
        if pyxel.btnp(pyxel.KEY_RIGHT,repeat=10) and self.posX<WIDTH-10:
            self.posX+=self.vitesse
        if pyxel.btnp(pyxel.KEY_LEFT,repeat=10) and self.posX>0:
            self.posX-=self.vitesse
        if pyxel.btnp(pyxel.KEY_DOWN,hold=10,repeat=10) and self.posY<HEIGHT-10:
            self.posY+=self.vitesse

    def draw(self):
        pyxel.rect(self.posX,self.posY,10,10,2)

#les ennemies
class Missile:
    def __init__(self) -> None:
        self.posX=HEIGHT-10
        self.posY=WIDTH-10
        self.vitesse=10
    def update(self):
        if self.posX>0:
            self.posX-=self.vitesse
        if self.posY>0:    
            self.posY-=self.vitesse
    def draw(self):
        pyxel.rect(self.posX,self.posY,10,10,5)

class App():
    
    #l'initialisation
    def __init__(self) -> None:
        #les variables globales du jeu
        self.objects=[]
        player=Player()
        missile1=Missile()
        self.objects.append(player)
        self.objects.append(missile1)
        pyxel.init(WIDTH,HEIGHT,title="Le silence dans la prairie",fps=30)
        pyxel.load("ressources/ressourceArchi.pyxres")
        pyxel.run(self.update,self.draw)
    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        for each in self.objects:
            each.update()
    def draw(self):
        pyxel.cls(0)
        for each in self.objects:
            each.draw()

App()