class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

    def __str__(self):
        return f"NIM: {self.nim}, Nama: {self.nama}, Jurusan: {self.jurusan}"

class DataMahasiswa:
    def __init__(self):
        self.mahasiswa_list = []

    def tambah_mahasiswa(self, mahasiswa):
        self.mahasiswa_list.append(mahasiswa)

    def hapus_mahasiswa(self, nim):
        self.mahasiswa_list = [mhs for mhs in self.mahasiswa_list if mhs.nim != nim]

    def ubah_mahasiswa(self, nim, nama=None, jurusan=None):
        for mhs in self.mahasiswa_list:
            if mhs.nim == nim:
                if nama:
                    mhs.nama = nama
                if jurusan:
                    mhs.jurusan = jurusan
                break

    def cari_mahasiswa(self, nim):
        for mhs in self.mahasiswa_list:
            if mhs.nim == nim:
                return mhs
        return None

    def tampilkan_semua_mahasiswa(self):
        return self.mahasiswa_list
