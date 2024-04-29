import random   #import angka random

num = random.randint(1,10)  #random.radint(1,10) memberikan angka random dari 1-10 dengan variabel num
guess = int(input("Tebak Angka diantara 1 sampai 10 : "))   #mendapat input user dengan tipe data int disimpan di variabel guess

while guess != num: #melakukan looping jika kondisi while terpenuhi yaitu guess tidak sama dengan num
    if guess > num: #jika guess lebih besar dari num maka print dibawahnya akan tampil
        print("Tebakan terlalu besar")
    elif guess < num:   #jika guess lebih kecil dari num maka pirnt dibawahnya akan tampil
        print("Tebakan terlalu kecil")
    guess = int(input("Tebak lagi : ")) #jika while belum terpenuhi maka input user ini akan tampil lagi

print ("Tebakan anda benar")    # jika kondisi while tidak terpenuhi yaitu  guess sama dengan num maka print ini akan muncul