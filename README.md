# Transformación de la industria manufacturera en Argentina (2016 - 2026)

Proyecto de Prácticas Profesionalizantes I — 2.º cuatrimestre 2026 — Equipo 1.

## Integrantes del equipo
- Delia Torres — Comunicadora del equipo / Documentadora
- Fátima Albornoz — Analista de datos
- Vanina Chávez — Diseñadora de visualizaciones / Documentadora
- Tomás Roa — Coordinador de recursos

Responsable de calidad de datos: todo el equipo.

---

## Descripción del proyecto

Este proyecto analiza la evolución de la industria manufacturera argentina entre enero de 2016 y julio de 2026 a partir del Índice de Producción Industrial manufacturero (IPI) del INDEC. Se busca describir cómo cambió la producción en ese período y qué diferencias se observan entre las distintas ramas de actividad, dentro de la línea de trabajo "Reconfiguración de la industria argentina" propuesta por la cátedra.

---

## Fuente de datos

- **Fuente:** INDEC — Índice de Producción Industrial manufacturero (IPI), base 2004 = 100. Obtenido de la API de Series de Tiempo de datos.gob.ar (dataset 453).
- **Tipo de datos:** indicadores económicos, series de tiempo mensuales.
- **Dataset:** `data/raw/ipi_manufacturero_indec_2016_2026.csv` — 127 registros (enero 2016 a julio 2026) y 20 variables: fecha, IPI general (serie original, desestacionalizada y tendencia-ciclo) y 16 ramas manufactureras.

---

## Objetivos del análisis

**Objetivo general**
- Describir la evolución de la industria manufacturera argentina entre 2016 y julio de 2026 y las diferencias entre sus ramas.

**Objetivos específicos**
- Identificar períodos de expansión y contracción de la actividad.
- Comparar el comportamiento de las distintas ramas manufactureras.
- Identificar las ramas con mayores crecimientos y contracciones.

---

## Herramientas utilizadas

- Google Sheets / Excel / CSV
- Python (numpy, pandas, matplotlib)
- Power BI (visualización, Sprint 3)
- Google Drive, Trello, GitHub, Google Meet

---

## Proceso de análisis

**Sprint 1 — Planificación y análisis inicial (28/09/2026 al 04/10/2026)**
- Organización del equipo, roles y diagrama de Gantt.
- Ficha de conocimiento del dominio.
- Diccionario de datos.
- Análisis exploratorio inicial (EDA).
- Formulación de 10 preguntas de análisis y selección de 3.

**Próximos sprints**
- Sprint 2: limpieza, transformación, patrones e insights.
- Sprint 3: visualización, narrativa con datos y presentación final.

---

## Resultados principales

En desarrollo. Primeras observaciones del EDA inicial:
- El dataset contiene 127 registros mensuales entre enero de 2016 y julio de 2026.
- No se encontraron valores nulos ni registros duplicados.
- Las variables presentan diferentes rangos, niveles de dispersión y formas de distribución según la rama industrial.
- Se identificaron valores potencialmente atípicos en algunas variables, que no necesariamente representan errores.
- El ipi_general presenta fluctuaciones a lo largo del período, con una caída marcada en 2020 y niveles más bajos desde 2024.
- Las distintas ramas industriales muestran comportamientos diferentes, aspecto que puede profundizarse en el Sprint 2.

---

## Visualizaciones

Se incorporarán a medida que avance el análisis (carpeta `analysis/`).

---

## Conclusiones

Se completarán al cierre del proyecto.

---

## Archivos del proyecto

- `data/raw/` → datos originales
- `data/processed/` → datos preparados o transformados (Sprint 2)
- `analysis/` → archivos de análisis (notebooks, .pbix, consultas)
- `docs/` → documentación del proyecto (fichas, diccionario, Gantt, minutas)
- `reports/` → informes y presentaciones

Documentación completa en el Google Drive del equipo. Gestión de tareas en Trello.

---

## Contacto
(opcional)
