class person:
    def __init__(self, nama, umur, jekel):
        self.nama = nama
        self.umur = umur
        self.jekel = jekel

    def jalan(self):
        print(f"{self.nama} bisa berjalan")

    def ngomong(self):
        print(f"Dia berbicara karena dia {self.jekel}")
        
        
class supir(person):
    def __init__(self, nama, umur, jekel, sim):
        super().__init__(nama, umur, jekel)
        self.sim = sim
        
    def nyupir(self):
        print(f'{self.nama} bisa menyupir karena dia punya SIM {self.sim}')
        
        
class mahasiswa(person):
    def __init__(self, nama, umur, jekel, nim):
        super().__init__(nama, umur, jekel)
        self.nim = nim

    def belajar(self):
        print(f"{self.nama} sedang belajar dengan nim {self.nim}")

bayu = person("Bayu", 20, "Laki-laki")
bayu.jalan()
bayu.ngomong()

andi = supir("Andi", 30, "Laki-laki", "A")
andi.jalan()
andi.ngomong()
andi.nyupir()

bunga = mahasiswa("Bunga", 20, "Perempuan", "0110124108")
bunga.belajar()
