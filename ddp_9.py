def celcius_ke_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit 

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))

print('---- Mencari bilangan genap ----')


def is_genap(bil_genap):
    return bil_genap % 2 == 0
# untuk memasukan value
print(is_genap(4))
print(is_genap(7)) 

print('\n---- Mencari nilai kelulusan ----')
#rata"nilai 70
def nilai_kelulusan(nilai):
    if nilai >= 80:
        return 'lulus'
    else:
        return 'tidak lulus'
    
# untuk mencetak value
print(nilai_kelulusan(80))
print(nilai_kelulusan(60))

print('\n ---- cetak bilangan ganjil ----')
def bilangan_ganjil(angka):
    for i in range(1, angka, 2):
        print(i, end=" ")

# untuk mencetak value
bilangan_ganjil(20)
print('\n')
        
