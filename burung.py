from Animal.Animal import *

class burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, Jenis, Warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.Jenis = Jenis
        self.Warna = Warna
        
    def cetak_burung(self):
        super().cetak()
        print("Jenis \t\t\t: ", self.Jenis,
        "\nWarna \t\t\t: ", self.Warna)
    
Pipit = burung("Pipit", "Daun", "Udara", "Bertelur", "Bondol", 
"Merah")
Pipit.cetak_burung()

Merpati = burung("Merpati", "Daun", "Udara", "Bertelur", "Cumulet", 
"Putih")
Merpati.cetak_burung()
