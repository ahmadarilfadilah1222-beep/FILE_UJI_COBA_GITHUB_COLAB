# transaksi.py
from prettytable import PrettyTable
from utils import transaksi_list, fmt_dt, clear

def lihat_transaksi():
    clear()
    print('=== RIWAYAT TRANSAKSI ===')
    table = PrettyTable(['Penyewa', 'Mobil', 'Plat', 'Durasi', 'Total Bayar', 'Waktu Bayar'])
    for t in transaksi_list:
        table.add_row([
            t['penyewa'],
            t['mobil'],
            t['plat'],
            f"{t['durasi']} hari",
            f"Rp{t['total_bayar']}",
            fmt_dt(t['waktu_bayar'])
        ])
    print(table)
    input('Tekan Enter...')
