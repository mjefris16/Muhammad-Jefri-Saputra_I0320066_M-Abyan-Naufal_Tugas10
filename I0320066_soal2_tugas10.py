print("Selamat datang di Program Biodata")
print("=================================")

#ambil input dari user
nama = input("Nama: ")
umur = input("Umur: ")
kelamin = input("Jenis kelamin: ")
alamat = input("Alamat: ")

#format teks
teks = "Nama: {}\nUmur: {}\nAlamat: {}\nJenis kelamin: {}".format(nama, umur, alamat, kelamin)

#buka file untuk ditulis
file_bio = open("file.txt", "w")

#tulis teks ke file
file_bio.write(teks)

#tutup file
file_bio.close()
