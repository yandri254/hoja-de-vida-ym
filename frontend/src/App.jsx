import React, { useState, useEffect } from 'react';
import axios from 'axios';
import html2pdf from 'html2pdf.js';
import Sidebar from './components/Sidebar';
import MainContent from './components/MainContent';
import './App.css';

function App() {
  const [cvData, setCvData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [activeSection, setActiveSection] = useState('home');
  const [isPrinting, setIsPrinting] = useState(false);

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

  const handleDownloadPDF = (mode) => {
    const generatePDF = (filenameSuffix) => {
      const element = document.querySelector('.resume-layout');
      const sanitizedName = `CV_${cvData.datos_personales.nombres}_${cvData.datos_personales.apellidos}`.replace(/[^a-z0-9]/gi, '_').toLowerCase();
      const filename = `${sanitizedName}_${filenameSuffix}.pdf`;

      const opt = {
        margin: 0,
        filename: filename,
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2, useCORS: true },
        jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
      };

      return html2pdf().set(opt).from(element).save(filename).then(() => {
        if (mode === 'full') setIsPrinting(false);
        if (mode !== 'full') {
          const el = document.querySelector('.resume-layout');
          if (el) el.classList.remove('pdf-section-mode');
        }
      });
    };

    if (mode === 'full') {
      setIsPrinting(true);
      // Wait for the state to update and DOM to render all sections
      setTimeout(() => {
        generatePDF('completo');
      }, 800);
    } else {
      // Download current view immediately
      // Add temporary class for styling
      const element = document.querySelector('.resume-layout');
      element.classList.add('pdf-section-mode');

      generatePDF(activeSection);

      // Remove class after a short delay to ensure capture is done
      // Note: html2pdf is async, but we don't have a promise returned from generatePDF here easily without refactoring.
      // However, html2pdf().save() returns a promise. Let's update generatePDF to return it.
    }
  };

  if (loading) return <div className="loading">Cargando...</div>;
  if (error) return <div className="error">{error}</div>;
  if (!cvData) return <div>No hay datos disponibles.</div>;

  return (
    <div className="app-container">
      <div className={`resume-layout ${isPrinting ? 'print-mode' : ''}`}>
        <Sidebar
          datos={cvData.datos_personales}
          referencias={cvData.referencias}
          activeSection={activeSection}
          setActiveSection={setActiveSection}
          onDownloadPDF={handleDownloadPDF}
          isPrinting={isPrinting}
        />
        <MainContent
          datos={cvData.datos_personales}
          formacion={cvData.formacion}
          experiencia={cvData.experiencia}
          referencias={cvData.referencias}
          activeSection={activeSection}
          isPrinting={isPrinting}
        />
      </div>
    </div>
  );
}

export default App;
