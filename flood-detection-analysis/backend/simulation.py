import rasterio
import numpy as np
import os

# =========================
# CONFIG
# =========================

DEM_PATH = "../data/dem.tif"
OUTPUT_DIR = "../processing"

# Rainfall durations (minutes)
RAINFALL_MINUTES = [20, 30, 40, 50, 60]

# Scenario-based severity multipliers
RAIN_MULTIPLIER = {
    20: 0.3,
    30: 0.45,
    40: 0.6,
    50: 0.8,
    60: 1.0
}

# =========================
# LOAD DEM
# =========================

with rasterio.open(DEM_PATH) as dem_src:
    dem = dem_src.read(1).astype("float32")
    dem_meta = dem_src.meta
    dem_crs = dem_src.crs
    dem_transform = dem_src.transform

print("DEM loaded successfully")

# =========================
# BASE FLOOD CALCULATION
# (Worst-case scenario)
# =========================

# Simple scenario-based flood logic
# Lower elevation → higher flood depth
min_elev = np.nanmin(dem)
max_elev = np.nanmax(dem)

normalized = (max_elev - dem) / (max_elev - min_elev)
normalized = np.clip(normalized, 0, 1)

# Maximum flood depth in meters (scenario-based)
MAX_FLOOD_DEPTH = 0.3
base_flood_depth = normalized * MAX_FLOOD_DEPTH

print("Base flood depth calculated")

# =========================
# TIME-STEPPED OUTPUTS
# =========================

os.makedirs(OUTPUT_DIR, exist_ok=True)

for minutes in RAINFALL_MINUTES:
    scaled_flood = base_flood_depth * RAIN_MULTIPLIER[minutes]

    output_path = os.path.join(
        OUTPUT_DIR, f"flood_depth_{minutes}min.tif"
    )

    meta = dem_meta.copy()
    meta.update({
        "dtype": "float32",
        "count": 1,
        "nodata": 0
    })

    with rasterio.open(output_path, "w", **meta) as dst:
        dst.write(scaled_flood.astype("float32"), 1)

    print(f"Generated flood depth for {minutes} minutes")

print("Time-stepped flood simulation completed")
