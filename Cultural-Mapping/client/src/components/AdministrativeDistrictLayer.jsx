// the administrative district boundaries from Stadtteile.geojson

import { useEffect, useState } from "react";
import { GeoJSON } from "react-leaflet";

const AdministrativeDistrictLayer = () => {
  const [districts, setDistricts] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/districts/")
      .then((res) => res.json())
      .then((data) => setDistricts(data.features))
      .catch((err) => console.error("Error fetching districts:", err));
  }, []);

  const onEachFeature = (feature, layer) => {
    const { name, district_id, area_km2 } = feature.properties;
    layer.bindPopup(`
      <strong>${name}</strong><br/>
      District ID: ${district_id}<br/>
      Area: ${area_km2} km²
    `);
  };

  return (
    <>
      {districts.length > 0 && (
        <GeoJSON
          data={districts}
          style={{ color: "#2262CC", weight: 2, fillOpacity: 0.1 }}
          onEachFeature={onEachFeature}
        />
      )}
    </>
  );
};

export default AdministrativeDistrictLayer;
