class InputForm:
    def __init__(self):
        self.nim = ""
        self.nama = ""
        self.jurusan = ""

    def input_data(self):
        self.nim = input("Masukkan NIM: ")
        self.nama = input("Masukkan Nama: ")
        self.jurusan = input("Masukkan Jurusan: ")

    def tampilkan_data(self):
        print(f"NIM: {self.nim}, Nama: {self.nama}, Jurusan: {self.jurusan}")
