# Industria manufacturera argentina 2022–2025, ¿recuperación o rebote?

**Inteligencia de Datos para la Reconfiguración Industrial Argentina**
Proyecto de Prácticas Profesionalizantes I — 2.º cuatrimestre 2026 — Politécnico Malvinas Argentinas — Equipo 1.

## Integrantes y roles (Sprint 3)

- Fátima Albornoz — Comunicadora del equipo
- Vanina Chávez — Analista de datos
- Delia Torres — Documentadora y encargada de la entrega
- Tomás Roa — Responsable de calidad de datos y seguimiento del Trello

Diseño de visualizaciones, coordinación de recursos y entrega final se asumen en conjunto.

---

## Pregunta del proyecto

En 2025 la industria manufacturera argentina volvió a crecer después de la caída de 2023–2024. ¿Se recuperó realmente o solo dejó de caer?

Período de estudio 2022–2025. Se toma 2022 como año de referencia porque es el último año completo antes de la contracción y ya sin el efecto de la pandemia.

Preguntas de análisis
1. ¿La producción manufacturera recuperó en 2025 los niveles de 2022?
2. ¿Cómo evolucionaron las distintas ramas manufactureras?
3. ¿La recuperación productiva estuvo acompañada por el empleo industrial y cómo evolucionó el comercio exterior?

---

## Fuentes de datos

- **INDEC** — Índice de Producción Industrial manufacturero (IPI), general y por ramas, serie original y desestacionalizada.
- **SIPA** — Empleo industrial registrado (asalariados de la industria manufacturera).
- **INDEC, Intercambio Comercial Argentino (ICA)** — Importaciones por uso económico y exportaciones por grandes rubros.
- **INDEC** — Índice de cantidades exportadas de manufacturas de origen industrial (anual).

Los datos de 2025 son provisorios.

## Datasets

| Archivo | Contenido |
|---|---|
| `data/processed/dataset_unificado.csv` | 126 meses (ene-2016 a jun-2026) y 33 variables: IPI general y por rama, empleo industrial e intercambio comercial |
| `data/processed/exportaciones_MOI_cantidades_anual_2022_2025.csv` | Índice anual de cantidades exportadas de manufacturas de origen industrial |
| `data/raw/` | Datos originales descargados de cada fuente |

El tablero de Power BI lee los dos CSV directamente desde este repositorio, así que se puede abrir y actualizar en cualquier computadora sin cambiar rutas.

---

## Herramientas utilizadas

- Python (pandas) para la limpieza y unión de los datos
- Power BI para el análisis y el tablero interactivo
- Canva para la presentación
- Google Drive, Trello, diagrama de Gantt, GitHub, Google Meet y WhatsApp para la organización del equipo

---

## Proceso de trabajo

**Sprint 1 — Planificación y análisis inicial (28/09 al 04/10)**
Organización del equipo, roles, Gantt, ficha de conocimiento del dominio, diccionario de datos, análisis exploratorio inicial y selección de preguntas.

**Sprint 2 — Preparación y análisis (05/10 al 25/10)**
Limpieza y unión de los datasets de IPI, empleo e intercambio comercial, cálculo de variaciones e índices base 2022, primeras visualizaciones e insights.

**Sprint 3 — Visualización y narrativa (26/10 al 01/11)**
Tablero final en Power BI, presentación en Canva, guion de la exposición, selección de insights, informe técnico y video de la exposición.

---

## Resultados principales

- **La recuperación fue parcial.** La producción cayó 11,5 % entre 2022 y 2024. En 2025 creció 1,9 %, pero quedó 9,8 % por debajo de 2022 (IPI desestacionalizado, promedios anuales).
- **La recuperación fue desigual entre ramas.** 12 de las 16 ramas crecieron entre 2024 y 2025, pero solo 2 superaron sus niveles de 2022 (otro equipo de transporte y refinación del petróleo).
- **El empleo no acompañó.** El empleo industrial bajó 1,8 % en 2025 frente a 2024 y quedó apenas por debajo de 2022.
- **El comercio exterior también fue desigual.** Las importaciones de bienes de consumo y de capital subieron más de 50 % en 2025, mientras que los bienes intermedios siguen 19 % por debajo de 2022. En exportaciones, combustibles y energía quedó 30,5 % por encima de 2022 y las manufacturas de origen industrial apenas 1,5 %.

---

## Visualizaciones

Tablero de Power BI en `reports/PowerBI/` (versión final `PP1-S2-Visualizaciones_Generales_V8.pbix`):
- Portada y preguntas, con navegación por botones
- P1 · Evolución de la producción
- P2 · Recuperación por rama
- P3 · Producción, empleo y comercio
- P3 · Comercio por rubros
- P3 · Exportaciones, valor y cantidad

Las versiones anteriores (V1 a V7) quedan como respaldo en la misma carpeta y en el Drive del equipo.

---

## Conclusión

El crecimiento de 2025 no alcanza para hablar de recuperación. Mirando desde 2022, la industria todavía no recuperó lo que perdió, la mejora se concentró en pocas ramas y el empleo no la acompañó. Un único porcentaje de crecimiento no muestra estas diferencias, por eso importa con qué año se compara y qué pasa dentro de cada indicador.

---

## Archivos del proyecto

- `data/raw/` → datos originales
- `data/processed/` → datos limpios y unificados
- `analysis/` → notebooks de análisis exploratorio
- `reports/PowerBI/` → tablero de Power BI (todas las versiones)
- `docs/` → documentación del proyecto

La documentación completa (diccionario de datos, bitácora, minutas, Gantt, informe técnico y guion) está en el Google Drive del equipo. La gestión de tareas se hizo en Trello.
