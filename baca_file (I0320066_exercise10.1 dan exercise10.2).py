#Exercise10.1
#Membaca File per Baris

#buka file
file_puisi = open("puisi.txt","r")

#baca isi file
print(file_puisi.readlines())

#tutup file
file_puisi.close()

"""""

#Exercise10.2
#Membaca Semua teks dalam file

#buka file
file_puisi = open("puisi.txt","r")

#baca isi file
puisi = file_puisi.read()

#cetak isi file
print (puisi)

#tutup file
file_puisi.close()

"""