# Tabel konversi nilai huruf ke angka
konversi_nilai = [
    ["A", 4.00],
    ["A-", 3.75],
    ["B+", 3.50],
    ["B", 3.00],
    ["B-", 2.75],
    ["C+", 2.50],
    ["C", 2.00],
    ["D", 1.00],
    ["E", 0.00]
]

# Input jumlah mahasiswa dan mata kuliah
jml_mhs = int(input("Jumlah mahasiswa: "))
jml_mk = int(input("Jumlah mata kuliah: "))

data = []

for i in range(jml_mhs):
    print("Mahasiswa ke-", i + 1)
    nama = input("Nama: ")
    daftar_nilai = []
    total = 0
    for j in range(jml_mk):
        valid = 0
        while valid == 0:
            nilai = input("Nilai mata kuliah ke-" + str(j + 1) + ": ")
            angka = -1
            for k in range(len(konversi_nilai)):
                if nilai == konversi_nilai[k][0]:
                    angka = konversi_nilai[k][1]
                    valid = 1
            if angka != -1:
                daftar_nilai.append(nilai)
                total = total + angka
    ip = total / jml_mk
    data.append([nama, daftar_nilai, ip])
    print("IP",ip)

# Urutkan berdasarkan IP tertinggi (bubble sort)
for i in range(len(data)):
    for j in range(len(data) - i - 1):
        if data[j][2] < data[j + 1][2]:
            sementara = data[j]
            data[j] = data[j + 1]
            data[j + 1] = sementara

# Tampilkan hasil
print("=" * 50)
print("Data Mahasiswa dan IP")
print("=" * 50)
print("Nama           Nilai                    IP")
print("-" * 50)

for i in range(len(data)):
    teks = data[i][0]
    while len(teks) < 15:
        teks = teks + " "
    teks = teks + str(data[i][1])
    while len(teks) < 42:
        teks = teks + " "
    teks = teks + str(data[i][2])
    print(teks)
