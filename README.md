# Pertemuan 7
## Kondisi dan Perulangan

## Profil
| Variable | Isi |
| -------- | --- |
| **Nama** | Reza Riyaldi Irawan |
| **NIM** | 312010284 |
| **Kelas** | TI.20.A.2 |
| **Mata Kuliah** | Bahasa Pemrograman |

## Daftar Isi
* [Pertemuan 7](https://github.com/RezaRiyaldi/Pertemuan7#pertemuan-7)
    * [Praktikum 1](https://github.com/RezaRiyaldi/Pertemuan7#praktikum-1) | [direktori](https://github.com/RezaRiyaldi/Pertemuan7/tree/master/Praktikum%201)
        - [Latihan 1](https://github.com/RezaRiyaldi/Pertemuan7#latihan-1) | [Source Code](https://github.com/RezaRiyaldi/Pertemuan7/blob/master/Praktikum%201/Latihan1.py)
        - [Latihan 2](https://github.com/RezaRiyaldi/Pertemuan7#latihan-2) | [Source Code](https://github.com/RezaRiyaldi/Pertemuan7/blob/master/Praktikum%201/Latihan2.py)
    * [Praktikum 2](https://github.com/RezaRiyaldi/Pertemuan7#praktikum-2) | [direktori](https://github.com/RezaRiyaldi/Pertemuan7/tree/master/Praktikum%202)
        - [Latihan 1](https://github.com/RezaRiyaldi/Pertemuan7#latihan-1-1) | [Source Code](https://github.com/RezaRiyaldi/Pertemuan7/blob/master/Praktikum%202/latihan1.py)
        - [Program 1](https://github.com/RezaRiyaldi/Pertemuan7#program-1) | [Source Code](https://github.com/RezaRiyaldi/Pertemuan7/blob/master/Praktikum%202/program1.py)

## Praktikum 1
### Latihan 1 
* Saya diberikan tugas untuk membuat program perulangan bersarang/bertingkat (nested for) yang menghasilkan output berikut

![output 1](https://github.com/RezaRiyaldi/Pertemuan7/blob/master/Praktikum%201/gambar/tugas%201.PNG)

Maka program yang saya buat sebagai berikut atau bisa dilihat di [Source Code](https://github.com/RezaRiyaldi/Pertemuan7/blob/master/Praktikum%201/Latihan1.py)

```python
baris = 10
kolom = baris

for bar in range(baris):
    for col in range(kolom):
        tab = bar+col
        print("{0:>5}".format(tab), end='')
    print()
```

Penjelasan

1. Pendeklarasian variable
```python
baris = 10
kolom = baris
```

2. Untuk perulangan baris dan kolom menggunakan `nested for`
```python
for bar in range(baris):
    for col in range(kolom):
        tab = bar+col        
```
3. Untuk menampikan hasil dari perulangan
     * Agar terlihat rapih menggunakan `format string` rata ke kanan sebanyak 5 karakter
     * Agar tidak membuat baris baru menggunakan `end=''` (baris)
     * Penggunaan `print()` untuk membuat baris baru (kolom)
```python
  print("{0:>5}".format(tab), end='')
print()    
```

Maka program yang di hasil seperti berikut

![tampil 1](https://github.com/RezaRiyaldi/Pertemuan7/blob/master/Praktikum%201/gambar/tampil%201.PNG)

Kembali ke [Daftar isi](https://github.com/RezaRiyaldi/Pertemuan7#daftar-isi)

### Latihan 2

Konsep program :
1. Menampilkan n bilangan acak yang lebih kecil dari 0.5.
2. nilai n diisi pada saat runtime

Program Menampilkan n Bilangan Acak Yang Lebih Kecil Dari 0.5
![latihan1](https://github.com/RezaRiyaldi/Pertemuan7/blob/master/Praktikum%202/gambar/latihan2.png)

Penjelasan

1. Mengimport module `random` untuk membuat bilangan acak
```python
import random
```

2. Untuk menentukan jumlah input yang diinginkan dan dikonversi ke dalam bilangan bulat (integer) yang dimasukan ke variable `jum`
```python
jum = int( input("Masukan nilai n : "))
```

3. Untuk pengulangan range yang diinputkan oleh variable `jum`
```python
for i in range(jum):
```

4. Untuk menampilkan urutan data sesuai jumlah inputan dengan hasil di bawah 0.5
```python
angkaDec = random.uniform(0, 0.5)
    print("Data ke", i, " = ", angkaDec)
```
Program yang saya buat bisa dilihat di [Source Code](https://github.com/RezaRiyaldi/Pertemuan7/blob/master/Praktikum%201/Latihan2.py)

Kembali ke [Daftar isi](https://github.com/RezaRiyaldi/Pertemuan7#daftar-isi)

## Praktikum 2

### Latihan 1
Konsep program : 
1. Membuat program untuk menampilkan bilangan terbesar dari n buah data yang diinputkan.
2. Ketika memasukan angka 0 program akan berhenti.

Program Sederhana Untuk Menampilkan bilangan Terbesar dari n buah data yang dimasukkan

![latihan1](https://github.com/RezaRiyaldi/Pertemuan7/blob/master/Praktikum%202/gambar/latihan1.png)

Penjelasan program

1. Membuat header `print(40*"=")` untuk menampilkan "=" sebanyak 40, begitupun yang `print(5*"=")` untuk menampilkan "=" sebanyak 5
```python
print(40*"=")
print(5*"=","Menentukan bilangan terbesar", 5*"=")
print(40*"=")
```
2. Deklarasi variable
```python
max = 0
```
3. Untuk perulangan hingga waktu yang tidak di tentukan atau selamanya
```pyhton
while True: 
```
4. Untuk menentukan jumlah input yang diinginkan dan dikonversi ke dalam bilangan bulat (integer) yang dimasukan ke variable `a`
```python
 a = int(input("Masukan bilangan : "))
```
5. Jika max kurang dari a maka max = a maka variable max = a atau nilai yang diinputkan
```pyhton
if max < a:
max = a
```
6. Jika a = 0 maka program akan berhenti dengan syarat break yang terpenuhi
```python
if a == 0: 
break 
```
7.  Menampilkan Bilangan Terbesar
```python
print ("Bilangan Terbesar Adalah : ", max) 
```
Program yang saya buat bisa dilihat di [Source Code](https://github.com/RezaRiyaldi/Pertemuan7/blob/master/Praktikum%202/latihan1.py)

Kembali ke [Daftar isi](https://github.com/RezaRiyaldi/Pertemuan7#daftar-isi)

### Program 1

Konsep program : 
1. Seorang pengusaha menginvestasikan uangnya untuk memulai usahanya dengan
modal awal 100 juta, pada bulan pertama dan kedua belum mendapatkan laba. pada
bulan ketiga baru mulai mendapatkan laba sebesar 1% dan pada bulan ke 5,
pendapatan meningkat 5%, selanjutnya pada bulan ke 8 mengalami penurunan
keuntungan sebesar 2%, sehingga laba menjadi 3%. Hitung total keuntungan selama 8
bulan berjalan usahanya.

Program Program Sederhana Menghitung Total Keuntungan Selama 8 Bulan

![latihan1](https://github.com/RezaRiyaldi/Pertemuan7/blob/master/Praktikum%202/gambar/program1.png)

Penjelasan program
1. Deklarasi variable
```python
modal = 100000000
laba = [modal * 0, modal* 0, modal * 1/100, modal * 1/100, modal * 5/100, modal * 5/100, modal * 5/100, modal * 3/100]
bulan = 0
sum = 0
```
2. Dari variable `laba` terdapat list `modal * 0, modal* 0, modal * 1/100, modal * 1/100, modal * 5/100, modal * 5/100, modal * 5/100, modal * 3/100` yang bermaksud dari bulan pertama - akhir
3. Membuat header `print(39*"=")` untuk menampilkan "=" sebanyak 39, begitupun yang `print(5*"=")` untuk menampilkan "=" sebanyak 5
```python
print(39*"=")
print(5*"=","Menentukan bilangan terbesar", 5*"=")
print(39*"=")
```
4. Menampilkan modal awal menggunakan `f string` pada `{modal}` atau variable modal
```python
print(f"Modal awal pengusaha {modal}")
```
5. Melakukan perulangan yang di masukan kedalam variable `i` dari variable `laba`
```python
for i in laba:
```
6. Variable `i` akan ditambahkan dengan variable `sum`, setiap melakukan perulangan `sum` + `i` sampai program selesai
```python
sum = sum + i
```
7. Untuk menentukan bulan
```python
bulan += 1
```
8. Menampilkan program dengan `f string`
```python
print(f"Laba pada bulan ke - {bulan}, mendapat laba = {i}")
```
9. Hasil akhir
```python
print(f"Keuntungan yang didapat selama {bulan} bulan = {sum}")
```
Program yang saya buat bisa dilihat di [Source Code](https://github.com/RezaRiyaldi/Pertemuan7/blob/master/Praktikum%202/program1.py)

Kembali ke [Daftar isi](https://github.com/RezaRiyaldi/Pertemuan7#daftar-isi)


