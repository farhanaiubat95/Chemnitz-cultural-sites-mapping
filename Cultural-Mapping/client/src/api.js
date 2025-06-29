// src/api.js
import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
});

export const fetchBusParkings = async () => {
  const res = await fetch(`${BASE_URL}/bus-parkings/`);
  return await res.json();
};

export const fetchMotorhomeParkings = async () => {
  const res = await fetch(`${BASE_URL}/motorhome-parkings/`);
  return await res.json();
};

export const fetchCulturalSites = async () => {
  const res = await fetch(`${BASE_URL}/cultural-sites/`);
  return await res.json();
};

export const fetchAdministrativeDistricts = async () => {
  const res = await fetch(`${BASE_URL}/administrative-districts/`);
  return await res.json();
};

export default api;