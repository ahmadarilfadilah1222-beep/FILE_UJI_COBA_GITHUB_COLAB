# sewa.py
import datetime
from utils import mobil_list, transaksi_list, clear

def sewa_mobil(username):
    clear()
    print('=== SEWA MOBIL ===')
    for i, (plat, data) in enumerate(mobil_list.items(), start=1):
        print(f"{i}. {plat} - {data['nama']} ({data['status']})")

    plat_sewa = input('\nMasukkan plat mobil yang ingin disewa: ').upper().strip()
    if plat_sewa in mobil_list:
        data = mobil_list[plat_sewa]
        if data['status'] == 'Tersedia':
            durasi = input('Berapa hari ingin disewa? ').strip()
            if not durasi.isdigit():
                print('Durasi harus angka!')
            else:
                durasi = int(durasi)
                batas = datetime.datetime.now() + datetime.timedelta(days=durasi)
                data['status'] = 'Disewa'
                data['penyewa'] = username
                data['batas_waktu'] = batas

                total_bayar = data['harga'] * durasi
                waktu_transaksi = datetime.datetime.now()

                transaksi_list.append({
                    'penyewa': username,
                    'mobil': data['nama'],
                    'plat': plat_sewa,
                    'durasi': durasi,
                    'total_bayar': total_bayar,
                    'waktu_bayar': waktu_transaksi
                })

                print(f"Mobil {data['nama']} berhasil disewa!")
                print(f"Total bayar: Rp{total_bayar}")
                print(f"Tanggal pembayaran: {waktu_transaksi}")
                print(f"Batas waktu pengembalian: {batas}")
        else:
            print('Mobil sedang disewa!')
    else:
        print('Plat tidak ditemukan!')
    input('Tekan Enter...')
    
def kembalikan_mobil(username):
    clear()
    ditemukan = False
    for data in mobil_list.values():
        if data.get('penyewa') == username:
            sekarang = datetime.datetime.now()
            if data.get('batas_waktu') and sekarang > data['batas_waktu']:
                print('Anda telat mengembalikan mobil! Harap hubungi admin.')
            data['status'] = 'Tersedia'
            data['penyewa'] = None
            data['batas_waktu'] = None
            print(f"Mobil {data['nama']} telah dikembalikan.")
            ditemukan = True
    if not ditemukan:
        print('Anda belum menyewa mobil.')
    input('Tekan Enter...')
