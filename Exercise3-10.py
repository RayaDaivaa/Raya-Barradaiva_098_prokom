cities = ["Jakarta", "Surakarta", "Bandung", "Yogyakarta"]

# Mengakses elemen list
print(cities[0])

# Mengubah elemen list
cities[0] = "Semarang"

# Menambahkan elemen
cities.append("Surabaya")
cities.insert(1, "Malang")

# Menghapus elemen
del cities[1]

# Menggunakan pop()
removed_city = cities.pop()
print(removed_city)

# Menggunakan remove()
cities.remove("Bandung")

# Mengurutkan list
cities.sort()
print(cities)

# Mengurutkan sementara
print(sorted(cities))

# Membalik urutan list
cities.reverse()
print(cities)

# Menghitung jumlah elemen
print(len(cities))