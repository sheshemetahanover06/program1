from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import MahasiswaView

def menu_utama():
    data_mahasiswa = DataMahasiswa()
    mahasiswa_view = MahasiswaView()

    while True:
        print("\nMenu Utama")
        print("1. Tambah Data Mahasiswa")
        print("2. Hapus Data Mahasiswa")
        print("3. Ubah Data Mahasiswa")
        print("4. Cari Data Mahasiswa")
        print("5. Tampilkan Semua Mahasiswa")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            form = InputForm()
            form.input_data()
            mahasiswa = Mahasiswa(form.nim, form.nama, form.jurusan)
            data_mahasiswa.tambah_mahasiswa(mahasiswa)
            print("Data mahasiswa berhasil ditambahkan.")

        elif pilihan == "2":
            nim = input("Masukkan NIM yang akan dihapus: ")
            data_mahasiswa.hapus_mahasiswa(nim)
            print("Data mahasiswa berhasil dihapus.")

        elif pilihan == "3":
            nim = input("Masukkan NIM yang akan diubah: ")
            nama = input("Masukkan Nama baru (kosongkan untuk tidak mengubah): ")
            jurusan = input("Masukkan Jurusan baru (kosongkan untuk tidak mengubah): ")
            data_mahasiswa.ubah_mahasiswa(nim, nama, jurusan)
            print("Data mahasiswa berhasil diubah.")

        elif pilihan == "4":
            nim = input("Masukkan NIM yang akan dicari: ")
            mahasiswa = data_mahasiswa.cari_mahasiswa(nim)
            mahasiswa_view.tampilkan_detail_mahasiswa(mahasiswa)

        elif pilihan == "5":
            mahasiswa_list = data_mahasiswa.tampilkan_semua_mahasiswa()
            mahasiswa_view.tampilkan_list_mahasiswa(mahasiswa_list)

        elif pilihan == "6":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    menu_utama()