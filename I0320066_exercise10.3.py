#Exercise10.3
#Cara Menulis File di Python

#menulis dengan mode "w"

print("Selamat datang di Program Biodata")
print("=================================")

#ambil input dari user
nama = input("Nama: ")
umur = input("Umur: ")
alamat = input("Alamat: ")

#format teks
teks = "Nama: {}\nUmur: {}\nAlamat: {}".format(nama, umur, alamat)

#buka file untuk ditulis
file_bio = open("biodata.txt", "w")

#tulis teks ke file
file_bio.write(teks)

#tutup file
file_bio.close()
