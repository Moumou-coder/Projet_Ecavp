from parcours import parcours
from horaire import horaire
class CPAV(object):
    def __init__(self):
        self.niveau_cycle = ""
        self.cours_selectionne = {}
        self.cours_reussi = {}
        self.cours_rate = {}
        self.total_credit_selectionne = 0
        


    def somme_credit(self):
        somme = 0
        for i in self.cours_selectionne.items():
            somme +=i
        self.total_credit_selectionne = somme
    
    def gen_horaire(self):
        h = horaire()
        

    
    def read_parcours(self):
        #lis le parcours d'un étudiant
        try:
            pass
        except Exception:
            pass
    
