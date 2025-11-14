# autentikasi.py
from utils import users, clear

def login_prompt():
    clear()
    print('=== LOGIN ===')
    username = input('Masukkan username: ').strip()
    password = input('Masukkan password: ').strip()
    if username in users and users[username]['password'] == password:
        print(f"Login berhasil sebagai {users[username]['role'].upper()}")
        input('Tekan Enter...')
        return username, users[username]['role']
    print('Username atau password salah!')
    input('Tekan Enter...')
    return None, None

def register_prompt():
    clear()
    print('=== REGISTER AKUN BARU ===')
    username = input('Masukkan username baru: ').strip()
    if username in users:
        print('Username sudah terdaftar!')
    else:
        password = input('Masukkan password: ').strip()
        users[username] = {'password': password, 'role': 'user'}
        print('Registrasi berhasil! Silakan login.')
    input('Tekan Enter...')
