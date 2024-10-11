# GitHub Repository Scraper and Cloner

## Deskripsi Proyek

Ini adalah proyek Python yang digunakan untuk mengambil daftar repositories dari halaman GitHub user, menampilkan detail repository beserta file-file yang ada di dalamnya, dan memungkinkan pengguna untuk meng-clone repositories tersebut secara lokal. Data hasil scraping juga disimpan dalam file CSV untuk referensi lebih lanjut.

### Fitur Utama
- Mengambil informasi repositories dari halaman GitHub berdasarkan username.
- Menampilkan deskripsi repositories, label, dan daftar file yang ada di dalam repository.
- Menyimpan informasi repositories dalam format CSV.
- Meng-clone repository pilihan pengguna ke direktori lokal.

## Cara Instalasi

1. **Clone repository ini** (jika Anda belum mendownload kodenya):
    ```bash
    git clone https://github.com/Fajarxyta/Repo-scrape
    ```

2. **Masuk ke direktori proyek:**
    ```bash
    cd Repo-scrape
    ```

3. **Install dependencies**:
    Anda perlu menginstal beberapa modul Python untuk menjalankan proyek ini. Pastikan Anda sudah mengaktifkan virtual environment (opsional), lalu jalankan:
    ```bash
    pip install -r requirements.txt
    ```
    Isi dari `requirements.txt`:
    ```
    requests
    beautifulsoup4
    pandas
    rich
    gitpython
    ```

4. **Jalankan Program:**
    Setelah dependencies terinstal, Anda bisa langsung menjalankan program dengan menggunakan:
    ```bash
    python run.py
    ```

## Cara Penggunaan

1. Ketika menjalankan program, Anda akan diminta untuk memasukkan **username GitHub** dari pengguna yang ingin Anda lihat repositories-nya.
   
2. Program akan mengambil daftar repositories, menampilkan informasi seperti:
    - Nama repository
    - URL repository
    - Deskripsi repository (jika ada)
    - Daftar file dalam repository

3. Setelah informasi ditampilkan, Anda akan diberi pilihan untuk meng-clone repository ke direktori lokal dengan menjawab "y" atau "n".

4. Jika Anda memilih untuk meng-clone, repository akan di-clone ke dalam direktori `Peyimpanan/` di dalam folder proyek Anda.

5. Pada akhirnya, program akan menyimpan informasi repository ke dalam file `repository.csv` di direktori proyek.

## Struktur Proyek

```bash
.
├── Penyimpanan/           # Folder penyimpanan repository yang di-clone
├── run.py                 # File utama yang berisi script Python
├── README.md              # Dokumentasi proyek
├── repository.csv         # File CSV berisi informasi repository (dihasilkan setelah scraping)
└── requirements.txt       # File yang berisi dependencies untuk proyek
