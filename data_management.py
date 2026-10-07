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
menu_aktif = True
while menu_aktif:
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
        # WHILE: untuk menginput angka berkali-kali
        input_lagi = True
        while input_lagi:
            angka.append(int(input("Masukkan angka: ")))
            tanya = input("Tambah angka lagi? (y/n): ")
            if tanya.lower() != "y":
                input_lagi = False
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
        # WHILE: konfirmasi hapus data
        konfirmasi = True
        while konfirmasi:
            tanya_hapus = input("Yakin ingin menghapus semua data? (y/n): ")
            if tanya_hapus.lower() == "y":
                angka.clear()
                print("Data dihapus.")
                konfirmasi = False
            elif tanya_hapus.lower() == "n":
                print("Pembatalan. Data tidak dihapus.")
                konfirmasi = False
            else:
                print("Input tidak valid. Masukkan 'y' atau 'n'")
    
    elif pilih == "0":
        print("Selesai. Terima kasih!")
        menu_aktif = False
    
    else:
        print("Pilihan tidak valid.")
