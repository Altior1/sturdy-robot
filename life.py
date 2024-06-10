import pyxel as px
WIDTH = 800
HEIGHT = 800
TAILLE_PIX = 5
INITCEL= [(1,2),(5,3),(0,0),(20,20),(80,80),(80,81),(18,159)]
class cellule:
    """ les cellules vont être la base du changement de comportement"""
    def __init__(self,x,y):
        self.etat=0
        self.x=x
        self.y=y
        self.voisin=[]
    def update(self):
        compt=0
        for each in self.voisin:
            if each.etat==1:
                compt+=1
        if compt==0:
            self.etat=0
        elif compt>2:
            self.etat=0
        else:
            self.etat=1
    def draw(self):
        if self.etat==1:
            px.rect(self.x*5,self.y*5,5,5,5)
        else:
            px.rect(self.x*5,self.y*5,5,5,15)

class App:
    """ La classe App contient les fonctions générales de l'application, qui vont appeler les 
    différentes classes"""
    def __init__(self):
        px.init(WIDTH,HEIGHT,title="jeu de la vie",fps=5)
        # self.list contient des listes de celulles correspondant aux différentes colonnes
        self.list=[]
        for i in range(160):
            #Le i est mis sur les lignes
            list_cel=[]
            for j in range(160):
                #le j est mis sur les colonnes1
                cel=cellule(i,j)
                list_cel.append(cel)
            self.list.append(list_cel)
        #ensuite on setup les voisins
        for i in range(len(self.list)):
            for j in range(len(self.list[i])):
                if i!=0:
                    self.list[i][j].voisin.append(self.list[i-1][j])
                if j!=0:
                    self.list[i][j].voisin.append(self.list[i][j-1])
                if i!=159:
                    self.list[i][j].voisin.append(self.list[i+1][j])
                if j!=159:
                    self.list[i][j].voisin.append(self.list[i][j+1])
        for each in INITCEL:
            self.list[each[0]][each[1]].etat=1

        px.run(self.update,self.draw)

    def update(self):
        for each in self.list:
            for ea in each:
                ea.update()
        if px.btnp(px.KEY_Q):
            px.quit()
    def draw(self):
        for each in self.list:
            for ea in each:
                ea.draw()

App()