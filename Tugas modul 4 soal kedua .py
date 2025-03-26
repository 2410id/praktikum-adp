# soal kedua
if len(password) < 8 = False
    
    # Inisialisasi variabel pengecekan
    has_lower = has_upper = has_digit = has_special = False
    special_characters = ("!@#$%*&()-_=[]{}|;:'\",.<>?/`~")

    # Perulangan untuk memeriksa setiap karakter dalam password
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

# Perulangan utama untuk meminta input hingga password valid
while True:
    password = input("Masukkan password: ")
    if is_valid_password(password):
        print("Password valid!")
        break
    else
        print("Password tidak valid! Harus mengandung minimal 1 huruf kecil,"
        "1 huruf besar,1 angka,1 karakter khusus,dan panjang minimal 8 karakter, masukkan ulang password.")