daftar_data = []

while True:
    print("\n=== Input Data Mahasiswa ===")
    nama = input("Nama: ")
    nim = int(input("NIM: "))
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    # Hitung nilai akhir sesuai ketentuan
    nilai_akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)

    # Simpan ke list
    data = {
        "nama": nama,
        "nim": nim,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "nilai_akhir": round(nilai_akhir, 2)
    }

    daftar_data.append(data)

    # Apakah ingin menambah data lagi?
    lanjut = input("\nTambah data lagi? (y/t): ").lower()
    if lanjut == "t":
        break

# ==================== OUTPUT TABEL ====================
print("\n==================== DAFTAR NILAI MAHASISWA ====================")
print("No | Nama             | NIM         | Tugas | UTS   | UAS   | Akhir")
print("---------------------------------------------------------------------")

for i, d in enumerate(daftar_data, 1):
    print(f"{i:<3}| {d['nama']:<16}| {d['nim']:<11}| {d['tugas']:<6}| {d['uts']:<6}| {d['uas']:<6}| {d['nilai_akhir']:<6}")
