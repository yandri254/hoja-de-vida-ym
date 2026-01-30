import React from 'react';

const MainContent = ({ datos, formacion, experiencia, referencias, activeSection, isPrinting }) => {
    if (!datos) return null;

    return (
        <main className="main-content" id="resume-content">
            <header className="main-header">
                <h1 className="name">{datos.nombres} <span className="surname">{datos.apellidos}</span></h1>
                <p className="job-title">{datos.titulo_profesional || 'PERFIL PROFESIONAL'}</p>
                <div className="header-line"></div>
            </header>

            <div className="content-body">
                {(activeSection === 'home' || isPrinting) && datos.perfil && (
                    <section className="content-section fade-in">
                        <h2 className="section-title">
                            <span className="title-icon">📝</span> PERFIL PROFESIONAL
                        </h2>
                        <p className="profile-summary">{datos.perfil}</p>
                    </section>
                )}

                {(activeSection === 'home' || isPrinting) && (
                    <section className="content-section fade-in">
                        <h2 className="section-title">
                            <span className="title-icon">👤</span> DATOS PERSONALES
                        </h2>
                        <div className="personal-details-grid">
                            <div className="detail-box">
                                <span className="label">Cédula</span>
                                <span className="value">{datos.cedula}</span>
                            </div>
                            <div className="detail-box">
                                <span className="label">Nacimiento</span>
                                <span className="value">{datos.fecha_nacimiento}</span>
                            </div>
                            <div className="detail-box">
                                <span className="label">Edad</span>
                                <span className="value">{datos.edad} años</span>
                            </div>
                            <div className="detail-box">
                                <span className="label">Estado Civil</span>
                                <span className="value">{datos.estado_civil}</span>
                            </div>
                        </div>
                    </section>
                )}

                {(activeSection === 'experiencia' || isPrinting) && (
                    <section className="content-section fade-in">
                        <h2 className="section-title">
                            <span className="title-icon">💼</span> EXPERIENCIA LABORAL
                        </h2>
                        <div className="timeline">
                            {experiencia && experiencia.length > 0 ? (
                                experiencia.map((item, index) => (
                                    <div key={index} className="timeline-item">
                                        <div className="timeline-marker"></div>
                                        <div className="timeline-content">
                                            <h3 className="item-role">{item.cargo}</h3>
                                            <div className="item-company">{item.empresa}</div>
                                            <div className="item-period">
                                                {item.fecha_inicio ? `${item.fecha_inicio} - ${item.fecha_fin || 'Presente'}` : ''}
                                            </div>
                                            <p className="item-description">{item.descripcion}</p>
                                        </div>
                                    </div>
                                ))
                            ) : (
                                <p>No hay experiencia registrada.</p>
                            )}
                        </div>
                    </section>
                )}

                {(activeSection === 'formacion' || isPrinting) && (
                    <section className="content-section fade-in">
                        <h2 className="section-title">
                            <span className="title-icon">🎓</span> FORMACIÓN ACADÉMICA
                        </h2>
                        <div className="education-grid">
                            {formacion && formacion.length > 0 ? (
                                formacion.map((item, index) => (
                                    <div key={index} className="education-item">
                                        <h3 className="edu-degree">{item.nivel}</h3>
                                        <div className="edu-institution">{item.institucion}</div>
                                        <div className="edu-status">{item.estado}</div>
                                        {item.titulo && <div className="edu-detail">{item.titulo}</div>}
                                    </div>
                                ))
                            ) : (
                                <p>No hay formación registrada.</p>
                            )}
                        </div>
                    </section>
                )}

                {(activeSection === 'referencias' || isPrinting) && (
                    <section className="content-section fade-in">
                        <h2 className="section-title">
                            <span className="title-icon">👥</span> REFERENCIAS PERSONALES
                        </h2>
                        <div className="references-grid">
                            {referencias && referencias.length > 0 ? (
                                referencias.map((ref, index) => (
                                    <div key={index} className="reference-card">
                                        <div className="ref-name">{ref.nombre}</div>
                                        <div className="ref-info">📞 {ref.telefono}</div>
                                        {ref.email && <div className="ref-info">✉️ {ref.email}</div>}
                                    </div>
                                ))
                            ) : (
                                <p>No hay referencias registradas.</p>
                            )}
                        </div>
                    </section>
                )}
            </div>
        </main>
    );
};

export default MainContent;
