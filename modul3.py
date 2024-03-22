class Orang:
    def __init__(self, name, nim, prodi, hobi):
        self.name = name
        self.nim = nim
        self.prodi = prodi
        self.hobi = hobi
    
    def showName(self):
        print(f"Nama saya adalah: {self.name} dengan nim ({self.nim})")
    
    def showProdi(self):
        print(f"Saya dari prodi {self.prodi}")
    
    def showHobi(self):
        print(f"Hobi saya adalah menghasilkan {self.hobi}")

orang1 = Orang("Muhammad Hakim", "064002300027", "Teknik Informatika", "uang")
orang1.showName()
orang1.showProdi()
orang1.showHobi()


# class hitung:
#     def __init__(self,p,l):
#         self.p = p 
#         self.l = l
#     def luas(self):
#         luas = self.p * self.l
#         return luas
    
# persegi1 = hitung(20,12)
# persegi1.luas()
# print(f"persegi panjang,dengan panjang {persegi1.p} dan lebar {persegi1.l } hasilnya {persegi1.luas()}")
