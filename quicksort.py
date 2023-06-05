import os
os.system ('cls')

# Berfungsi untuk melakukan Penyortiran Cepat
def quick_sort(angka):
    # fungsi melakukan pemeriksaan apabila angka kurang dari atau sama dengan 1, maka fungsi akan mengembalikan angka
    if len(angka) <= 1:
        return angka
    else:
        # Pilih elemen pivot
        pivot = angka[0]
        kiri = []
        kanan = []
        # Bagi elemen menjadi dua daftar
        for i in angka[1:]:
            # jika angka memiliki lebih dari 1 elemen, maka fungsi pertama angka sebagai pivot
            if i < pivot:
                kiri.append(i)
            else:
                kanan.append(i)
        # Mengurutkan daftar kiri dan kanan secara rekursif dan menggabungkan list hasil pengurutan 
        return quick_sort(kiri) + [pivot] + quick_sort(kanan)

# Masukan angka 
angka = []
jumlah = int(input("Masukan Jumlah Angka Yang Ingin Diurutkan: "))
for i in range(jumlah):
    masukan_angka = int(input("Masukan Angka: "))
    angka.append(masukan_angka)

# cetak 
print("=====================")
print("Sebelum:", angka)
angka = quick_sort(angka)
print("Sesudah:", angka)
