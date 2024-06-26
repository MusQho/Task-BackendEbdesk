def tambah(x, y):
  return x + y
  
def kurang(x, y):
  return x - y
  
def kali(x, y):
  return x * y
  
def bagi(x, y):
  if y == 0:
    print("Tidak terdefinisi")
  else:
    return x / y

print("Hey kamu, boleh dong kenalan.😁")
pengunjung = (input("Tulis Namamu: "))

print()

print(f"Baiklah salam kenal ya {pengunjung}")
print("Saya Cimus, editor program ini😎")

print()

print(f"Ey {pengunjung}👋,") 
print("Coba dong jalankan program berikut ini 👇")

print()

print("Pilih salah satu opsi: ")
print("1. pertambahan")
print("2. pengurangan")
print("3. perkalian")
print("4. pembagian")
opsi = (input("pilihlah opsi (1/2/3/4): "))

print()

angka1 = float(input("Pilih angka pertama: "))
angka2 = float(input("Pilih angka kedua: "))

print()

if opsi == '1':
  print(f"Hasil Perjumlahan Dari {angka1} + {angka2} = ", tambah(angka1, angka2), "👍") 
  
elif opsi == '2':
  print(f"Hasil Pengurangan Dari {angka1} - {angka2} = ", kurang(angka1, angka2), "👍")
  
elif opsi == '3':
  print(f"Hasil Perkalian Dari {angka1} × {angka2} = ", kali(angka1, angka2), "👍")

elif opsi == '4':
  print(f"Hasil Pembagian Dari {angka1} / {angka2} = ", bagi(angka1, angka2), "👍")
  
else:
  print(f"Maaf {pengunjung},")
  print("Tolong masukkan opsi yang sesuai (1/2/3/4) 🙏")