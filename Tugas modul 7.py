def hitung_kecepatan_akhir(v0, a, t):
    return v0 + a * t

def hitung_jarak(v0, a, t):
    return v0 * t + 0.5 * a * t * t

n = int(input("Masukkan jumlah data: "))

hasil = []

for i in range(n):
    print("Data ke-", i + 1)
    v0 = float(input("Kecepatan awal (m/s): "))
    a = float(input("Percepatan (m/s^2): "))
    t = float(input("Waktu (s): "))

    v = hitung_kecepatan_akhir(v0, a, t)
    s = hitung_jarak(v0, a, t)

    hasil.append([v0, a, t, v, s])

print("\n" + "=" * 60)
print("TABEL HASIL PERHITUNGAN GLBB")
print("=" * 60)
print("v0(m/s)\ta(m/s^2)\tt(s)\tv(m/s)\ts(m)")
print("-" * 60)

for data in hasil:
    print(str(data[0]) + "\t" + str(data[1]) + "\t\t" + str(data[2]) + "\t" + str(data[3]) + "\t" + str(data[4]))
