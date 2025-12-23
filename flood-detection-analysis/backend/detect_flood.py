import json
import numpy as np
import rasterio

# Load parameters
with open("../processing/parameters.json") as f:
    params = json.load(f)

threshold = params["flood_depth_threshold_m"]

# Load flood depth
with rasterio.open("../processing/flood_depth.tif") as src:
    depth = src.read(1)
    meta = src.meta.copy()

# Create flood mask (STRICT threshold)
flood_mask = np.zeros_like(depth, dtype=np.uint8)
flood_mask[depth >= threshold] = 1

# Save mask
meta.update(dtype="uint8", nodata=0)

with rasterio.open("../processing/flood_mask.tif", "w", **meta) as dst:
    dst.write(flood_mask, 1)

print("Flood detection complete.")
