def Luas_persegi(sisi):
  return sisi ** 2
  
def Luas_Persegi_Panjang(panjang, lebar):
  return panjang * lebar
  
def Luas_Segitiga(alas, tinggi):
  return 0.5 * alas * tinggi
  
def Luas_Lingkaran(jari_jari):
  import math
  return math.pi * jari_jari ** 2
  
def main():
  print("Dengan Siapa aku bisa memanggilmu ? 😏")
  pengunjung = input("Tulis namamu: ")
  
  print()
  
  print(f"Oh, Selamat datang ya {pengunjung} 👋")
  print("Ini adalah Program Keduaku, Cimus😎.  Program tentang Penghitung Luas. ")
  
  print()
  
  print(f"Baiklah {pengunjung}")
  print("Cobain programku kali ini 👇")
  
  print()
  
  print("pilih luas bangun yang anda butuhkan:")
  print("1) Luas Persegi")
  print("2) Luas Persegi Panjang")
  print("3) Luas Segitiga")
  print("4) Luas Lingkaran")
  
  pilih = int(input("Pilih salah satu opsi (1/2/3/4): "))
  
  if pilih == 1:
    sisi = int(input("Masukkan sisinya: "))
    print(f"Luas persegi = {Luas_persegi(sisi)}")
    print("Ok! See You🎉")
    
  elif pilih == 2:
    panjang = int(input("Masukkan Panjangnya: "))
    lebar = int(input("Masukkan Lebarnya: "))
    print(f"Luas Persegi Panjangnya = {Luas_Persegi_Panjang(panjang, lebar)}")
    print("Ok! See You🎉")
    
  elif pilih == 3:
    alas = int(input("Masukkan Alasnya: "))
    tinggi = int(input("Masukkan Tingginya: "))
    print(f"Luas Segitiganya = {Luas_Segitiga(alas, tinggi)}")
    print("Ok! See You🎉")
    
  elif pilih == 4:
    jari_jari = int(input("Masukkan Jari-Jarinya: "))
    print(f"Luas Lingkarannya = {Luas_Lingkaran(jari_jari):.2f}")
    print("Ok! See You🎉")

if __name__ == "__main__":
  main()




