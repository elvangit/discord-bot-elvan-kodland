import random

sandi =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
panjang = int(input("Berapa panjang karakter untuk kata sandi   "))
hasil = ""

for i in range(panjang):
    hasil += random.choice(sandi)
print("Kata sandi yang dihasilkan adalah",hasil)    

