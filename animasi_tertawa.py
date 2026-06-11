from PIL import Image, ImageEnhance
import cv2
import numpy as np

img = Image.open("saya sendiri.jpg")
img = img.convert("RGB")
w, h = img.size

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('tertawa_4detik.mp4', fourcc, 25, (w, h))

total_frames = 100

for i in range(total_frames):
    progress = i / total_frames
    
    scale = 1 + 0.15 * np.sin(progress * np.pi)
    
    img_resized = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
    img_np = np.array(img_resized)
    
    sw, sh = img_resized.size
    start_x = (sw - w) // 2
    start_y = (sh - h) // 2
    
    frame = img_np[start_y:start_y+h, start_x:start_x+w]
    
    brightness = 1 + 0.1 * np.sin(progress * np.pi * 2)
    frame = np.clip(frame * brightness, 0, 255).astype(np.uint8)
    
    out.write(frame)

out.release()
print("Video berhasil dibuat: tertawa_4detik.mp4")