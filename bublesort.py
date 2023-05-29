import os
os.system('cls')

# definisi
def bubleSort(arr):
    # menentukan panjang
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                # menukar posisi
                # temp adalah array j
                temp = arr[j]
                # yang sebelumnya arr j diubah menjadi arr j +1
                arr[j] = arr[j+1]
                # kemudian diposisikan kembali ke temp
                arr[j+1] = temp
                
buble = [5,1,2,7,84,6,90]

bubleSort(buble)
print(buble)                                