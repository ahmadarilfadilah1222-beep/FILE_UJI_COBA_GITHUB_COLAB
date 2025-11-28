# menu_user.py
from navigasi import menu_interaktif
from utils import clear, mobil_list, transaksi_list, fmt_dt
from sewa import sewa_mobil, kembalikan_mobil

def menu_user_loop(username):
    while True:
        pilihan = menu_interaktif(f"MENU PENGGUNA ({username})", [
            'Lihat daftar mobil',
            'Sewa mobil',
            'Kembalikan mobil',
            'Lihat transaksi saya (riwayat)',
            'Logout'
        ])
        if pilihan == 0:
            clear()
            from prettytable import PrettyTable
            table = PrettyTable(['Plat', 'Nama', 'Harga', 'Status'])
            for plat, d in mobil_list.items():
                table.add_row([plat, d['nama'], f"Rp{d['harga']}", d['status']])
            print(table)
            input('Tekan Enter...')
        elif pilihan == 1:
            sewa_mobil(username)
        elif pilihan == 2:
            kembalikan_mobil(username)
        elif pilihan == 3:
            clear()
            from prettytable import PrettyTable
            table = PrettyTable(['Penyewa', 'Mobil', 'Plat', 'Durasi', 'Total Bayar', 'Waktu Bayar'])
            for t in transaksi_list:
                if t['penyewa'] == username:
                    table.add_row([t['penyewa'], t['mobil'], t['plat'], f"{t['durasi']} hari", f"Rp{t['total_bayar']}", fmt_dt(t['waktu_bayar'])])
            print(table)
            input('Tekan Enter...')
        else:
            break
