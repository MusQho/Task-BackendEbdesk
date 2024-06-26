#INTI PROGRAM
def Inti_program():
  
#SEGITIGA SIKU SIKU
  
    def segitiga_siku_kiribawah(tinggi):
        print("RESULT")
        print()
        for q in range(1, tinggi+1):
            print(q * " *")
        print()
        print("DETAILS")
        print("=======")
        print("Model : SEGITIGA SIKU SIKU")
        print("Sudut Siku  : KIRI BAWAH")
        print(f"Jumlah Bintang : {tinggi * (tinggi+1) // 2}")

    def segitiga_siku_kiriatas(tinggi):
        print("RESULT")
        print()
        for w in range(1, tinggi+1):
            print((tinggi-w+1) * " *")
        print()
        print("DETAILS")
        print("=======")
        print("Model : SEGITIGA SIKU SIKU")
        print("Sudut Siku  : KIRI ATAS")
        print(f"Jumlah Bintang : {tinggi * (tinggi+1) // 2}")

    def segitiga_siku_kananbawah(tinggi):
        print("RESULT")
        print()
        for r in range(1, tinggi+1):
            print(((tinggi-r+1) * "  ") + (r * " *"))
        print()
        print("DETAILS")
        print("=======")
        print("Model : SEGITIGA SIKU SIKU")
        print("Sudut Siku  : KANAN BAWAH")
        print(f"Jumlah Bintang : {tinggi * (tinggi+1) // 2}")

    def segitiga_siku_kananatas(tinggi):
        print("RESULT")
        print()
        for e in range(1, tinggi+1):
            print((e * "  ") + ((tinggi-e+1) * " *"))
        print()
        print("DETAILS")
        print("=======")
        print("Model : SEGITIGA SIKU SIKU")
        print("Sudut Siku  : KANAN ATAS")
        print(f"Jumlah Bintang : {tinggi * (tinggi+1) // 2}")

#SEGITIGA SAMA KAKI

    def segitiga_atas(tinggi):
        print("RESULT")
        print()
        for t in range(1, tinggi+1):
            print(((tinggi-t+1) * "  ") + (t * " *") + ((t-1)* " *"))
        print()
        print("DETAILS")
        print("=======")
        print("Model : SEGITIGA SAMA KAKI")
        print("Arah  : KEATAS")
        print(f"Jumlah Bintang : {(tinggi * 2) * (tinggi) // 2}")

    def segitiga_bawah(tinggi):
        print("RESULT")
        print()
        for y in range(1, tinggi+1):
            print((y * "  ") + ((tinggi-y+1) * " *") + ((tinggi-y) * " *"))
        print()
        print("DETAILS")
        print("=======")
        print("Model : SEGITIGA SAMA KAKI")
        print("Arah  : KEBAWAH")
        print(f"Jumlah Bintang : {(tinggi * 2) * (tinggi) // 2}")

    def segitiga_kanan(tinggi):
        print("RESULT")
        print()
        for u in range(1, tinggi):
            print(u * " *")
        for i in range(1, tinggi+1):
            print((tinggi-i+1) * " *")
        print()
        print("DETAILS")
        print("=======")
        print("Model : SEGITIGA SAMA KAKI")
        print("Arah  : KEKANAN")
        print(f"Jumlah Bintang : {(tinggi * 2) * (tinggi) // 2}")

    def segitiga_kiri(tinggi):
        print("RESULT")
        print()
        for o in range(1, tinggi):
            print(((tinggi-o+1) * "  ") + (o * " *"))
        for p in range(1, tinggi+1):
            print((p * "  ") + ((tinggi-p+1) * " *"))
        print()
        print("DETAILS")
        print("=======")
        print("Model : SEGITIGA SAMA KAKI")
        print("Arah  : KEKIRI")
        print(f"Jumlah Bintang : {(tinggi * 2) * (tinggi) // 2}")

#HASIL DARI USER MEMILIH SEGITIGA SIKU SIKU

    def segitiga_siku(tinggi, sudut):
        if sudut == "kiri bawah":
              segitiga_siku_kiribawah(tinggi)
        elif sudut == "kiri atas":
              segitiga_siku_kiriatas(tinggi)
        elif sudut == "kanan bawah":
              segitiga_siku_kananbawah(tinggi)
        elif sudut == "kanan atas":
              segitiga_siku_kananatas(tinggi)
        else:
              print("PILIHAN TIDAK VALID")
              print("ATAU")
              print("PILIH DENGAN HURUF KECIL SEMUA")
  
#HASIL DARI USER MEMILIH SEGITIGA SAMA KAKI
  
    def segitiga_sama_kaki(tinggi, arah):
        if arah == "keatas":
            segitiga_atas(tinggi)
        elif arah == "kebawah":
            segitiga_bawah(tinggi)
        elif arah == "kekanan":
            segitiga_kanan(tinggi)
        elif arah == "kekiri":
            segitiga_kiri(tinggi)
        else:
            print("PILIHAN TIDAK VALID")
            print("ATAU")
            print("PILIH DENGAN HURUF KECIL SEMUA")

#PENGEKSEKUSIAN DARI PERINTAH USER
  
    print("===== BUILDER TRIANGLE CHAIR =====")
    print("By:MASMUS")

    input()

    print()

    print("PILIHLAH DENGAN HURUF KECIL")
    print()
    print("1. segitiga siku siku")
    print("2. segitiga sama kaki")

    print()

    pilihan = input("SILAHKAN PILIH BENTUK SEGITIGANYA : ")

    print()

#USER MEMILIH SEGITIGA SIKU SIKU

    if pilihan == "segitiga siku siku":
            tinggi = int(input("TENTUKAN TINGGI BARIS STAIRNYA : "))
            print()
            print("1. kiri bawah")
            print("2. kiri atas")
            print("3. kanan bawah")
            print("4. kanan atas")
            print()
            sudut = input("PILIH TITIK SUDUT SIKU STAIRNYA : ")
            print()
            segitiga_siku(tinggi, sudut)

#USER MEMILIH SEGITIGA SAMA KAKI
        
    elif pilihan == "segitiga sama kaki":
            tinggi = int(input("PILIH TINGGI BARIS STAIRNYA : "))
            print()
            print("1. Keatas")
            print("2. Kebawah")
            print("3  Kekanan")
            print("4. Kekiri")
            print()
            arah = input("PILIH ARAH SEGITIGANYA : ")
            print()
            segitiga_sama_kaki(tinggi, arah)
        
    else:
            print("PILIHAN TIDAK VALID")
            print("ATAU")
            print("PILIH DENGAN HURUF KECIL SEMUA")
            
    print()
  
#MENGULANGI PROGRAM
  
    while True:
      ulang = input("APAKAH ANDA INGIN MENGULANGI PROGRAM? (y/n): ").lower()
      if ulang == 'y':
        v = 10
        for g in range(1, v+1):
          print(v * " ")
        Inti_program()
        break
      elif ulang == 'n':
        print()
        print("TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI !")
        break
      
Inti_program()

print()
