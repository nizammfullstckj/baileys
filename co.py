import os
import sqlite3
import base64

# ANSI
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

# TAMPILAN INPUT
os.system('cls' if os.name == 'nt' else 'clear')
print(f"{MAGENTA}XATANIC11{RESET}")
print("PILIH PREFENCY")
print("1. DATABASE")
print("2. SQL")
print("3. TOOLS ENCODE/DECODE BASE64")

# INPUT PILIHAN
pilihan = input("Masukkan pilihan: ")

if pilihan == "1":
    # DATABASE
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    print("DATABASE")
    print("1. Buat tabel")
    print("2. Tambah data")
    print("3. Lihat data")
    pilihan_db = input("Masukkan pilihan: ")
    if pilihan_db == "1":
        # Buat tabel
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users
            (id INTEGER PRIMARY KEY, name TEXT, email TEXT)
        ''')
        conn.commit()
        print("Tabel berhasil dibuat")
    elif pilihan_db == "2":
        # Tambah data
        name = input("Masukkan nama: ")
        email = input("Masukkan email: ")
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print("Data berhasil ditambahkan")
    elif pilihan_db == "3":
        # Lihat data
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    conn.close()
elif pilihan == "2":
    # SQL
    print("SQL")
    print("1. Buat t