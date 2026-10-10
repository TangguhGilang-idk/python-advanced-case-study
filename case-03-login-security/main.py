"""Studi Kasus 3 - Sistem Keamanan Akun & Audit Log Login.

Konsep: RegEx, decorator & closure, @property.
"""

import functools
import hashlib
import re
from datetime import datetime

USERNAME_PATTERN = re.compile(r"^[A-Za-z0-9]{5,}$")
PASSWORD_PATTERN = re.compile(r"^(?=.*\d).{8,}$")


class User:
    """Model pengguna dengan username/password terenkapsulasi."""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not USERNAME_PATTERN.fullmatch(value):
            raise ValueError(
                "Format username tidak sesuai (min. 5 karakter, hanya huruf dan angka)"
            )
        self._username = value

    @property
    def password(self):
        return "********"

    @password.setter
    def password(self, value):
        if len(value) < 8:
            raise ValueError("Password terlalu pendek (minimal 8 karakter)")
        if not PASSWORD_PATTERN.fullmatch(value):
            raise ValueError("Password harus mengandung minimal satu angka")
        self._password_hash = self._hash(value)

    @staticmethod
    def _hash(teks):
        return hashlib.sha256(teks.encode()).hexdigest()

    def cek_password(self, password):
        return self._hash(password) == self._password_hash


def buat_audit_logger():
    """Closure: menyimpan riwayat log di variabel 'riwayat' (tanpa file)."""
    riwayat = []

    def audit(func):
        @functools.wraps(func)
        def wrapper(username, password):
            waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                func(username, password)
                status, alasan = "BERHASIL", ""
                hasil = True
            except ValueError as err:
                status, alasan = "DITOLAK", f" | Alasan: {err}"
                hasil = False
            baris = f"[{waktu}] User: {username!r} | Status: {status}{alasan}"
            riwayat.append(baris)
            print(baris)
            return hasil

        wrapper.riwayat = riwayat
        return wrapper

    return audit


audit_log = buat_audit_logger()

DB_USER = {}


def daftarkan(username, password):
    """Mendaftarkan pengguna baru (tervalidasi lewat class User)."""
    user = User(username, password)
    DB_USER[user.username] = user


@audit_log
def login(username, password):
    """Logika otentikasi murni; logging ditangani decorator."""
    User(username, password)
    user = DB_USER.get(username)
    if user is None:
        raise ValueError("Username tidak terdaftar")
    if not user.cek_password(password):
        raise ValueError("Password salah")


def main():
    daftarkan("Gilang26admin", "07 Oktober 2026")

    skenario = [
        ("Format username salah (ada simbol dan spasi)", "len> ", "07 Oktober 2026"),
        ("Username terlalu pendek", "len", "07 Oktober 2026"),
        ("Password terlalu pendek", "Gilang26admin", "Okt"),
        ("Password tanpa angka", "Gilang26admin", "passwordsaja"),
        ("Password salah", "Gilang26admin", "salah"),
        ("Login sukses", "Gilang26admin", "07 Oktober 2026"),
    ]
    for i, (judul, u, p) in enumerate(skenario, start=1):
        print(f"\nSkenario {i}: {judul}")
        login(u, p)

    print(f"\nTotal {len(login.riwayat)} percobaan tercatat di riwayat audit")


if __name__ == "__main__":
    main()
