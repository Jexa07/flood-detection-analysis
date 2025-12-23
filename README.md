# 🌊 Flood Detection & Time‑Stepped Flood Simulation

A **DEM‑based flood simulation and visualization project** that demonstrates how flood inundation can progressively increase over time under an extreme rainfall scenario.

This project focuses on **terrain‑driven flood susceptibility**, **time‑stepped simulation**, and **clear visual communication**, rather than full hydrodynamic rainfall‑runoff modeling.

---

## 📌 Project Overview

The system uses a **Digital Elevation Model (DEM)** as the base input to identify low‑lying flood‑prone areas and generate **scenario‑based flood simulations**.

Instead of complex physical equations, the model implements a **time‑stepped, scenario‑based approach** where flood severity increases with rainfall duration. This makes the results easy to understand, visualize, and present.

---

## 🎯 Key Features

- Uses original **DEM (`dem.tif`)** as terrain input  
- DEM‑based flood depth estimation  
- **Time‑stepped simulation** for rainfall durations:
  - 20 minutes  
  - 30 minutes  
  - 40 minutes  
  - 50 minutes  
  - 60 minutes  
- Frame‑by‑frame flood progression  
- PNG export for each timestep  
- Animated GIF showing flood progression  
- Interactive frontend visualization (React + Leaflet)

---

## 🛰️ Input Data

### Digital Elevation Model (DEM)
- File: `data/dem.tif`
- Represents ground elevation
- Used to identify low‑lying flood‑prone areas
- All flood simulation outputs are derived from this DEM

The DEM can be viewed and verified using **QGIS** or **GRASS GIS**.

---

## ⏱️ Time‑Stepped Flood Simulation Logic

This project implements a **scenario‑based flood simulation**:

- A maximum flood depth is estimated from terrain elevation
- Rainfall duration is defined in **minutes**
- Each timestep scales flood severity using predefined multipliers

### Rainfall Duration Mapping

| Rainfall Duration | Severity Multiplier |
|------------------|--------------------|
| 20 minutes | 0.30 |
| 30 minutes | 0.45 |
| 40 minutes | 0.60 |
| 50 minutes | 0.80 |
| 60 minutes | 1.00 |

Each timestep generates a separate flood depth raster and visualization frame.

> ⚠️ Note:  
> This is a **scenario‑based visualization**, not a physically‑based hydrodynamic rainfall‑runoff model.

---


## 🌐 Frontend Visualization

The frontend is built using:
- React  
- Leaflet  

Features:
- Interactive map view  
- Flood overlay visualization  
- Opacity control  
- Time‑based animation support  

---

## 🚀 How to Run the Project

### Backend

```bash
cd backend
pip install -r requirements.txt
python simulation.py
python export_png.py
python make_gif.py
python -m uvicorn api:app --reload

Frontend

cd frontend
npm install
npm start

