import React from 'react';

const MainContent = ({ 
    datos, 
    formacion, 
    experiencia, 
    referencias, 
    reconocimientos,
    cursos,
    productosAcademicos,
    productosLaborales,
    ventasGarage,
    activeSection, 
    isPrinting 
}) => {
    if (!datos) return null;

    // Función para calcular edad
    const calcularEdad = (fechaNacimiento) => {
        if (!fechaNacimiento) return null;
        const hoy = new Date();
        const nacimiento = new Date(fechaNacimiento);
        let edad = hoy.getFullYear() - nacimiento.getFullYear();
        const mes = hoy.getMonth() - nacimiento.getMonth();
        if (mes < 0 || (mes === 0 && hoy.getDate() < nacimiento.getDate())) {
            edad--;
        }
        return edad;
    };

    return (
        <main className="main-content" id="resume-content">
            <header className="main-header">
                <h1 className="name">{datos.nombres} <span className="surname">{datos.apellidos}</span></h1>
                <p className="job-title">{datos.titulo_profesional || 'PERFIL PROFESIONAL'}</p>
                <div className="header-line"></div>
            </header>

            <div className="content-body">
                {/* PERFIL PROFESIONAL */}
                {(activeSection === 'home' || isPrinting) && datos.mostrar_perfil && (
                    <section className="content-section fade-in">
                        <h2 className="section-title">
                            <span className="title-icon">📝</span> PERFIL PROFESIONAL
                        </h2>
                        <p className="profile-description">{datos.perfil}</p>
                    </section>
                )}

                {/* DATOS PERSONALES */}
                {(activeSection === 'home' || isPrinting) && (
                    <section className="content-section fade-in">
                        <h2 className="section-title">
                            <span className="title-icon">👤</span> DATOS PERSONALES
                        </h2>
                        <div className="personal-details-grid">
                            {datos.numero_cedula && (
                                <div className="detail-box">
                                    <span className="label">Cédula</span>
                                    <span className="value">{datos.numero_cedula}</span>
                                </div>
                            )}
                            {datos.fecha_nacimiento && (
                                <div className="detail-box">
                                    <span className="label">Nacimiento</span>
                                    <span className="value">{datos.fecha_nacimiento}</span>
                                </div>
                            )}
                            {datos.fecha_nacimiento && (
                                <div className="detail-box">
                                    <span className="label">Edad</span>
                                    <span className="value">{calcularEdad(datos.fecha_nacimiento)} años</span>
                                </div>
                            )}
                            {datos.estado_civil && (
                                <div className="detail-box">
                                    <span className="label">Estado Civil</span>
                                    <span className="value">{datos.estado_civil}</span>
                                </div>
                            )}
                            {datos.nacionalidad && (
                                <div className="detail-box">
                                    <span className="label">Nacionalidad</span>
                                    <span className="value">{datos.nacionalidad}</span>
                                </div>
                            )}
                            {datos.lugar_nacimiento && (
                                <div className="detail-box">
                                    <span className="label">Lugar de Nacimiento</span>
                                    <span className="value">{datos.lugar_nacimiento}</span>
                                </div>
                            )}
                            {datos.sexo && (
                                <div className="detail-box">
                                    <span className="label">Sexo</span>
                                    <span className="value">{datos.sexo === 'H' ? 'Masculino' : 'Femenino'}</span>
                                </div>
                            )}
                            {datos.licencia_conducir && (
                                <div className="detail-box">
                                    <span className="label">Licencia</span>
                                    <span className="value">{datos.licencia_conducir}</span>
                                </div>
                            )}
                        </div>
                    </section>
                )}

                {/* EXPERIENCIA LABORAL */}
                {(activeSection === 'experiencia' || isPrinting) && datos.mostrar_experiencia && (
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
                                            <h3 className="item-role">{item.cargo_desempenado}</h3>
                                            <div className="item-company">{item.nombre_empresa}</div>
                                            {item.lugar_empresa && (
                                                <div className="item-location">📍 {item.lugar_empresa}</div>
                                            )}
                                            <div className="item-period">
                                                {item.fecha_inicio_gestion ? `${item.fecha_inicio_gestion} - ${item.fecha_fin_gestion || 'Presente'}` : ''}
                                            </div>
                                            {item.descripcion_funciones && (
                                                <p className="item-description">{item.descripcion_funciones}</p>
                                            )}
                                            {item.email_empresa && (
                                                <div className="item-contact">✉️ {item.email_empresa}</div>
                                            )}
                                            {item.sitio_web_empresa && (
                                                <div className="item-contact">🌐 {item.sitio_web_empresa}</div>
                                            )}
                                        </div>
                                    </div>
                                ))
                            ) : (
                                <p>No hay experiencia registrada.</p>
                            )}
                        </div>
                    </section>
                )}

                {/* FORMACIÓN ACADÉMICA */}
                {(activeSection === 'formacion' || isPrinting) && datos.mostrar_formacion && (
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

                {/* RECONOCIMIENTOS */}
                {(activeSection === 'reconocimientos' || isPrinting) && datos.mostrar_reconocimientos && (
                    <section className="content-section fade-in">
                        <h2 className="section-title">
                            <span className="title-icon">🏆</span> RECONOCIMIENTOS
                        </h2>
                        <div className="timeline">
                            {reconocimientos && reconocimientos.length > 0 ? (
                                reconocimientos.map((item, index) => (
                                    <div key={index} className="timeline-item">
                                        <div className="timeline-marker"></div>
                                        <div className="timeline-content">
                                            <h3 className="item-role">{item.descripcion_reconocimiento}</h3>
                                            <div className="item-type">
                                                <span className={`badge badge-${item.tipo_reconocimiento.toLowerCase()}`}>
                                                    {item.tipo_reconocimiento}
                                                </span>
                                            </div>
                                            {item.entidad_patrocinadora && (
                                                <div className="item-company">{item.entidad_patrocinadora}</div>
                                            )}
                                            {item.fecha_reconocimiento && (
                                                <div className="item-period">📅 {item.fecha_reconocimiento}</div>
                                            )}
                                            {item.nombre_contacto_auspicia && (
                                                <div className="item-contact">👤 {item.nombre_contacto_auspicia}</div>
                                            )}
                                            {item.telefono_contacto_auspicia && (
                                                <div className="item-contact">📞 {item.telefono_contacto_auspicia}</div>
                                            )}
                                        </div>
                                    </div>
                                ))
                            ) : (
                                <p>No hay reconocimientos registrados.</p>
                            )}
                        </div>
                    </section>
                )}

                {/* CURSOS REALIZADOS */}
                {(activeSection === 'cursos' || isPrinting) && datos.mostrar_cursos && (
                    <section className="content-section fade-in">
                        <h2 className="section-title">
                            <span className="title-icon">📚</span> CURSOS REALIZADOS
                        </h2>
                        <div className="courses-grid">
                            {cursos && cursos.length > 0 ? (
                                cursos.map((item, index) => (
                                    <div key={index} className="course-card">
                                        <h3 className="course-name">{item.nombre_curso}</h3>
                                        {item.entidad_patrocinadora && (
                                            <div className="course-institution">🏛️ {item.entidad_patrocinadora}</div>
                                        )}
                                        {item.total_horas && (
                                            <div className="course-hours">⏱️ {item.total_horas} horas</div>
                                        )}
                                        <div className="course-period">
                                            {item.fecha_inicio && `${item.fecha_inicio} - ${item.fecha_fin || 'En curso'}`}
                                        </div>
                                        {item.descripcion_curso && (
                                            <p className="course-description">{item.descripcion_curso}</p>
                                        )}
                                    </div>
                                ))
                            ) : (
                                <p>No hay cursos registrados.</p>
                            )}
                        </div>
                    </section>
                )}

                {/* PRODUCTOS ACADÉMICOS Y LABORALES */}
                {(activeSection === 'productos' || isPrinting) && (datos.mostrar_productos_academicos || datos.mostrar_productos_laborales) && (
                    <>
                        {datos.mostrar_productos_academicos && (
                            <section className="content-section fade-in">
                                <h2 className="section-title">
                                    <span className="title-icon">🎓</span> PRODUCTOS ACADÉMICOS
                                </h2>
                                <div className="products-grid">
                                    {productosAcademicos && productosAcademicos.length > 0 ? (
                                        productosAcademicos.map((item, index) => (
                                            <div key={index} className="product-card">
                                                <h3 className="product-name">{item.nombre_recurso}</h3>
                                                {item.clasificador && (
                                                    <div className="product-category">
                                                        <span className="badge">{item.clasificador}</span>
                                                    </div>
                                                )}
                                                {item.descripcion && (
                                                    <p className="product-description">{item.descripcion}</p>
                                                )}
                                            </div>
                                        ))
                                    ) : (
                                        <p>No hay productos académicos registrados.</p>
                                    )}
                                </div>
                            </section>
                        )}

                        {datos.mostrar_productos_laborales && (
                            <section className="content-section fade-in">
                                <h2 className="section-title">
                                    <span className="title-icon">💼</span> PRODUCTOS LABORALES
                                </h2>
                                <div className="products-grid">
                                    {productosLaborales && productosLaborales.length > 0 ? (
                                        productosLaborales.map((item, index) => (
                                            <div key={index} className="product-card">
                                                <h3 className="product-name">{item.nombre_producto}</h3>
                                                {item.fecha_producto && (
                                                    <div className="product-date">📅 {item.fecha_producto}</div>
                                                )}
                                                {item.descripcion && (
                                                    <p className="product-description">{item.descripcion}</p>
                                                )}
                                            </div>
                                        ))
                                    ) : (
                                        <p>No hay productos laborales registrados.</p>
                                    )}
                                </div>
                            </section>
                        )}
                    </>
                )}

                {/* VENTA GARAGE */}
                {(activeSection === 'garage' || isPrinting) && datos.mostrar_venta_garage && (
                    <section className="content-section fade-in">
                        <h2 className="section-title">
                            <span className="title-icon">🏷️</span> VENTA GARAGE
                        </h2>
                        <div className="garage-grid">
                            {ventasGarage && ventasGarage.length > 0 ? (
                                ventasGarage.map((item, index) => (
                                    <div key={index} className="garage-card">
                                        <h3 className="garage-name">{item.nombre_producto}</h3>
                                        <div className="garage-state">
                                            <span className={`badge badge-${item.estado_producto.toLowerCase()}`}>
                                                {item.estado_producto}
                                            </span>
                                        </div>
                                        {item.valor_del_bien && (
                                            <div className="garage-price">${item.valor_del_bien}</div>
                                        )}
                                        {item.descripcion && (
                                            <p className="garage-description">{item.descripcion}</p>
                                        )}
                                    </div>
                                ))
                            ) : (
                                <p>No hay productos en venta.</p>
                            )}
                        </div>
                    </section>
                )}

                {/* REFERENCIAS PERSONALES */}
                {(activeSection === 'referencias' || isPrinting) && datos.mostrar_referencias && (
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
