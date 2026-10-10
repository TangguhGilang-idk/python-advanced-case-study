# Case 01 - Analisis Nilai Mahasiswa

## Masalah yang Diselesaikan
Bagian akademik menerima data nilai mahasiswa berupa list dictionary mentah. Program ini menghitung nilai akhir (Tugas 30%, UTS 30%, UAS 40%), memfilter mahasiswa berprestasi (nilai akhir > 80), meranking dari tertinggi ke terendah, dan mengumumkan mahasiswa terbaik beserta NIM dan detail nilainya.

## Konsep Python yang Digunakan
- **List Comprehension**: kalkulasi nilai akhir dan filter mahasiswa > 80.
- **Lambda Function**: rumus nilai akhir dan key sorting.
- **Filtering & Sorting**: `sorted()` dengan `key=lambda` dan `reverse=True`.

## Cara Menjalankan
```bash
cd case-01-analisis-nilai
python main.py
```
atau langsung run file main.py