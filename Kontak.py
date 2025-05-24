print('Daftar Kontak')

def main():
    kontak = []

    while True:
        print('\nMenu:')
        print('1. Cari Kontak')  
        print('2. Tampilkan Kontak')
        print('3. Tambah Kontak') 
        print('4. Hapus Kontak')
        print('5. Keluar')

        pilihan = input('Pilih menu (1-5): ')
        if not pilihan.isdigit() or int(pilihan) not in {1, 2, 3, 4, 5}:
            print('Input tidak valid. Silakan masukkan angka 1-5.')
            continue
        pilihan = pilihan.strip()
        if pilihan == '':
            print('Input tidak boleh kosong. Silakan masukkan angka 1-5.')
            continue
        if pilihan not in {'1', '2', '3', '4', '5'}:
            print('Input tidak valid. Silakan masukkan angka 1-5.')
            continue
        pilihan = pilihan.strip()
        if pilihan == '':
            print('Input tidak boleh kosong. Silakan masukkan angka 1-5.')
            continue
       
        if pilihan == '1':
            cari_kontak(kontak)
        elif pilihan == '2':
            tampilkan_kontak(kontak)         
        elif pilihan == '3':    
            tambah_kontak(kontak)
        elif pilihan == '4':
            hapus_kontak(kontak)    
        
            
        # elif pilihan == '5': # bawaan
        #     keluar = input('Apakah Anda yakin ingin keluar? (y/n): ').strip().lower()
        #     if keluar == 'y':
        #         print('Program dihentikan.')
        #         break
        #     elif keluar == 'n':
        #         print('Kembali ke menu utama.') 
                
        #     else:
        #         print('Input tidak valid. Silakan masukkan "y" atau "n".')
        #         continue
        
        # elif pilihan == '5': #gpt
        #     while True:
        #         keluar = input('Apakah Anda yakin ingin keluar? (y/n): ').strip().lower()
        #         if keluar == 'y':
        #             print('Program dihentikan.')
        #             break
        #         elif keluar == 'n':
        #             print('Kembali ke menu utama.')
        #             break
        #         else:
        #             print('Input tidak valid. Silakan masukkan "y" atau "n".')
        #     if keluar == 'y':
        #         break  # keluar dari while True utama 
            
        elif pilihan == '5':
            while True:
                keluar = input('Apakah Anda yakin ingin keluar? (y/n): ').strip().lower()
                if keluar == 'y':
                    print('Program dihentikan.')
                    return  # Keluar dari fungsi main()
                elif keluar == 'n':
                    print('Kembali ke menu utama.')
                    break  # Keluar dari loop konfirmasi, kembali ke menu
                else:
                    print('Input tidak valid. Silakan masukkan "y" atau "n".')       
       
def tambah_kontak(kontak):      
    print('\nTambah Kontak (ketik "SELESAI" untuk kembali)')
    while True:
        nama = input("Nama kontak: ").strip()
        if nama.upper() == "SELESAI":
            break
        if not nama:
            print("Nama tidak boleh kosong.")
            continue
        nomor = input(f"Nomor {nama}: ").strip()
        if not nomor.isdigit():
            print("Nomor harus berupa angka.")
            continue
        kontak.append((nama, nomor))
        print(f"{nama} ditambahkan!")
def hapus_kontak(kontak):
    if not kontak:
        print("\nDaftar kosong.")
        return
    tampilkan_kontak(kontak)
    try:
        index = int(input("\nNomor kontak yang dihapus: ")) - 1
        nama, nomor = kontak.pop(index)
        print(f"{nama} dihapus!")
        tampilkan_kontak(kontak)
    except (ValueError, IndexError):
        print("Input tidak valid.")
def tampilkan_kontak(kontak):
    if not kontak:
        print("\nDaftar kosong.")
        return
    print("\nDaftar Kontak:")
    for i, (nama, nomor) in enumerate(kontak, start=1):
        print(f"{i}. {nama} - {nomor}") 
def cari_kontak(kontak):
    if not kontak:
        print("\nDaftar kosong.")
        return
    nama = input("Masukkan nama kontak yang dicari: ").strip()
    for i, (nama_kontak, nomor) in enumerate(kontak, start=1):
        if nama.lower() in nama_kontak.lower():
            print(f"{i}. {nama_kontak} - {nomor}")
            return
    print("Kontak tidak ditemukan.")   
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        print("Program dihentikan.")