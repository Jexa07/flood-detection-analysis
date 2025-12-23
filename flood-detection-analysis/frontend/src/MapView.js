import { MapContainer, ImageOverlay } from "react-leaflet";
import L from "leaflet";
import { useEffect, useState } from "react";
import "leaflet/dist/leaflet.css";

export default function MapView({ showDepth, showMask, opacity }) {
  const [bounds, setBounds] = useState(null);

  useEffect(() => {
    const img = new Image();
    img.src = "http://127.0.0.1:8000/results/flood_depth.png";
    img.onload = () => {
      setBounds([
        [0, 0],
        [img.height, img.width],
      ]);
    };
  }, []);

  if (!bounds) {
    return (
      <div style={{ color: "white", padding: "20px" }}>
        Loading flood map…
      </div>
    );
  }

  return (
    <MapContainer
      crs={L.CRS.Simple}
      bounds={bounds}
      style={{ height: "100%", width: "100%" }}
      whenReady={(map) => map.target.fitBounds(bounds)}
    >
      {showDepth && (
        <ImageOverlay
          url="http://127.0.0.1:8000/results/flood_depth.png"
          bounds={bounds}
          opacity={opacity}
        />
      )}

      {showMask && (
        <ImageOverlay
          url="http://127.0.0.1:8000/results/flood_mask.png"
          bounds={bounds}
          opacity={0.6}
        />
      )}
    </MapContainer>
  );
}
