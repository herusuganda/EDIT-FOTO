from PIL import Image
import cv2
import numpy as np
import math

# Buka gambar
img = Image.open("foto.jpg")
img = img.convert("RGB")

# Konversi ke numpy
frame = np.array(img)

# Ukuran gambar
h, w, _ = frame.shape

# Buat video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("animasi_halus.mp4", fourcc, 30, (w, h))

# Total frame
total_frames = 120

for i in range(total_frames):

    # Copy frame asli
    animated = frame.copy()

    # Gerakan halus kiri kanan
    shift_x = int(8 * math.sin(i * 0.1))

    # Gerakan halus atas bawah
    shift_y = int(4 * math.sin(i * 0.08))

    # Matrix translasi
    M = np.float32([
        [1, 0, shift_x],
        [0, 1, shift_y]
    ])

    # Geser gambar TANPA mengubah struktur
    moved = cv2.warpAffine(animated, M, (w, h))

    # Tambahkan zoom sangat kecil agar terasa hidup
    scale = 1 + 0.01 * math.sin(i * 0.05)

    zoomed = cv2.resize(
        moved,
        None,
        fx=scale,
        fy=scale
    )

    # Crop kembali ke ukuran asli
    zh, zw, _ = zoomed.shape

    start_x = (zw - w) // 2
    start_y = (zh - h) // 2

    final = zoomed[
        start_y:start_y+h,
        start_x:start_x+w
    ]

    # Pastikan ukuran sama
    final = cv2.resize(final, (w, h))

    # Tulis frame
    out.write(cv2.cvtColor(final, cv2.COLOR_RGB2BGR))

# Simpan video
out.release()

print("Video berhasil dibuat: animasi_halus.mp4")