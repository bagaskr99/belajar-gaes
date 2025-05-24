from decimal import Decimal

print('Daftar Belanja Mingguan')

barang = []

def main():
    while True:
        print('\nMenu:')
        print('1. Tambah Barang')
        print('2. Tampilkan Barang')
        print('3. Hapus Barang')
        print('4. Keluar')
        
        pilihan = input('Pilih menu (1-4): ')
        if not pilihan.isdigit() or int(pilihan) not in {1, 2, 3, 4}:
            print('Input tidak valid. Silakan masukkan angka 1-4.')
            continue
        
        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            tampilkan_barang()
        elif pilihan == '3':
            hapus_barang()
        elif pilihan == '4':
            print('Terima kasih!')
            break

def tambah_barang():
    print('\nTambah Barang (ketik "SELESAI" untuk kembali)')
    while True:
        nama = input("Nama barang: ").strip()
        if nama.upper() == "SELESAI":
            break
        try:
            harga = Decimal(input(f"Harga {nama}: "))
            if harga < 0:
                print("Harga tidak boleh negatif.")
                continue
            barang.append((nama, harga))
            print(f"{nama} ditambahkan!")
        except Exception as e:
            print(f"Error: {e}")


def hapus_barang():
    if not barang:
        print("\nDaftar kosong.")
        return
    tampilkan_barang()
    try:
        index = int(input("\nNomor barang yang dihapus: ")) - 1
        nama, harga = barang.pop(index)
        print(f"{nama} dihapus!")
        tampilkan_barang()
    except (ValueError, IndexError):
        print("Input tidak valid.")

def tampilkan_barang():
    if not barang:
        print("\nDaftar kosong.")
        return
    print("\nDaftar Belanja:")
    total = Decimal('0.00')
    for i, (nama, harga) in enumerate(barang, start=1):
        print(f"{i}. {nama}: Rp{harga:.2f}")
        total += harga
    print(f"Total: Rp{total:.2f}")
if __name__ == "__main__":
    while True:
        try:
            main()
            break
        except Exception as e:
            print(f"Error: {e}")