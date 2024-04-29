# Contoh 1
inpt_user = int(input("Masukan Tinggi Segitga Contoh 1: "))
jumlah_baris = 0

while jumlah_baris < inpt_user: # jika nilai variabel jumlah_baris kurang dari inpt_user maka looping akan berjalan
    jumlah_baris += 1 # setiap looping dilakukan nilai variabel jumlah_baris akan bertambah 1
    print("*"*jumlah_baris) # jumlah "*" yang dicetak akan sesusai dengan nilai variabel jumlah_baris
print("Akhir Program \n")

# Contoh 1.2 (Break)
inpt_user = int(input("Masukan Tinggi Segitga Contoh 2 : "))
jumlah_baris = 0
while True:  # perulangan selama True, sehingga tidak terhenti sampai diberikan kondisi Break
    jumlah_baris += 1 # setiap looping dilakukan nilai variabel jumlah_baris akan bertambah 1
    if jumlah_baris > inpt_user: # jika nilai variabel jumlah_baris lebiih dari inpt_user maka looping akan berhenti
        break
    print("*" * jumlah_baris) # jumlah "*" yang dicetak akan sesusai dengan nilai variabel jumlah_baris
print("Akhir Program \n")

# Contoh 1.3 hanya ganjil (Continue)
inpt_user = int(input("Masukan Tinggi Segitiga Contoh 3 : "))
jumlah_baris = 0
while inpt_user > jumlah_baris:
    jumlah_baris += 1
    if jumlah_baris % 2 == 0: # jika jumlah_baris sisa baginya 0, maka looping akan dimulai dari awal
        continue
    print("*"*jumlah_baris)
print("Akhir Program \n")

# Contoh 1.4 hanya genap (Continue)
inpt_user = int(input("Masukan Tinggi Segitiga Contoh 4 : "))
jumlah_baris = 0
while inpt_user > jumlah_baris: # jika jumlah_baris sisa baginya tidak sama dengan 0, maka looping akan dimulai dari awal
    jumlah_baris += 1
    if jumlah_baris % 2 != 0:
        continue
    print("*"*jumlah_baris)
print("Akhir Program \n")

#contoh 2
inpt_user = int(input("Masukan Tinggi Segitiga Contoh 5 : "))
jumlah_baris = 0

while jumlah_baris < inpt_user:
    jumlah_baris += 1
    spasi = jumlah_baris - inpt_user
    spasi -= 1
    print(" "*spasi + "*"* jumlah_baris )