# utils.py
import os
import datetime
from prettytable import PrettyTable

# Data pusat
users = {
    "admin": {"password": "admin123", "role": "admin"}
}

mobil_list = {
    "KT1234AA": {"nama": "Toyota Alphard", "harga": 1500000, "status": "Tersedia", "penyewa": None, "batas_waktu": None},
    "DA5678BB": {"nama": "BMW i8", "harga": 2500000, "status": "Tersedia", "penyewa": None, "batas_waktu": None},
    "KH8765CC": {"nama": "Mercedes Benz S-Class", "harga": 2800000, "status": "Tersedia", "penyewa": None, "batas_waktu": None},
    "KB4321DD": {"nama": "Range Rover Evoque", "harga": 2000000, "status": "Tersedia", "penyewa": None, "batas_waktu": None},
    "KU9999EE": {"nama": "Porsche Cayenne", "harga": 3000000, "status": "Tersedia", "penyewa": None, "batas_waktu": None}
}

transaksi_list = []

def clear():
    """Bersihkan layar (cross-platform)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def fmt_dt(dt):
    if not dt:
        return "-"
    if isinstance(dt, datetime.datetime):
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    return str(dt)
