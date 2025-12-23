import rasterio
import matplotlib.pyplot as plt
import os

INPUT_DIR = "../processing"
OUTPUT_DIR = "../processing/png"

os.makedirs(OUTPUT_DIR, exist_ok=True)

TIME_STEPS = [20, 30, 40, 50, 60]

for t in TIME_STEPS:
    tif_path = os.path.join(INPUT_DIR, f"flood_depth_{t}min.tif")
    png_path = os.path.join(OUTPUT_DIR, f"flood_depth_{t}min.png")

    with rasterio.open(tif_path) as src:
        data = src.read(1)

    plt.figure(figsize=(6, 6))
    plt.imshow(data, cmap="Blues")
    plt.colorbar(label="Flood depth (m)")
    plt.title(f"Flood Depth after {t} minutes")
    plt.axis("off")
    plt.savefig(png_path, dpi=200, bbox_inches="tight")
    plt.close()

    print(f"Exported PNG for {t} minutes")

print("All PNG frames exported")
