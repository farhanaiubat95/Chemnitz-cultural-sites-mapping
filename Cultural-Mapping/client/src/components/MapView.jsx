// src/components/MapView.jsx
import { MapContainer, TileLayer, GeoJSON } from 'react-leaflet';
import { useEffect, useState } from 'react';
import L from 'leaflet';
import LayerToggle from './LayerToggle';

// Fix Leaflet default icon URLs
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl:
    'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon-2x.png',
  iconUrl:
    'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png',
  shadowUrl:
    'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
});

// Custom icons
const blueIcon = new L.Icon({
  iconUrl:
    'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-blue.png',
  shadowUrl:
    'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41],
});

const greenIcon = new L.Icon({
  iconUrl:
    'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-green.png',
  shadowUrl:
    'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41],
});

const redIcon = new L.Icon({
  iconUrl:
    'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png',
  shadowUrl:
    'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41],
});

// GeoJSON wrapper
const wrapFeatureCollection = (data) => {
  if (!data) return null;
  if (data.type === 'FeatureCollection') return data;
  if (Array.isArray(data)) {
    return {
      type: 'FeatureCollection',
      features: data,
    };
  }
  return null;
};

// Marker factories
const culturalMarker = (feature, latlng) => {
  return L.marker(latlng, { icon: blueIcon });
};

const busMarker = (feature, latlng) => {
  return L.marker(latlng, { icon: greenIcon });
};

const motorhomeMarker = (feature, latlng) => {
  return L.marker(latlng, { icon: redIcon });
};

// Popups
const onCulturalSite = (feature, layer) => {
  const p = feature.properties;
  const html = `
    <div style="background-color: #e0f0ff; padding: 8px; border-radius: 6px;">
      <strong>${p.name || 'Unnamed'}</strong><br/>
      Type: ${p.tourism || 'N/A'}<br/>
      Operator: ${p.operator || 'N/A'}<br/>
      Wheelchair Access: ${p.wheelchair_access || 'N/A'}<br/>
      ${p.website ? `<a href="${p.website}" target="_blank">Website</a>` : ''}
    </div>
  `;
  layer.bindPopup(html);
};

const onBusParking = (feature, layer) => {
  const p = feature.properties;
  const html = `
    <div>
      <strong>Bus Parking</strong><br/>
      Location: ${p.location || 'N/A'}<br/>
      Capacity: ${p.capacity || 'N/A'}<br/>
      Cost: ${p.cost || 'Free'}<br/>
      Remarks: ${p.remarks || 'None'}
    </div>
  `;
  layer.bindPopup(html);
};

const onMotorhomeParking = (feature, layer) => {
  const p = feature.properties;
  const html = `
    <div>
      <strong>Motorhome Parking</strong><br/>
      Location: ${p.location || 'N/A'}<br/>
      Capacity: ${p.capacity || 'N/A'}<br/>
      Cost: ${p.cost || 'Free'}<br/>
      Remarks: ${p.remarks || 'None'}
    </div>
  `;
  layer.bindPopup(html);
};

const onEachDistrictFeature = (feature, layer) => {
  const p = feature.properties;
  layer.bindPopup(
    `<strong>${p.name}</strong><br/>District ID: ${p.district_id}<br/>Area: ${p.area_km2} km²`
  );
};

// Main Component
const MapView = () => {
  const [culturalSites, setCulturalSites] = useState(null);
  const [busParkings, setBusParkings] = useState(null);
  const [motorhomeParkings, setMotorhomeParkings] = useState(null);
  const [districts, setDistricts] = useState(null);

  const [layers, setLayers] = useState({
    culturalSites: true,
    busParkings: true,
    motorhomeParkings: true,
    districts: true,
  });

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/cultural-sites/')
      .then((res) => res.json())
      .then((data) => setCulturalSites(wrapFeatureCollection(data)))
      .catch((err) => console.error('Error loading cultural sites:', err));

    fetch('http://127.0.0.1:8000/api/bus-parkings/')
      .then((res) => res.json())
      .then((data) => setBusParkings(wrapFeatureCollection(data)))
      .catch((err) => console.error('Error loading bus parkings:', err));

    fetch('http://127.0.0.1:8000/api/motorhome-parkings/')
      .then((res) => res.json())
      .then((data) => setMotorhomeParkings(wrapFeatureCollection(data)))
      .catch((err) => console.error('Error loading motorhome parkings:', err));

    fetch('http://127.0.0.1:8000/api/districts/')
      .then((res) => res.json())
      .then((data) => setDistricts(wrapFeatureCollection(data)))
      .catch((err) => console.error('Error loading districts:', err));
  }, []);

  const polygonStyle = {
    color: '#3388ff',
    weight: 2,
    fillOpacity: 0.2,
  };

  return (
    <div className="relative">
      <LayerToggle layers={layers} setLayers={setLayers} />

      <MapContainer center={[50.83, 12.92]} zoom={12} className="h-screen w-full">
        <TileLayer
          attribution="&copy; OpenStreetMap contributors"
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        {layers.districts && districts && (
          <GeoJSON
            data={districts}
            style={polygonStyle}
            onEachFeature={onEachDistrictFeature}
          />
        )}

        {layers.culturalSites && culturalSites && (
          <GeoJSON
            data={culturalSites}
            pointToLayer={culturalMarker}
            onEachFeature={onCulturalSite}
          />
        )}

        {layers.busParkings && busParkings && (
          <GeoJSON
            data={busParkings}
            pointToLayer={busMarker}
            onEachFeature={onBusParking}
          />
        )}

        {layers.motorhomeParkings && motorhomeParkings && (
          <GeoJSON
            data={motorhomeParkings}
            pointToLayer={motorhomeMarker}
            onEachFeature={onMotorhomeParking}
          />
        )}
      </MapContainer>
    </div>
  );
};

export default MapView;
