while True:  # Tambahkan while loop
    print(30 * "=")
    print("kalkulator sederhanaaaa")
    print(30 * "=")

    num1 = float(input("Masukkan angka 1 = "))
    operator = input("Pilih Operator (-,+,x,/) =")
    num2 = float(input("Masukkan angka 2 = "))

    if operator == "-":
        hasil = num1 - num2
        print(f"hasilnya yaitu {hasil}")
    elif operator == "+":
        hasil = num1 + num2
        print(f"hasilnya yaitu {hasil}")
    elif operator == "x":
        hasil = num1 * num2
        print(f"hasilnya yaitu {hasil}")
    elif operator == "/":
        hasil = num1 / num2
        print(f"hasilnya yaitu {hasil}")
    else:
        print("Input yang anda masukkan salah!")
        ulang = input("Apakah Anda ingin mencoba lagi? (y/n): ")
        if ulang.lower() != 'y':
            break  # Keluar dari loop jika pengguna tidak ingin mengulang
        else:
            continue  # Ulangi jika pengguna ingin mencoba lagi

    break  # Keluar dari loop setelah operasi berhasil

# Pesan ini hanya akan muncul jika pengguna selesai menggunakan kalkulator
print(20 * "=", "Terima kasih telah mencoba kalkulator sederhana ini", 20 * "=")
