import os
import time
import random

# Representasi layout dalam bentuk string
layout = \
    """
            _____
           /     \\
          /       \\
    ,----(         )----.
   /      \\       /      \\
  /        \\_____/        \\
  \\        /     \\        /
   \\      /       \\      /
    )----(         )----(
   /      \\       /      \\
  /        \\_____/        \\
  \\        /     \\        /
   \\      /       \\      /
    `----(         )----'
          \\       /
           \\_____/


    """.split('\n')

# Memecah layout menjadi list karakter
layout = [
    list(row) for row in layout
]

# Karakter pembatas dari heksagon
bound_chars = ['\\', '/', '\'', '_', '-', '.', ',', '`', '(', ')']

# Titik awal dalam setiap heksagon
points = [
    (4, 14),
    (6, 6),
    (6, 22),
    (9, 14),
    (11, 6),
    (11, 22),
    (14, 14),
]

# Fungsi untuk mencetak layout heksagon
def print_layout():
    # os.system('clear')
    print("\n".join(["".join(row) for row in layout]))

# Fungsi rekursif untuk flood fill
def _flood(x, y):
    # Cek batas layout
    if x >= len(layout) or x < 0 or y < 0 or y >= len(layout[x]):
        return

    # Cek batas dalam heksagon
    if layout[x][y] in bound_chars:
        return

    # Cek apakah sudah diisi
    if layout[x][y] == '#':
        return

    # Isi posisi saat ini
    layout[x][y] = '#'

    # Tambahkan jeda
    time.sleep(0.01)

    # Cetak layout yang telah diubah
    print_layout()

    # Rekursif memanggil fungsi flood fill untuk tetangga
    _flood(x + 1, y)
    _flood(x - 1, y)
    _flood(x, y + 1)
    _flood(x, y - 1)

# Fungsi utama untuk memulai flood fill dari titik awal
def flood(x, y):
    _flood(x, y)

# Acak urutan titik awal flood fill
random.shuffle(points)

# Lakukan flood fill untuk setiap heksagon
for X, Y in points:
    flood(X, Y)
