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
            print("Linked list is empty.")
        else:
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print()

    def isEmpty(self):
        return self.head is None

    def remove(self, data):
        if self.head is None:
            print("Linked list is empty.")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

        print("Element not found in the linked list.")

    def search(self, data):
        if self.head is None:
            print("Linked list is empty.")
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
            count += 1
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
            if current_node != min_node:
                current_node.data, min_node.data = min_node.data, current_node.data
            current_node = current_node.next

    def mainmenu(self):
        pilih = 'y'
        while pilih == 'y':
            print("Menu:")
            print("1. Add")
            print("2. Show")
            print("3. Is Empty")
            print("4. Remove")
            print("5. Search")
            print("6. Size")
            print("7. Sort")
            print("8. Quit")

            pilihan = input("Masukkan pilihan Anda: ")

            if pilihan == '1':
                data = int(input("Masukkan data yang ingin ditambahkan: "))
                self.add(data)
                print("Data telah ditambahkan ke linked list.")

            elif pilihan == '2':
                self.show()

            elif pilihan == '3':
                if self.isEmpty():
                    print("Linked list kosong.")
                else:
                    print("Linked list tidak kosong.")

            elif pilihan == '4':
                data = int(input("Masukkan data yang ingin dihapus: "))
                self.remove(data)

            elif pilihan == '5':
                data = int(input("Masukkan data yang ingin dicari: "))
                if self.search(data):
                    print("Data ditemukan dalam linked list.")
                else:
                    print("Data tidak ditemukan dalam linked list.")

            elif pilihan == '6':
                size = self.size()
                print("Ukuran linked list: ", size)

            elif pilihan == '7':
                self.selection_sort()
                print("Linked list telah diurutkan menggunakan Selection Sort.")

            elif pilihan == '8':
                break

            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

# Contoh penggunaan
linked_list = LinkedList()
linked_list.mainmenu()
