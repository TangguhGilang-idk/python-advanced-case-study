"""Studi Kasus 2 - Streaming Data Sensor IoT Hemat Memori.

Konsep: iterator pattern, generator function (yield), efisiensi memori.
"""

import random
import sys
from itertools import islice


def sensor_suhu(min_c=15.0, max_c=38.0, seed=None):
    """Generator tak hingga: menghasilkan satu suhu setiap kali diminta."""
    rng = random.Random(seed)
    while True:
        yield round(rng.uniform(min_c, max_c), 1)


def kategorikan(suhu):
    if suhu < 20:
        return "Dingin"
    if suhu <= 30:
        return "Normal"
    return "Panas"


def stream_terkategori(sumber):
    """Generator kedua (pipeline): setiap suhu langsung diberi kategori."""
    for suhu in sumber:
        yield suhu, kategorikan(suhu)


def main():
    sensor = sensor_suhu(seed=42)
    print(f"Tipe sensor: {type(sensor).__name__} (iterator, tidak menyimpan data)\n")

    print("Pembacaan manual dengan next()")
    for i in range(1, 4):
        suhu = next(sensor)
        print(f"Bacaan #{i:02d} | {suhu:5.1f} C | {kategorikan(suhu)}")

    print("\nStreaming terkategori (12 bacaan)")
    print(f"{'No':<5}{'Suhu (C)':>10}   {'Status':<8}")
    print("-" * 28)
    stream = stream_terkategori(sensor_suhu(seed=7))
    for i, (suhu, status) in enumerate(islice(stream, 12), start=1):
        print(f"{i:<5}{suhu:>10.1f}   {status:<8}")

    n = 1_000_000
    gen = (x for x in range(n))
    lst = list(range(n))
    print("\nPerbandingan memori untuk 1.000.000 data")
    print(f"Generator : {sys.getsizeof(gen):>10,} byte")
    print(f"List      : {sys.getsizeof(lst):>10,} byte")


if __name__ == "__main__":
    main()
