README - Program Input Data Mahasiswa

## Deskripsi Program

Program ini digunakan untuk menambahkan data mahasiswa ke dalam sebuah list menggunakan perulangan.
Setiap mahasiswa memiliki data berupa Nama, NIM, Nilai Tugas, Nilai UTS, dan Nilai UAS.

Program akan terus meminta input data selama pengguna memilih untuk menambah data (jawaban "y").
Jika pengguna menjawab "t", maka program berhenti dan menampilkan daftar data mahasiswa dalam bentuk tabel.

## Aturan Perhitungan Nilai Akhir

Nilai akhir dihitung berdasarkan tiga komponen:

- Tugas: 30%
- UTS: 35%
- UAS: 35%

Rumus:

```
nilai_akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
```

## Flowchart Program

1. Mulai
2. Inisialisasi list `daftar_data`
3. Input nama, NIM, nilai tugas, uts, uas
4. Hitung nilai akhir
5. Simpan data ke list
6. Tanya "Tambah data lagi? (y/t)"
7. Jika "y", ulangi ke langkah 3
8. Jika "t", tampilkan tabel data
9. Selesai

## Cara Menjalankan Program

1. Pastikan Python sudah terinstal.
2. Simpan script `.py` yang diberikan.
3. Jalankan program dengan perintah:

```
python namafile.py
```

4. Masukkan data sesuai instruksi.
5. Lihat hasil tabel saat memilih "t".
