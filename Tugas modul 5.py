data_mahasiswa = []

while True:
    print("Menu Manajemen Data Mahasiswa")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Data")
    print("4. Keluar")
    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == '1':
        no = input("Masukkan Nomor Mahasiswa: ")
        nama = input("Masukkan Nama Mahasiswa: ")
        nilai_input = input("Masukkan Nilai Mahasiswa: ")
        nilai = float(nilai_input)
        data_mahasiswa.append([no, nama, nilai])
        print("Data berhasil ditambahkan.")

    elif pilihan == '2':
        no_hapus = input("Masukkan Nomor Mahasiswa yang akan dihapus: ")
        i = 0
        ketemu = False
        while i < len(data_mahasiswa):
            if data_mahasiswa[i][0] == no_hapus:
                del data_mahasiswa[i]
                print("Data berhasil dihapus.")
                ketemu = True
                break
            i += 1
        if ketemu == False:
            print("Data tidak ditemukan.")

    elif pilihan == '3':
        if len(data_mahasiswa) == 0:
            print("Belum ada data.")
        else:
           
            n = len(data_mahasiswa)
            for i in range(n):
                for j in range(0, n-i-1):
                    if data_mahasiswa[j][2] < data_mahasiswa[j+1][2]:
                        data_mahasiswa[j], data_mahasiswa[j+1] = data_mahasiswa[j+1], data_mahasiswa[j]

            print("Data Mahasiswa (Urut Nilai Tertinggi):")
            print(("No", "Nama", "Nilai"))
            for i in range(len(data_mahasiswa)):
                print((data_mahasiswa[i][0], data_mahasiswa[i][1], data_mahasiswa[i][2]))
            print()

    elif pilihan == '4':
        print("Program selesai.")
        break

    else:
        print("Angka tidak valid.")
