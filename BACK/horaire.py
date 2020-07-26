from test import file
class horaire(object):
    def __init__(self,horaire_semaine):
        self.quadrimestre = ""
        #quadrismetre de l'horaire
        self.n_groupe = ng
        #nombre de groupe
        self.nb_heure = 0
        #nombre d'heure
        self.jour_semaine = ["LUNDI","MARDI","MERCREDI","JEUDI","VENDREDI"]
        #tout les jours de la semaine
        self.gen_groupe()

    def read_sheet(self,namefile,nsheet):
        jour_trouve = False
        f = file("horaire",namefile)
        f.read(namefile,0)

        data = []
        for i in f.list_horaire.values():
            if(i in self.jour_semaine and jour_trouve):
                self.horaire_semaine_g1[jour] = data
                data.clear()
                jour_trouve = False

            if(i in self.jour_semaine and not jour_trouve):
                jour_trouve = True
                jour = i

            if(jour_trouve and len(i)>3):
                data.append(i)




    def gen_horaire(self):
        #génère un horaire
        for jour in self.jour_semaine:
            pass


    def scan_horaire(self):
        #scan l'horaire
        for jour in self.horaire_semaine.keys():
            if(self.horaire_semaine[jour]):
                pass



   def gen_groupe(self):
       for i in range(self.n_groupe):
           self.groupe.append("G" + str(i+1))



if __name__=="__main__":
    h = horaire()
