from Animal.Animal import *

class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, Jenis, Warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.Jenis = Jenis
        self.Warna = Warna
        
    def cetak_ikan(self):
        super().cetak()
        print("Jenis \t\t\t: ", self.Jenis,
        "\nWarna \t\t\t: ", self.Warna)
    
Koi = ikan("Koi", "Cacing", "Air", "Bertelur", "Bekko", 
"Oren")
Koi.cetak_ikan()

Bawel = ikan("Bawel", "Daging", "Air", "Bertelur", "Brama", 
"Silver")
Bawel.cetak_ikan()