#sınıf ve sınıf ozellikleri

class VeriBilimci():
    print("bu bir sınıftır")
    bolum = ''
    deneyim_yili = 0
    sql = "Evet"
    bildigi_diller = []
    
    
#orneklendirme    
VeriBilimci.sql = "Hayır"

VeriBilimci.sql


Ali = VeriBilimci()

Ali.sql

Ali.bildigi_diller
Ali.deneyim_yili

Ali.bildigi_diller.append("Python")

Ali.bildigi_diller


veli = VeriBilimci()

veli.bildigi_diller


#örnek ozellikleri

class VeriBilimci():
    def __init__(self):
        self.bildigi_diller = []

ali = VeriBilimci()
veli = VeriBilimci()

ali.bildigi_diller.append("R")
ali.bildigi_diller


veli.bildigi_diller.append("Python")
veli.bildigi_diller


VeriBilimci.bildigi_diller


class VeriBilimci():
    bildigi_diller = ["R","Python","SQL"]
    def __init__(self):
        self.bildigi_diller = []


VeriBilimci.bildigi_diller


ali = VeriBilimci()
ali.bildigi_diller
ali.bildigi_diller.append("R")
ali.bildigi_diller

veli = VeriBilimci()
veli.bildigi_diller
veli.bildigi_diller.append("Python")
veli.bildigi_diller

VeriBilimci.bildigi_diller


#ornek metodları 

class VeriBilimci():
    def __init__(self):
        self.bildigi_diller = []
    def dil_ekle(self, yeni_dil)    :
        self.bildigi_diller.append(yeni_dil)
    


dir(VeriBilimci)

ali = VeriBilimci()
ali.bildigi_diller

veli = VeriBilimci()
veli.bildigi_diller


VeriBilimci.dil_ekle("R")

ali.dil_ekle("R")
ali.bildigi_diller

veli.dil_ekle("Python")
veli.bildigi_diller


        













