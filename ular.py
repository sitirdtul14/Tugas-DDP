from Animal.Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun
        
    def cetak_ular(self):
        super().cetak()
        print("Design \t\t\t: ", self.design,
        "\nRacun \t\t\t: ", self.racun)
    
Anaconda = Ular("Anaconda", "Daging", "Darat", "Bertelur", "Shimer", 
"Tidak Berbisa")
Anaconda.cetak_ular()

Python = Ular("Python", "Daging", "Darat", "Bertelur", "Batik", 
"Berbisa")
Python.cetak_ular()


