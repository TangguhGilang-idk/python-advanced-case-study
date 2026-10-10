BOBOT = {"tugas": 0.30, "uts": 0.30, "uas": 0.40}

data_mahasiswa = [
    {"nama": "Gilang", "nim": "2595114026", "tugas": 85, "uts": 80, "uas": 88},
    {"nama": "Fandi", "nim": "2595114028", "tugas": 70, "uts": 65, "uas": 75},
    {"nama": "Bisma", "nim": "2595114034", "tugas": 90, "uts": 85, "uas": 92},
    {"nama": "Fuad", "nim": "2595114030", "tugas": 78, "uts": 82, "uas": 80},
    {"nama": "Alfa", "nim": "2595114029", "tugas": 60, "uts": 70, "uas": 65},
]

hitung_nilai_akhir = lambda m: round(
    m["tugas"] * BOBOT["tugas"] + m["uts"] * BOBOT["uts"] + m["uas"] * BOBOT["uas"], 2
)


def tampilkan_tabel(judul, daftar):
    print(f"\n    {judul}    ")
    print(f"{'No':<4}{'NIM':<12}{'Nama':<12}{'Nilai Akhir':>12}")
    print("-" * 40)
    for i, m in enumerate(daftar, start=1):
        print(f"{i:<4}{m['nim']:<12}{m['nama']:<12}{m['nilai_akhir']:>12.2f}")


def main():
    hasil = [{**m, "nilai_akhir": hitung_nilai_akhir(m)} for m in data_mahasiswa]
    tampilkan_tabel("Nilai Akhir Seluruh Mahasiswa", hasil)

    berprestasi = [m for m in hasil if m["nilai_akhir"] > 80]
    tampilkan_tabel("Mahasiswa Berprestasi (Nilai Akhir > 80)", berprestasi)

    ranking = sorted(hasil, key=lambda m: m["nilai_akhir"], reverse=True)
    tampilkan_tabel("Ranking Mahasiswa", ranking)

    terbaik = ranking[0]
    print("\n    MAHASISWA TERBAIK    ")
    print(f"Nama        : {terbaik['nama']}")
    print(f"NIM         : {terbaik['nim']}")
    print(f"Tugas / UTS / UAS : {terbaik['tugas']} / {terbaik['uts']} / {terbaik['uas']}")
    print(f"Nilai Akhir : {terbaik['nilai_akhir']:.2f}")


if __name__ == "__main__":
    main()
