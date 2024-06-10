import pyxel as px
WIDTH = 800
HEIGHT = 800
TAILLE_PIX = 5

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
            px.rect(self.x*5,self.y*5,5,5,12)
        else:
            px.rect(self.x*5,self.y*5,5,5,15)

class App:
    """ La classe App contient les fonctions générales de l'application, qui vont appeler les 
    différentes classes"""
    def __init__(self):
        px.init(WIDTH,HEIGHT,title="jeu de la vie")
        color=px.colors.from_list([0x111111,0x222222,0x333333])
        # self.list contient des listes de celulles correspondant aux différentes colonnes
        self.list=[]
        for i in range(80):
            #Le i est mis sur les lignes
            list_cel=[]
            for j in range(80):
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
                if i!=79:
                    self.list[i][j].voisin.append(self.list[i+1][j])
                if j!=79:
                    self.list[i][j].voisin.append(self.list[i][j+1])    
        px.run(self.update,self.draw)

    def update(self):
        for each in self.list:
            for ea in each:
                ea.update()
        if px.btnp(px.KEY_Q):
            px.quit()
    def draw(self):
        px.cls(15)
        for each in self.list:
            for ea in each:
                ea.draw()

App()