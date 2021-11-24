# python-compiler-tbfo
> Tugas Besar IF2124 Teori Bahasa Formal dan Otomata - Compiler Bahasa Python Semester I 2021/2022

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Contact](#contact)

## General Information
<p> Compiler bahasa Python untuk statement-statement dan sintaks-sintaks bawaan Python. 
 Menggunakan konsep FA, CFG, CNF, dan Algoritma CYK untuk mengevaluasi sintaks program. </p>


## Technologies Used
- Program ini 100% ditulis dalam bahasa Python 


## Features
<p> Program menerima inputan file Python yang berisikan kode program, kemudian program dapat mengevaluasi kebenaran sintaks kode program dengan memanfaatkan konsep FA, CFG, CNF, dan Algoritma CYK. Program menampilkan pesan pada layar apakah program lulus compile atau tidak. Jika tidak lulus compile, program akan menampilkan juga lokasi baris yang mengandung kesalahan sintaks pertama kali. Program juga dapat menampilkan progress jalannya algoritma CYK dan waktu proses evaluasi </p>


## Setup
- Clone repository ini dan unzip sehingga akan terbentuk folder `python-compiler-tbfo`
- Pastikan sudah menginstall Python versi terbaru pada sistem operasi yang digunakan
- Akses folder `python-compiler-tbfo`, masukkan file program Python `.py` yang ingin dievaluasi sintaksnya ke folder `input` 
- Buka program Terminal yang sesuai dengan sistem operasi yang digunakan (dapat menggunakan `cmd` untuk pengguna OS Windows)
- Program dapat dijalankan dengan perintah 
```python main.py <nama file yang dievaluasi .py>```


## Usage
Contoh tampilan penggunaan program 
```
F:\Tubes\python-compiler-tbfo> python main.py inputAcc.py

Checking syntax of inputAcc.py...
Progress: 100%   -   Time Elapsed: 6.97 s
Syntax is correct!

F:\Tubes\python-compiler-tbfo> python main.py inputReject.py

Checking syntax of inputReject.py...
Progress: 100%   -   Time Elapsed: 6.56 s
Syntax is wrong. Error at line 5
```

## Contact
Dibuat oleh:
- Fachry Dennis Heraldi (13520139)
- Zayd Muhammad Kawakibi Zuhri (13520144)
- Vito Ghifari (13520153)
