import os
os.system ('cls')

def selectionsort(angka):
    for tujuan in range (len(angka)-1,0,-1):
        max = 0;
        for i in range(1, tujuan+1):
            max_temp = angka[max]
            if max_temp < angka[i]:
                max = i;
        angka[max],angka[tujuan] = angka[tujuan], angka[max]
    return angka;
    
angka = [15,7,3,10,80,34,8];
print('sebelum',angka);
selectionsort(angka);
print('sesudah',angka)

