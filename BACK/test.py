class file(object):
    def __init__(self,type,fichier):
        self.type = type
        #type de fichier horaire ou parcours
        self.namefile = fichier
        #nom du fichier
        self.n_page = 0
        #nombre de page du fichier excel
        self.list_horaire = {}
        self.jour_semaine = ["LUNDI","MARDI","MERCREDI","JEUDI","VENDREDI"]
        self.quadrimestre = []



    def read(self,namefile,page):
        #methode permettant de lire un fichier excel
        #avec comme arguments le type de fichier
        #et le numero de la page


        try:
        #essaie d'importer le module et
        #essaie de lire le fichier
            import xlrd
            wb = xlrd.open_workbook(self.namefile)
            #ouverture du fichier excel

            self.n_page = len(wb.sheets())
            #compte le nombre de page du fichier

            print('lecture du fichier feuille n°',page)
            sheet = wb.sheet_by_index(page)
            #lecture de la feuille

            for colonne in range(sheet.ncols):
                for ligne in range(sheet.nrows):
                    self.list_horaire[str(colonne) + "," + str(ligne)] = sheet.cell_value(ligne,colonne)
                    #parcours du fichier ligne par ligne, colonne par colonne
                    #if(sheet.cell_value(ligne,colonne)!=""):
                        #si la cellule n'est pas vide afficher la valeur de la cellule
                        #print(sheet.cell_value(ligne,colonne), end=" ")


        except IOError:
            print('erreur de lecture de fichier !')
        except ImportError:
            print('erreur d\'importation !')

        #interception des erreurs

    def traitement(self):
        self.tri()
        #supprime la dernière colonnne car inutile
        self.alldata = []
        jour_trouve = False
        self.data = []
        jour=""
        cpt = 0

        for i in self.list_horaire.values():
            if(i!=""):
                cpt+=1
                if(i in self.jour_semaine and jour_trouve):
                    #si i est un jour
                    print(">> Ajout du jour : "+jour)
                    a = self.data
                    self.alldata.append(a)
                    self.data = []
                    jour_trouve = False

                if(i in self.jour_semaine and not jour_trouve):
                    #si i est un jour de la semaine et qu'on ne la pas trouve
                    jour_trouve = True
                    jour = i



                if(jour_trouve):
                    if(len(i)>=5 and i in self.jour_semaine):
                        #ajouter seulement les données qui ont une longueur supérieur à 5 et qui sont des jours
                        self.data.append(i)
                    if(len(i)>5 and i not in self.jour_semaine):
                        #ajouter les autres données
                        self.data.append(i)
                    if(len(i)==2 and "Q" in i and i not in self.quadrimestre):
                        self.quadrimestre.append(i)

                if(jour == "VENDREDI"):
                    #si i est le dernier jour de la semaine et est différent de ""
                    if(cpt==self.count_data()):
                        print(">> Ajout du jour : "+jour)
                        a = self.data
                        self.alldata.append(self.data)
                        


    def tri(self):
        #pour supprimer les données inutiles de la dernière colonne
        for i in range(46):
            self.list_horaire.__delitem__("11,"+str(i))


    def count_data(self):
        cpt = 0
        for i in self.list_horaire.values():
            if(i!=""):
                cpt+=1
        return cpt

    def count_nodata(self):
        cpt = 0
        for i in self.list_horaire.values():
            if(i==""):
                cpt+=1
        return cpt




class horaire(object):
    def __init__(self, horaire_semaine,quadrimestre):
        self.horaire_semaine = horaire_semaine
        self.quadrimestre = quadrimestre
        


    def det_quad(self):
        for liste in self.horaire_semaine:
            for element in liste:
                if(len(element)==2 and "Q" in element):
                    self.quadrimestre = element
                    print(self.quadrimestre)

    def gen_horaire(self):
        pass
    


class CAVP(object):
    def __init__(self):
        self.niveau_cycle = ""
        self.cours_selectionne = {}
        self.cours_reussi = {}
        self.cours_rate = {}
        self.total_credit_selectionne = 0
        self.cours_credits = {}

    def somme_credit(self):
        somme = 0
        for cours in self.cours_selectionne.values():
            somme+=self.cours_credits[cours]

        self.total_credit_selectionne = somme

    def read_parcours(self):
        pass

    def ajouter_cours_select(self,quadri,cours):
        self.cours_selectionne[quadri] = cours

    def ajouter_cours_reussi(self,quadri,cours):
        self.cours_reussi[quadri] = cours

    def ajouter_cours_rate(self,quadri,cours):
        self.cours_rate[quadri] = cours

    def traitement(self):
        pass
    
    

    
if __name__ =="__main__":
    f = file("horaire","Horaire_Cours_2019-2020_IG_Q2-Q4.xlsx")
    f.read(f.namefile,0)
    f.traitement()
    h = horaire(f.alldata+f.quadrimestre)
    h.det_quad()
