class MahasiswaView:
    def tampilkan_list_mahasiswa(self, mahasiswa_list):
        print("Daftar Mahasiswa:")
        for mhs in mahasiswa_list:
            print(mhs)

    def tampilkan_detail_mahasiswa(self, mahasiswa):
        if mahasiswa:
            print("Detail Mahasiswa:")
            print(mahasiswa)
        else:
            print("Mahasiswa tidak ditemukan!")
