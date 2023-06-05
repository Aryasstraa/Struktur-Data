import os
os.system ('cls')

def margesort(angka):
    jumlah = len(angka)
    if jumlah > 1:
        posisi_tengah = jumlah//2
        potong_kiri = angka[:posisi_tengah]
        potong_kanan = angka[posisi_tengah:]
        margesort(potong_kiri);
        margesort(potong_kanan);
        jumlah_kiri = len(potong_kiri)
        jumlah_kanan = len(potong_kanan)
        c_all,c_kiri,c_kanan = 0,0,0
        while c_kiri < jumlah_kiri or c_kanan < jumlah_kanan:
            # elemen di potongan kiri habis
            if c_kiri == jumlah_kiri:
                # menggabungkan angka
                angka[c_all] = potong_kanan[c_kanan]
                c_kanan = c_kanan +1
            # elemen di potongan kanan hbis
            elif c_kanan == jumlah_kanan:
                # menggabungkan angka
                angka[c_all] = potong_kiri[c_kiri]
                c_kiri = c_kiri +1
            # membandingkan nilai elemen  kiri lebih kecil dari kanan
            elif potong_kiri[c_kiri] <= potong_kanan[c_kanan]:
                angka[c_all] = potong_kiri[c_kiri]
                c_kiri = c_kiri+1
            # membandingkan nilai elemen kanan lebih besar kiri
            else :
                angka[c_all] = potong_kanan[c_kanan]
                c_kanan = c_kanan +1
            c_all = c_all +1
            
angka = [1,3,2,5,9,6,45,86,82]
print(f'sebelum', angka)
margesort(angka)
print(f'sesudah', angka)