print("Kalkulator Gaess")

while True:
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        
        if angka1 == 0 and angka2 == 0:
            print("Error: Kedua angka tidak boleh 0 sekaligus!")
            continue 
        elif angka1 == 0:
            print("Error: Angka pertama tidak boleh 0!")
            continue
        elif angka2 == 0:
            print("Error: Angka kedua tidak boleh 0 untuk operasi pembagian!")
            continue
            
        
        break
    except ValueError:
        print("Input harus berupa angka!")
tambah = angka1 + angka2  
kurang = angka1 - angka2  
kali = angka1 * angka2  
bagi = angka1 / angka2  

print(f'''Hasil:  
- Tambah: {round(tambah, 2)}  
- Kurang: {round(kurang, 2)}  
- Kali: {round(kali, 2)}  
- Bagi: {round(bagi, 2)}
''')
