# menu_admin.py
from navigasi import menu_interaktif
from utils import clear, mobil_list
from transaksi import lihat_transaksi

def menu_admin_loop():
    while True:
        pilihan = menu_interaktif('MENU ADMIN RENTAL MOBIL', [
            'Lihat daftar mobil',
            'Tambah mobil',
            'Update mobil',
            'Hapus mobil',
            'Lihat transaksi pembayaran',
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
            clear()
            plat = input('Plat mobil (misal KT8888XX): ').upper().strip()
            if plat in mobil_list:
                print('Plat sudah terdaftar!')
            else:
                nama = input('Nama mobil: ').strip()
                harga = input('Harga sewa per hari: ').strip()
                if not harga.isdigit():
                    print('Harga harus berupa angka!')
                else:
                    mobil_list[plat] = {'nama': nama, 'harga': int(harga), 'status': 'Tersedia', 'penyewa': None, 'batas_waktu': None}
                    print('Mobil berhasil ditambahkan!')
            input('Tekan Enter...')
        elif pilihan == 2:
            clear()
            for i, (plat, data) in enumerate(mobil_list.items(), start=1):
                print(f"{i}. {plat} - {data['nama']} - Rp{data['harga']} - {data['status']}")
            plat_update = input('\nMasukkan plat mobil yang ingin diupdate: ').upper().strip()
            if plat_update not in mobil_list:
                print('Plat tidak ditemukan!')
            else:
                nama_baru = input('Nama baru (kosong = tidak ubah): ').strip()
                harga_baru = input('Harga baru (kosong = tidak ubah): ').strip()
                status_baru = input('Status baru (Tersedia/Disewa): ').strip()
                if nama_baru:
                    mobil_list[plat_update]['nama'] = nama_baru
                if harga_baru.isdigit():
                    mobil_list[plat_update]['harga'] = int(harga_baru)
                if status_baru in ['Tersedia', 'Disewa']:
                    mobil_list[plat_update]['status'] = status_baru
                print('Data mobil berhasil diperbarui!')
            input('Tekan Enter...')
        elif pilihan == 3:
            clear()
            plat_hapus = input('Masukkan plat mobil yang ingin dihapus: ').upper().strip()
            if plat_hapus in mobil_list:
                del mobil_list[plat_hapus]
                print('Mobil berhasil dihapus!')
            else:
                print('Plat tidak ditemukan!')
            input('Tekan Enter...')
        elif pilihan == 4:
            lihat_transaksi()
        else:
            break
