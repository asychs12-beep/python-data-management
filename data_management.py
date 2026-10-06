import random

print("=== START ===")
# LIST: tempat menyimpan angka
angka = [5, 3, 8, 1, 9, 2, 4, 6, 7]

def tampilkan():
    if not angka:
        print("Data masih kosong.")
        return
    print("Data:", end=" ")
    # FOR: menampilkan setiap angka
    for n in angka:
        print(n, end=" ")
    print()

# WHILE: menu berulang sampai pilih keluar
while True:
    print("\n=== MENU DATA ANGKA ===")
    print("1. Isi angka urutan (1 sampai N)")
    print("2. Tambah angka manual")
    print("3. Urutkan naik (sort)")
    print("4. Urutkan turun (sort)")
    print("5. Tampilkan data")
    print("6. Hapus semua data")
    print("0. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        n = int(input("Sampai angka berapa? "))
        angka = []
        for i in range(1, n + 1):
            angka.append(i)
        tampilkan()
    elif pilih == "2":
        angka.append(int(input("Masukkan angka: ")))
        tampilkan()
    elif pilih == "3":
        angka.sort()
        tampilkan()
    elif pilih == "4":
        angka.sort(reverse=True)
        tampilkan()
    elif pilih == "5":
        tampilkan()
    elif pilih == "6":
        angka.clear()
        print("Data dihapus.")
    elif pilih == "0":
        print("Selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")
