# Case 03 - Sistem Keamanan Akun & Audit Log Login

## Masalah yang Diselesaikan
Validasi kredensial yang ketat (username min. 5 karakter alfanumerik; password min. 8 karakter dan memuat angka) disertai audit trail otomatis untuk setiap percobaan login, berhasil maupun gagal, tanpa mengotori logika otentikasi.

## Konsep Python yang Digunakan
- **RegEx (`re`)**: validasi format username dan password.
- **Decorator & Closure**: `buat_audit_logger()` membungkus fungsi `login` dan mencatat timestamp, nama pengguna, serta status BERHASIL/DITOLAK beserta alasannya.
- **Property Decorator (`@property`)**: class `User` mengenkapsulasi username dan password.

## Cara Menjalankan
```bash
cd case-03-login-security
python main.py
```
maupun langsung run file main.py