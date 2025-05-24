print("=== Kalkulator BMI ===")


def hitung_bmi():  
    print("=== Kalkulator BMI ===")  
    try:  
        berat = float(input("Masukkan berat (kg): "))  
        tinggicm = float(input("Masukkan tinggi (cm): "))  
        tinggi = tinggicm / 100  # Konversi cm ke m
        if berat <= 0 or tinggi <= 0:  
            print("Error: Berat/tinggi harus > 0!")  
            return  
       
        bmi = berat / (tinggi ** 2)  
        kategori = ""  

        if bmi < 18.5:
            kategori = "Kurus"
        elif 18.5 <= bmi < 25:
            kategori = "Normal"
        elif 25 <= bmi < 30:
            kategori = "Gemuk"
        else:
            kategori = "Obesitas"

        print(f"\nBMI Anda: {bmi:.1f} → Kategori: {kategori}")  
    except ValueError:  
        print("Input harus berupa angka!")  

# Tambahkan di akhir untuk loop program
while True:
    hitung_bmi()
    ulangi = input("\nHitung lagi? (y/n): ").lower()
    if ulangi != 'y':
        print("Terima kasih!")
        break
      
