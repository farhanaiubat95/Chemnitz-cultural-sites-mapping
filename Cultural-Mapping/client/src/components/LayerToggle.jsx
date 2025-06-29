import React from "react";

// Define circle colors per layer
const layerColors = {
  culturalSites: "#1e40af",     // blue-800
  busParkings: "#15803d",       // green-800
  motorhomeParkings: "#b91c1c", // red-700
  districts: "#2563eb",         // blue-600
};

const LayerToggle = ({ layers, setLayers }) => {
  const handleToggle = (layerName) => {
    setLayers((prev) => ({
      ...prev,
      [layerName]: !prev[layerName],
    }));
  };

  return (
    <div className="absolute top-4 left-14 bg-white p-4 rounded shadow-md z-[1000] text-sm">
      <h3 className="font-semibold mb-2 text-base">Map Layers</h3>
      {Object.keys(layers).map((layer) => {
        const label = layer
          .replace(/([A-Z])/g, " $1")
          .replace(/^./, (str) => str.toUpperCase());

        return (
          <label
            key={layer}
            className="flex items-center justify-between mb-2 cursor-pointer text-sm"
          >
            <div className="flex items-center">
              <input
                type="checkbox"
                checked={layers[layer]}
                onChange={() => handleToggle(layer)}
                className="mr-2"
              />
              <span>{label}</span>
            </div>
            <span
              className="w-3 h-3 rounded-full ml-3"
              style={{ backgroundColor: layerColors[layer] }}
            ></span>
          </label>
        );
      })}
    </div>
  );
};

export default LayerToggle;
