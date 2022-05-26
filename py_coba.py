print("Paragraf pertama")

nama = input("Masukan Nama : ")
umur = input("Masukan umur")
hobi = input("Masukan hobi anda : ")
pekerjaan = input("Masukan pekerjaan : ")

print(f"Nama anda {nama} dengan usia {umur} pekerjaan anda {pekerjaan} hobby anda {hobi}")

i = 0
while(i<5):
	if i % 2 == 0:
		print(i, ": anka genap")
	else:
		print(i, ": angka ganjil")
	i += 1


