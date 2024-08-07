print("\nPENDATAAN TUJUAN PEMBERANGKATAN KERETA")
print(" ===========","By: MusQho","=============")
input()

list_kerja = []
while True:
    print("\n\n","="*5,"MASUKKAN DATA","="*5)
    nama = input("ISIKAN NAMA ANDA\t: ") 
    kerja = input("TUJUAN AKHIR ANDA\t: ")

    total = [nama,kerja]
    list_kerja.append(total)

    print("\n","="*5,"DATA TUNJUAN PENUMPANG","="*5)
    for index,gua in enumerate(list_kerja):
        print(f"{index+1}    |   {gua[0]}    |   {gua[1]}")

    berhenti = input("\nAPAKAH ANDA INGIN MENAMBAHKAN DATANYA? (y/n): ")
    if berhenti == "n":
        break

print("="*5,"PROGRAM DISELESAIKAN!!","="*5)