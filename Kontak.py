print('Daftar Kontak')
import csv

CSV_FILE = "kontak.csv"

def load_kontak():
    kontak = []
    try:
        with open(CSV_FILE, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2:
                    kontak.append((row[0], row[1]))
    except FileNotFoundError:
        pass
    return kontak

def save_kontak(kontak):
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for nama, nomor in kontak:
            writer.writerow([nama, nomor])

def main():
    kontak = load_kontak()
    while True:
        print('\nMenu:')
        print('1. Cari Kontak')  
        print('2. Tampilkan Kontak')
        print('3. Tambah Kontak') 
        print('4. Hapus Kontak')
        print('5. Edit Kontak')
        print('6. Keluar')

        pilihan = input('Pilih menu (1-6): ')
        if not pilihan.isdigit() or int(pilihan) not in {1, 2, 3, 4, 5, 6}:
            print('Input tidak valid. Silakan masukkan angka 1-6.')
            continue
        if pilihan == '1':
            cari_kontak(kontak)
        elif pilihan == '2':
            tampilkan_kontak(kontak)         
        elif pilihan == '3':    
            tambah_kontak(kontak)
            save_kontak(kontak)
        elif pilihan == '4':
            hapus_kontak(kontak)
            save_kontak(kontak)
        elif pilihan == '5':
            edit_kontak(kontak)
            save_kontak(kontak)
        elif pilihan == '6':
            while True:
                keluar = input('Apakah Anda yakin ingin keluar? (y/n): ').strip().lower()
                if keluar == 'y':
                    print('Program dihentikan.')
                    save_kontak(kontak)
                    return
                elif keluar == 'n':
                    print('Kembali ke menu utama.')
                    break
                else:
                    print('Input tidak valid. Silakan masukkan "y" atau "n".')

def tambah_kontak(kontak):
    nama = input("Masukkan nama kontak: ").strip()
    nomor = input("Masukkan nomor kontak: ").strip()
    if not nama or not nomor:
        print("Nama dan nomor tidak boleh kosong.")
        return
    kontak.append((nama, nomor))
    print(f"{nama} - {nomor} telah ditambahkan!")
    tampilkan_kontak(kontak)
    
def hapus_kontak(kontak):
    if not kontak:
        print("\nDaftar kosong.")
        return
    tampilkan_kontak(kontak)
    try:
        index = int(input("\nNomor kontak yang dihapus: ")) - 1
        if 0 <= index < len(kontak):
            nama, nomor = kontak.pop(index)
            print(f"{nama} - {nomor} telah dihapus!")
        else:
            print("Nomor kontak tidak valid.")
    except (ValueError, IndexError):
        print("Input tidak valid.")
        
def tampilkan_kontak(kontak):
    if not kontak:
        print("\nDaftar kosong.")
        return
    print("\nDaftar Kontak:")
    for i, (nama, nomor) in enumerate(kontak, start=1):
        print(f"{i}. {nama} - {nomor}")
    print()  # Tambahkan baris kosong untuk pemisah
    
def cari_kontak(kontak):
    if not kontak:
        print("\nDaftar kosong.")
        return
    nama_cari = input("Masukkan nama yang dicari: ").strip().lower()
    hasil = [f"{i+1}. {nama} - {nomor}" for i, (nama, nomor) in enumerate(kontak) if nama.lower() == nama_cari]
    if hasil:
        print("\nHasil pencarian:")
        print("\n".join(hasil))
    else:
        print("Kontak tidak ditemukan.")
        
def edit_kontak(kontak):
    if not kontak:
        print("\nDaftar kosong.")
        return
    tampilkan_kontak(kontak)
    try:
        index = int(input("\nNomor kontak yang akan diedit: ")) - 1
        if 0 <= index < len(kontak):
            nama_baru = input("Masukkan nama baru: ").strip()
            nomor_baru = input("Masukkan nomor baru: ").strip()
            if not nama_baru or not nomor_baru:
                print("Nama dan nomor tidak boleh kosong.")
                return
            kontak[index] = (nama_baru, nomor_baru)
            print(f"Kontak telah diperbarui: {nama_baru} - {nomor_baru}")
        else:
            print("Nomor kontak tidak valid.")
    except (ValueError, IndexError):
        print("Input tidak valid.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        print("Program dihentikan.")
