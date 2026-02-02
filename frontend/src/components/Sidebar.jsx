import React from 'react';

const Sidebar = ({ datos, referencias, activeSection, setActiveSection, onDownloadPDF, isPrinting }) => {
  if (!datos) return null;

  const menuItems = [
    { id: 'home', label: 'INICIO', icon: '🏠' },
    { id: 'experiencia', label: 'EXPERIENCIA', icon: '💼' },
    { id: 'formacion', label: 'FORMACIÓN', icon: '🎓' },
    { id: 'referencias', label: 'REFERENCIAS', icon: '👥' },
  ];

  return (
    <aside className="sidebar">
      <div className="profile-container">
        <div className="profile-img-wrapper">
          <img
            src={datos.imagen ? datos.imagen : "/static/assets/perfil.png"}
            alt="Profile"
            className="profile-img"
            onError={(e) => { e.target.src = 'https://via.placeholder.com/150'; }}
          />
        </div>

        <nav className="sidebar-menu">
          {menuItems.map((item) => (
            <button
              key={item.id}
              className={`menu-button ${activeSection === item.id ? 'active' : ''}`}
              onClick={() => setActiveSection(item.id)}
            >
              <span className="menu-icon">{item.icon}</span>
              {item.label}
            </button>
          ))}
        </nav>

        {!isPrinting && (
          <div className="pdf-buttons">
            <button className="pdf-button" onClick={() => onDownloadPDF('full')}>
              <span className="icon">📥</span> CV COMPLETO
            </button>
            <button className="pdf-button" onClick={() => onDownloadPDF('section')}>
              <span className="icon">📄</span> SOLO SECCIÓN
            </button>
          </div>
        )}
      </div>

      <div className="sidebar-section contact-section">
        <h2 className="sidebar-title">CONTACTO</h2>
        <div className="contact-list">
          <div className="contact-item">
            <span className="icon">📞</span>
            <div className="contact-text">
              <span className="value">{datos.telefono}</span>
            </div>
          </div>
          <div className="contact-item">
            <span className="icon">✉️</span>
            <div className="contact-text">
              <span className="value">{datos.email}</span>
            </div>
          </div>
          <div className="contact-item">
            <span className="icon">📍</span>
            <div className="contact-text">
              <span className="value">{datos.direccion}</span>
            </div>
          </div>
        </div>
      </div>
    </aside>
  );
};

export default Sidebar;
