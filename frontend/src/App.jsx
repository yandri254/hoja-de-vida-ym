import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Sidebar from './components/Sidebar';
import MainContent from './components/MainContent';
import './App.css';

function App() {
  const [cvData, setCvData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('/api/cv/')
      .then(response => {
        setCvData(response.data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Error fetching CV data:", err);
        setError("No se pudo cargar la información. Asegúrate de que el servidor backend esté corriendo.");
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="loading">Cargando...</div>;
  if (error) return <div className="error">{error}</div>;
  if (!cvData) return <div>No hay datos disponibles.</div>;

  return (
    <div className="container">
      <Sidebar
        datos={cvData.datos_personales}
        referencias={cvData.referencias}
      />
      <MainContent
        datos={cvData.datos_personales}
        formacion={cvData.formacion}
        experiencia={cvData.experiencia}
      />
    </div>
  );
}

export default App;
