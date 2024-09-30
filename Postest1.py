print("=== Selamat datang Di Perusahaan Selalu Menyala ===")

#input nama dan nim
print("Masukan nama dan nim dengan benar !")
nama = input("Masukkan nama anda : ")
nim = input("Masukkan NIM anda : ")

print("============================================")
#input jam kerja dan tarif kerja
jam_kerja = float(input('Masukan jam kerja: '))
tarif_kerja = float(input('Masukan tarif kerja: Rp. '))
#total gaji
total_gaji = jam_kerja * tarif_kerja
print("============================================")

print("==================================================")
if jam_kerja > 160:
    bonus = 0.1 * total_gaji
    total_gaji += bonus
    print(f"bonus tambahan 10 % :{bonus}")
    print(f"total gaji yang diserahkan: {total_gaji}")

elif jam_kerja < 160:
    print(f"total gaji yang di serahkan: Rp.{total_gaji}")
print("==================================================")
    
ulang = "ya"

while(ulang == "ya"):
    ulang = input("Apakah anda menghitung gaji lagi (ya/tidak): ")
    if (ulang == "ya"):
        print("=== Selamat datang Di Perusahaan Selalu Menyala ===")

        #input nama dan nim
        nama = input("Masukkan nama anda : ")
        nim = input("Masukkan NIM anda : ")

        print("============================================")
        #input jam kerja dan tarif kerja
        jam_kerja = int(input("Masukan jam kerja: "))
        tarif_kerja = int(input("Masukan tarif : Rp. "))
        #total gaji
        total_gaji = jam_kerja * tarif_kerja
        print("============================================")

        if jam_kerja > 160:
            bonus = 0.1 * total_gaji
            total_gaji += bonus
            print(f"bonus tambahan: {bonus}")
            print(f"total gaji yang diserahkan: {total_gaji}")
        
        elif jam_kerja < 160:
            print(f"total gaji yang di serahkan: {total_gaji}")
        print("==================================================")
        
    elif (ulang == "tidak"):
        print("Terima kasih atas kerja sama anda! ")
        break




