from prettytable import PrettyTable

# Initial Data
data = [
    ["NAZ1939", "Mein Kampf", "Hitler, Adolf", 10, 10],
    ["RUS1848", "The Communist Manifest", "Marx, Karl", 9, 9],
    ["ITA1932", "The Doctrine of Fascism", "Mussolini, Benito", 8, 8],
    ["CHI1964", "The Little Red Book", "Zedong, Mao", 7, 7],
    ["RUS1917", "The State and Revolution", "Lenin, Vladimir", 6, 6],
    ["ITA1934", "Revolt Against the Modern World", "Evola, Julius", 5, 5],
    ["IND1957", "Masjarakat Indonesia dan Revolusi Indonesia", "Aidit, Dipa Nusantara", 4, 4],
    ["IND1983", "Catatan Seorang Demonstran", "Gie, Soe Hok", 3, 3],
    ["IND2015", "Perencanaan dan Analisis IEEE 802.11n Sebagai Backhaul", "Pangestu, Hendro Iman", 2, 2]
]

while True:
    print()
    print("SISTEM MANAJEMEN PERPUSTAKAAN")
    print("1. Menampilkan daftar buku")
    print("2. Menambah buku baru")
    print("3. Menghapus buku (Berdasarkan ID)")
    print("4. Mengubah data buku (Berdasarkan ID)")
    print("5. Pinjam Buku")
    print("6. Exit Program")
    print()

    input1 = input("Masukkan nomor menu: ")

    # 1. SHOW DATA
    if input1 == "1":
        if not data:
            print()
            print("[!] Perpustakaan kosong.")
        else:
            table = PrettyTable()
            table.field_names = ["No", "ID Buku", "Judul", "Author", "Stock Total", "Stock"]
            for i, book in enumerate(data):
                table.add_row([i, book[0], book[1], book[2], book[3], book[4]])
            print()
            print("DAFTAR BUKU TERSEDIA:")
            print(table)

    # 2. ADD DATA
    elif input1 == "2":
        print()
        id_buku = input("Masukkan ID Buku: ").upper()
        exists = any(book[0] == id_buku for book in data)
        if exists:
            print(f"[!] Gagal: Buku dengan ID {id_buku} sudah ada.")
        else:
            try:
                judul = input("Masukkan Judul: ")
                author = input("Masukkan Author: ")
                st_total = int(input("Masukkan Stock Total: "))
                data.append([id_buku, judul, author, st_total, st_total])
                print(f"[+] BERHASIL: Buku '{judul}' telah disimpan.")
            except ValueError:
                print("[!] ERROR: Stock harus berupa angka.")

    # 3. DELETE DATA (Modified to strictly use ID Buku)
    elif input1 == "3":
        print()
        id_hapus = input("Masukkan ID Buku yang ingin dihapus: ").upper()
        
        # Use a flag to track if we found the book
        found_index = -1
        for i in range(len(data)):
            if data[i][0] == id_hapus:
                found_index = i
                break
        
        if found_index != -1:
            # Save the title before popping to show it in the message
            judul_terhapus = data[found_index][1]
            data.pop(found_index)
            print(f"[-] BERHASIL: Buku '{judul_terhapus}' (ID: {id_hapus}) telah dihapus.")
        else:
            print(f"[!] ERROR: ID Buku '{id_hapus}' tidak ditemukan.")

    # 4. UPDATE DATA
    elif input1 == "4":
        print()
        id_ubah = input("Masukkan ID Buku yang ingin diubah: ").upper()
        book_index = -1

        for i, book in enumerate(data):
            if book[0] == id_ubah:
                book_index = i
                break
        
        if book_index != -1:
            current_book = data[book_index]
            print(f"[*] Mengubah data untuk ID: {current_book[0]}")
            
            new_judul = input(f"Masukkan Judul baru ({current_book[1]}): ") or current_book[1]
            new_author = input(f"Masukkan Author baru ({current_book[2]}): ") or current_book[2]
            
            try:
                new_st_total_str = input(f"Masukkan Stock Total baru ({current_book[3]}): ")
                new_st_total = int(new_st_total_str) if new_st_total_str else current_book[3]
                
                # Update list (ID remains the same)
                data[book_index] = [id_ubah, new_judul, new_author, new_st_total, new_st_total]
                print("[+] Data berhasil diperbarui!")
            except ValueError:
                print("[!] ERROR: Stock harus berupa angka. Pembaharuan dibatalkan.")
        else:
            print(f"[!] ID {id_ubah} tidak ditemukan.")

    # 5. PINJAM BUKU
    elif input1 == "5":
        print()
        id_pinjam = input("Masukkan ID Buku yang ingin dipinjam: ").upper()
        book_found = False

        for book in data:
            if book[0] == id_pinjam:
                book_found = True
                if book[4] <= 0:
                    print("[!] WARNING: Stok buku habis, tidak dapat dipinjam.")
                else:
                    book[4] -= 1
                    print(f"[+] BERHASIL: Meminjam '{book[1]}'. Sisa stok: {book[4]}")
                break
        
        if not book_found:
            print(f"\n[!] ERROR: ID {id_pinjam} tidak ditemukan.")

    # 6. EXIT
    elif input1 == "6":
        print()
        print("Terima kasih telah menggunakan sistem perpustakaan. Keluar...")
        break
    
    else:
        print()
        print("[!] Menu tidak valid. Silakan masukkan angka 1-6.")
