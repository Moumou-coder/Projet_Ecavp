
class horaire(object):
    def __init__(self, horaire_semaine):
        self.horaire_semaine = horaire_semaine
        self.groupe = []
        self.quadrimestre


    def det_quad(self):
        for i in self.horaire_semaine.values():
            if(len(i)==2 and "Q" in i):
                self.quadrimestre = i

    def decomposer(self):
        for i in self.horaire_semaine.values():
            if i in self.groupe:
                self.gen_horaire(self.groupe.index(i)+1,i)


    def gen_horaire(self, gr, content):
        pass

if __name__ == '__main__':
    h = horaire()
