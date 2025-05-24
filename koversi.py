print('Kalkulator Konversi Fahrenheit & Celsius')


while True:
    try:
        suhu = float(input("Masukkan suhu: "))
        satuan = input("Masukkan satuan (F untuk Fahrenheit, C untuk Celsius): ").strip().upper()
        
        if satuan == 'F':
            celsius = (suhu - 32) * 5.0/9.0
            print(f"{suhu} Fahrenheit = {round(celsius, 2)} Celsius")
        elif satuan == 'C':
            fahrenheit = (suhu * 9.0/5.0) + 32
            print(f"{suhu} Celsius = {round(fahrenheit, 2)} Fahrenheit")
        else:
            print("Satuan tidak valid! Gunakan 'F' untuk Fahrenheit atau 'C' untuk Celsius.")
        
        break  # Keluar dari loop setelah konversi berhasil
    except ValueError:
        print("Input harus berupa angka!")