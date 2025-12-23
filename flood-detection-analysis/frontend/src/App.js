import { useState } from "react";
import MapView from "./MapView";
import Legend from "./Legend";
import "./App.css";

function App() {
  const [showDepth, setShowDepth] = useState(true);
  const [showMask, setShowMask] = useState(true);
  const [opacity, setOpacity] = useState(0.7);

  return (
    <div className="app">
      <div className="sidebar">
        <h2>🌊 Flood Simulator</h2>
        <p className="subtitle">Terrain‑aware flood modeling</p>

        <div className="section">
          <h3>Layers</h3>

          <label>
            <input
              type="checkbox"
              checked={showDepth}
              onChange={() => setShowDepth(!showDepth)}
            />
            Flood Depth
          </label>

          <label>
            <input
              type="checkbox"
              checked={showMask}
              onChange={() => setShowMask(!showMask)}
            />
            Flood Mask
          </label>
        </div>

        <div className="section">
          <h3>Visualization</h3>

          <label>Opacity</label>
          <input
            type="range"
            min="0"
            max="1"
            step="0.05"
            value={opacity}
            onChange={(e) => setOpacity(e.target.value)}
          />

          <Legend />
        </div>

        <div className="section info">
          <h3>Scenario</h3>
          <p><b>Rainfall:</b> Extreme</p>
          <p><b>Threshold:</b> 0.02 m</p>
        </div>
      </div>

      <div className="map-frame">
        <MapView
          showDepth={showDepth}
          showMask={showMask}
          opacity={opacity}
        />
      </div>
    </div>
  );
}

export default App;
