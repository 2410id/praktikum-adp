# soal pertama

baris = int(input("Masukkan jumlah baris: "))
kolom = int(input("Masukkan jumlah kolom: "))

# Perulangan bersarang untuk mencetak pola
for i in range(baris):
    for j in range(kolom):
        if (i + j) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()  

