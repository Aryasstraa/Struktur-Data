import os
os.system('cls')

def insertionSort(arr):
    for i in range (1,len(arr)):
        # simpan value disimpan di sebuah variable i
        key = arr[i].lower()
        j = i-1
        # melakukan while 
        while j >= 0 and key.lower() < arr[j].lower():
            # maka lakukan pemindahan
            arr[j+1] = arr[j]
            j-=1
            arr[j+1] = key
            
# i = int(input("Masukan Array : " ))
# insertion = []
# for i in range(i):
#     print("NIlai ke ",i+1,sep=' ',end=" : ")
#     insertion.append(int(input()))


insertion = ["ABC","abc","Abc","Aad"]
# loop = int(input("Masukan Nilai ? " ))
# for i in range(1 , loop):
#     inp = int(input("Masukan Nilai ke " + str(i)))
#     insertion.append(inp)
insertionSort(insertion)
print(insertion)

