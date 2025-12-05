# Membuat dictinary
mahasiswa = {
    "nama": "Nurul Auliya",
    "nim": "D0425324",
    "jurusan": "Sistem Informasi"
}

# Mengakses nilai
print("nama:", mahasiswa["nama"])

# Menambah data baru
mahasiswa["angkatan"] = 2025

# Mengubah data
mahasiswa["jurusan"] = "Sistem informasi"

# Menghapus data
del mahasiswa["nim"]

# Menampilkan seluruh isi dictionary
print("data mahasiswa:", mahasiswa)