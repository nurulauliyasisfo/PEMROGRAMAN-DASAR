import array

# Membuat array berisi angka integer
angka = array.array('i', [10, 20, 30, 40, 50])

# Menampilkan isi array
print("isi.array:",angka )

# Mengakses elemen
print("elemen pertama:", angka[0])

# Menambah elemen
angka.append(60)
print("setelah ditambah:", angka)

# Menghapus elemen
angka.remove(30)
print("setelah dihapus:", angka)