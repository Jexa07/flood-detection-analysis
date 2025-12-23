from PIL import Image
import os

png_dir = "../processing/png"
output_gif = "../processing/flood_simulation.gif"

frames = []
order = [20, 30, 40, 50, 60]

for t in order:
    img_path = os.path.join(png_dir, f"flood_depth_{t}min.png")
    frames.append(Image.open(img_path))

frames[0].save(
    output_gif,
    format="GIF",
    append_images=frames[1:],
    save_all=True,
    duration=1000,  # milliseconds per frame
    loop=0
)

print("GIF created successfully:", output_gif)
