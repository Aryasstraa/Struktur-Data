import os
os.system('cls')

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def show(self):
        if self.head is None:
            print("Linked list Kosong.")
        else:
            current = self.head
            print("Show Data:")
            while current:
                print(f"-> {current.data}")
                current = current.next
            print()

    def isEmpty(self):
        return self.head is None

    def remove(self, data):
        if self.head is None:
            print("Linked list Kosong.")
            return

        if self.head.data == data:
            self.head = self.head.next
            print("Data berhasil dihapusssss.")
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                print("Data berhasil dihapus.")
                return
            current = current.next

        print("Data tidak ditemukan.")

    def search(self, data):
        if self.head is None:
            print("Linked list Kosong.")
            return False

        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next

        return False

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1 # += artinya penjumlahan
            current = current.next
        return count

    def selection_sort(self):
        # Menerapkan selection sort pada linked list
        current_node = self.head
        while current_node:
            min_node = current_node
            next_node = current_node.next
            while next_node:
                if next_node.data < min_node.data:
                    min_node = next_node
                next_node = next_node.next
            if current_node != min_node: # =! artinya tidak sama dengan
                current_node.data, min_node.data = min_node.data, current_node.data
            current_node = current_node.next

    def mainmenu(self):
        pilih = 'y'
        while pilih == 'y':
            # Menampilkan judul dan menu
            print("==========================")
            print("*     KELOMPOK 6 UAS     *")
            print("==========================\n")
            print("Menu:")
            print("1. Masukan Data")
            print("2. Show Data")
            print("3. Is Empty")
            print("4. Remove Data")
            print("5. Search Data")
            print("6. Size")
            print("7. Sort Data")
            print("8. Quit Program")
            print("==========================")

            # Meminta input dari pengguna
            pilihan = input("Masukkan pilihan Anda: ")

            # Menjalankan aksi sesuai dengan pilihan pengguna
            if pilihan == '1':
                # Menambahkan data ke linked list
                os.system('cls')
                data = int(input("Masukkan data yang ingin ditambahkan: "))
                self.add(data)
                print(f"Data {data} telah ditambahkan ke linked list.")
            elif pilihan == '2':
                # Menampilkan data dalam linked list
                os.system('cls')
                self.show()
            elif pilihan == '3':
                # Memeriksa apakah linked list kosong
                os.system('cls')
                if self.isEmpty():
                    print("Data kosong.")
                else:
                    print("Data tidak kosong.")
            elif pilihan == '4':
                # Menghapus data dari linked list
                os.system('cls')
                data = int(input("Masukkan data yang ingin dihapus: "))
                self.remove(data)
            elif pilihan == '5':
                # Mencari data dalam linked list
                os.system('cls')
                data = int(input("Masukkan data yang ingin dicari: "))
                if self.search(data):
                    print(f"Data {data} ditemukan dalam linked list.")
                else:
                    print(f"Data {data} tidak ditemukan dalam linked list.")
            elif pilihan == '6':
                # Menghitung ukuran linked list
                os.system('cls')
                size = self.size()
                print(f"Ukuran linked list: {size}")
            elif pilihan == '7':
                # Mengurutkan data dalam linked list menggunakan Selection Sort
                os.system('cls')
                self.selection_sort()
                print("Linked list telah diurutkan menggunakan Selection Sort.")
            elif pilihan == '8':
                # Keluar dari program
                break
            else:
                # Menangani pilihan yang tidak valid
                print("Pilihan tidak valid. Silakan coba lagi.")


linked_list = LinkedList()
linked_list.mainmenu()