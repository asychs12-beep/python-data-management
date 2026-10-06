#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program Manajemen Data Dinamis
Fitur: List, Sort, For, While dalam satu program
Dibuat dengan menu pilihan interaktif
"""

def tampilkan_menu():
    """Menampilkan menu utama program"""
    print("\n" + "="*50)
    print("      PROGRAM MANAJEMEN DATA DINAMIS")
    print("="*50)
    print("1. Lihat semua data")
    print("2. Tambah data baru")
    print("3. Urutkan data (A-Z)")
    print("4. Urutkan data (Z-A)")
    print("5. Hapus data")
    print("6. Cari data")
    print("7. Statistik data")
    print("8. Keluar")
    print("="*50)

def lihat_data(data):
    """Menampilkan semua data dengan nomor urut"""
    if len(data) == 0:
        print("\n⚠️  Data kosong! Silakan tambahkan data terlebih dahulu.")
        return
    
    print("\n📋 DAFTAR DATA:")
    print("-" * 50)
    for i, item in enumerate(data, 1):
        print(f"{i}. {item}")
    print("-" * 50)
    print(f"Total data: {len(data)}")

def tambah_data(data):
    """Menambah data baru secara dinamis dengan while loop"""
    print("\n➕ TAMBAH DATA BARU")
    print("-" * 50)
    
    jumlah = 0
    while True:
        try:
            input_jumlah = input("Berapa banyak data yang ingin ditambahkan? ")
            jumlah = int(input_jumlah)
            if jumlah <= 0:
                print("❌ Jumlah harus positif! Coba lagi.")
                continue
            break
        except ValueError:
            print("❌ Input tidak valid! Masukkan angka.")
    
    i = 0
    while i < jumlah:
        item = input(f"Data ke-{i+1}: ").strip()
        
        if item == "":
            print("⚠️  Data tidak boleh kosong! Coba lagi.")
            continue
        
        if item in data:
            print("⚠️  Data sudah ada! Coba dengan data lain.")
            continue
        
        data.append(item)
        print(f"✅ Data '{item}' berhasil ditambahkan!")
        i += 1
    
    print(f"\n✨ Total {jumlah} data berhasil ditambahkan!")

def urutkan_data(data, ascending=True):
    """Mengurutkan data secara ascending atau descending"""
    if len(data) == 0:
        print("\n⚠️  Data kosong! Tidak ada yang bisa diurutkan.")
        return
    
    data_sorted = sorted(data, reverse=not ascending)
    urutan = "A-Z" if ascending else "Z-A"
    
    print(f"\n📊 DATA TERURUT ({urutan}):")
    print("-" * 50)
    for i, item in enumerate(data_sorted, 1):
        print(f"{i}. {item}")
    print("-" * 50)
    
    tanya = input("Simpan urutan ini ke data asli? (y/n): ").lower()
    if tanya == 'y':
        data.clear()
        for item in data_sorted:
            data.append(item)
        print("✅ Data berhasil diurutkan dan disimpan!")
    else:
        print("⚠️  Perubahan tidak disimpan.")

def hapus_data(data):
    """Menghapus data tertentu dari list"""
    if len(data) == 0:
        print("\n⚠️  Data kosong! Tidak ada yang bisa dihapus.")
        return
    
    print("\n🗑️  HAPUS DATA")
    print("-" * 50)
    
    lihat_data(data)
    
    while True:
        try:
            pilihan = int(input("\nNomor data yang ingin dihapus (0 untuk batal): "))
            
            if pilihan == 0:
                print("❌ Pembatalan.")
                return
            
            if 1 <= pilihan <= len(data):
                item_dihapus = data.pop(pilihan - 1)
                print(f"✅ Data '{item_dihapus}' berhasil dihapus!")
                break
            else:
                print("❌ Nomor tidak valid! Coba lagi.")
        except ValueError:
            print("❌ Input harus berupa angka!")

def cari_data(data):
    """Mencari data tertentu dalam list"""
    if len(data) == 0:
        print("\n⚠️  Data kosong! Tidak ada yang bisa dicari.")
        return
    
    print("\n🔍 CARI DATA")
    print("-" * 50)
    
    pencarian = input("Masukkan keyword pencarian: ").strip().lower()
    
    if pencarian == "":
        print("⚠️  Keyword tidak boleh kosong!")
        return
    
    hasil = []
    for i, item in enumerate(data, 1):
        if pencarian in item.lower():
            hasil.append((i, item))
    
    if len(hasil) == 0:
        print(f"❌ Data dengan keyword '{pencarian}' tidak ditemukan.")
    else:
        print(f"\n✅ Ditemukan {len(hasil)} hasil pencarian:")
        print("-" * 50)
        for nomor, item in hasil:
            print(f"{nomor}. {item}")

def statistik_data(data):
    """Menampilkan statistik data"""
    if len(data) == 0:
        print("\n⚠️  Data kosong! Tidak ada statistik yang bisa ditampilkan.")
        return
    
    print("\n📈 STATISTIK DATA")
    print("-" * 50)
    print(f"Total data: {len(data)}")
    print(f"Data terpendek: {min(data, key=len)}")
    print(f"Data terpanjang: {max(data, key=len)}")
    
    # Hitung rata-rata panjang karakter
    total_karakter = 0
    for item in data:
        total_karakter += len(item)
    
    rata_rata = total_karakter / len(data)
    print(f"Rata-rata panjang karakter: {rata_rata:.2f}")
    
    # Data berurutan
    data_terurut = sorted(data)
    print(f"Data pertama (urutan A-Z): {data_terurut[0]}")
    print(f"Data terakhir (urutan Z-A): {data_terurut[-1]}")
    print("-" * 50)

def main():
    """Fungsi utama program"""
    data = []
    
    print("🎉 Selamat datang di Program Manajemen Data Dinamis!")
    
    while True:
        tampilkan_menu()
        pilihan = input("\nPilih menu (1-8): ").strip()
        
        if pilihan == "1":
            lihat_data(data)
        
        elif pilihan == "2":
            tambah_data(data)
        
        elif pilihan == "3":
            urutkan_data(data, ascending=True)
        
        elif pilihan == "4":
            urutkan_data(data, ascending=False)
        
        elif pilihan == "5":
            hapus_data(data)
        
        elif pilihan == "6":
            cari_data(data)
        
        elif pilihan == "7":
            statistik_data(data)
        
        elif pilihan == "8":
            print("\n" + "="*50)
            print("👋 Terima kasih telah menggunakan program ini!")
            print("Sampai jumpa lagi!")
            print("="*50)
            break
        
        else:
            print("\n❌ Pilihan tidak valid! Silakan pilih menu 1-8.")
        
        input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()
