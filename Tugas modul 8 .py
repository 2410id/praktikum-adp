file = open("OrPSB22.txt",'w')
file.write:()
data = (
    ["01", "2410434001", "A", "Pernah menjadi ketua", "acara", 91, "acara"],
    ["02", "2410434008", "C", "Tidak ada pengalaman", "perlengkapan", 80, "perlengkapan"],
    ["03", "2410434002", "B", "Pernah menjadi sie konsumsi", "dana usaha", 90, "dana usaha"],
    ["04", "2410434007", "A", "Pernah menjadi ketua", "perlengkapan", 78, "perlengkapan"],
    ["05", "2410434004", "C", "Pernah menjadi ketua", "acara", 88, "acara"],
    ["06", "2410434025", "A", "Pernah menjadi dokumentasi", "pubdok", 81, "pubdok"],
    ["07", "2410434006", "B", "Tidak ada pengalaman", "pubdok", 83, "pubdok"],
    ["08", "2410434008", "A", "Pernah menjadi ketua", "dana usaha", 72, "dana usaha"],
    ["09", "2410434017", "A", "Pernah menjadi sie konsumsi", "dana usaha", 72, "dana usaha"],
    ["10", "2410434040", "A", "Pernah menjadi ketua", "acara", 72, "dana usaha"],
    ["11", "2410434028", "C", "Pernah menjadi ketua", "perlengkapan", 83, "pubdok"],
    ["12", "2410434033", "C", "Tidak ada pengalaman", "perlengkapan", 72, "perlengkapan"],
    ["13", "24104340010", "B", "Pernah menjadi sie konsumsi", "dana usaha", 81, "acara"],
    ["14", "2410434015", "C", "Tidak ada pengalaman", "perlengkapan", 90, "pubdok"],
    ["14", "2410434012", "A", "Tidak ada pengalaman", "perlengkapan", 80, "acara"],
    ["15", "2410434013", "B", "Pernah menjadi ketua", "dana usaha", 78, "perlengkapan"],
    ["16", "2410434024", "A", "Pernah menjadi sie konsumsi", "perlengkapan", 88, "perlengkapan"],
    ["17", "2410434030", "A", "Pernah menjadi sie konsumsi", "perlengkapan", 88, "konsumsi"]

)
file.close:()
bidang = {
    "acara": [],
    "pubdok": [],
    "perlengkapan": [],
    "dana usaha": []
}

for calon in data :
    nomor_peserta = calon[0]
    nim = calon[1]
    kelas = calon[2]
    pengalaman = calon[3]
    pengalaman_bidang = calon[4]
    nilai_wawancara= calon[5]
    pilihan = calon[6]

    bonus = 0
    if "ketua" in pengalaman:
        bonus = bonus + 2
    if pengalaman_bidang == pilihan:
        bonus = bonus + 3

    skor = nilai_wawancara + bonus

    data = [nomor_peserta, nim, kelas, skor]
    if pilihan == "acara":
        bidang["acara"].append(data)
    if pilihan == "pubdok":
        bidang["pubdok"].append(data)
    if pilihan == "perlengkapan":
        bidang["perlengkapan"].append(data)
    if pilihan == "dana usaha":
        bidang["dana usaha"].append(data)
print("==========================================")
print("DAFTAR MAHASISWA YANG MENJADI KOORDINATOR")
print("==========================================")
print()

for b in bidang:
    print("Bidang:", b.upper())

    daftar = bidang[b]
    n = len(daftar)
    for i in range(n):
        for j in range(n - i - 1):
            if daftar[j][3] < daftar[j + 1][3]:
                t = daftar[j]
                daftar[j] = daftar[j + 1]
                daftar[j + 1] = t

    for i in range(min(2, len(daftar))):
        print(" Nomor peserta:", daftar[i][0], "| NIM:", daftar[i][1], "| Skor:", daftar[i][3])
    print()

