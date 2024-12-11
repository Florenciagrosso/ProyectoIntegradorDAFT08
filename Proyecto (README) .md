<img src="https://github.com/Florenciagrosso/ProyectoIntegradorDAFT08/blob/main/Assets/Banner.png?raw=true">



# Wings of the East: Optimizando la Operación de una Aerolínea  
**"La aerolínea que conecta Oriente con el mundo. Nuestro compromiso es brindar una experiencia de vuelo premium, fusionando comodidad y excelencia en cada trayecto."**  

**Lema:** *“Descubre Oriente. Vuela con Wings of the East.”*

---

## **Descripción del Proyecto**  

### **Contexto**  
Wings of the East, una aerolínea reconocida por conectar Oriente con el resto del mundo, enfrenta serios desafíos operativos debido a altos niveles de retrasos en sus vuelos. Estos retrasos afectan negativamente tanto la experiencia de los clientes como la eficiencia operativa, ocasionando:  
- **Reducción de la satisfacción del cliente:** Impacto directo en la lealtad hacia la marca.  
- **Incremento en costos operativos:** Penalizaciones, combustible adicional y compensaciones elevan los gastos.  
- **Problemas de itinerarios:** Los retrasos tienen un efecto dominó en las operaciones diarias.  

Data Scope, un equipo especializado en análisis y manejo de datos, compuesto por **5 expertos en Data Engineering y Data Analytics**, fue contratado para identificar las causas de estos retrasos y proporcionar insights clave para optimizar las operaciones de la aerolínea.

---

### **Objetivo**  
El principal propósito de este proyecto es realizar un análisis profundo de los retrasos en vuelos para:  
1. **Identificar patrones y causas subyacentes.**  
2. **Ofrecer recomendaciones prácticas para minimizar los retrasos.**  
3. **Ayudar a optimizar la experiencia del cliente y reducir costos operativos.**

---

## **Estructura del Repositorio**  
1. **`Assets/`**  
 - Contiene Imagenes, logos, etc.).  
2. **`data/`**  
   - Contiene los datasets utilizados, tanto en su forma original como procesada. 

3. **`notebooks/`**  
   - Incluye los análisis exploratorios y de limpieza de datos en Jupyter,  Notebooks.  
   Ejemplos:
   -  `Tabla - boardingPasses.ipynb` : Notebook para la limpieza y el análisis de pases de abordar.
   - `Tabla- Tickets.ipynb` : Notebook para  la limpieza y el análisis de tickets.
   - `Tabla- Tickets.ipynb` : Notebook para  la limpieza y el análisis de aeronaves.

4. **`scripts/`**  
   - Código fuente en Python  para procesamiento de datos
   - Subcarpetas:  
     - `Ingesta Automatizada/` - Scripts para análisis de datos.  
     - `visualizations/` - Scripts para creación de gráficos.  

5. **`dashboards/`**  
   - Reportes y dashboards interactivos creados en Power BI.  

6. **`docs/`**  
   - Documentación técnica del proyecto, incluyendo metodología, resultados y conclusiones.  
8. **`Diagramas/`**  
   - Diagrama de Gantt.png: Diagrama de Gantt para la planificación del proyecto.
 - WingsOfTheEastDiagramaER.png: Diagrama de entidad-relación de la base de datos.  
7. **`README.md`**  
   - Explicación general del proyecto y cómo navegar el repositorio.  

---

## **Metodología**  

### **Fase 1: Exploración de Datos**  
- Recopilación de un dataset inicial proporcionado por Wings of the East.  
- Identificación y resolución de problemas en los datos (limpieza de datos).  
- Análisis descriptivo para entender la distribución y características generales del dataset.  

### **Fase 2: Análisis de Retrasos**  
- Identificación de patrones en los retrasos mediante visualizaciones interactivas y estadísticas descriptivas.  
- Exploración de variables como clima, rutas específicas, horarios pico, y más.  

### **Fase 3: Generación de Insights**  
- Uso de **Python** (Pandas, NumPy, Seaborn, Scikit-learn) para modelado predictivo.  
- Creación de dashboards con **Power BI** para comunicar hallazgos a los stakeholders de Wings of the East.  

---

## **Herramientas y Tecnología**  

### **SQL Server**  

<img src="https://clipart.info/images/ccovers/1499955337microsoft-sql-server-logo-png.png" alt="SQL Server" width="120" style="display:inline; margin-left:-0px;"> 

Gestión centralizada y consulta eficiente de grandes volúmenes de datos.  



### **Python**  
<img src="https://logohistory.net/wp-content/uploads/2023/06/Python-Emblem.png" alt="Python" width="120" style="display:inline; margin-left:-20px;"> 

Análisis y modelado de datos utilizando librerías como Pandas, NumPy, Matplotlib, Seaborn, y Scikit-learn.  

### **Power BI**  
<img src="https://logosmarcas.net/wp-content/uploads/2022/02/Power-BI-Emblema.png" alt="Power Bi" width="120" style="display:inline; margin-left:-0px;"> 
Visualización interactiva y creación de reportes ejecutivos.  

### **GIT & GitHub**  
<img src="https://cdn3.iconfinder.com/data/icons/social-media-2169/24/social_media_social_media_logo_git-1024.png" alt="Git" width="80" style="display:inline; margin-left:-0px;"> <img src="https://creazilla-store.fra1.digitaloceanspaces.com/icons/7912097/git-icon-md.png" alt="Git" width="80" style="display:inline; margin-left:-0px;"> 


Colaboración y control de versiones para un desarrollo eficiente.  


---

## **Resultados Esperados**  
- Reducción significativa en los retrasos mediante la implementación de soluciones basadas en datos.  
- Mejora en la satisfacción del cliente y optimización de costos operativos.  
- Dashboards interactivos que permitan a Wings of the East monitorear sus operaciones en tiempo real.  

---

## **Conclusión**  
Este proyecto representa un esfuerzo conjunto entre Wings of the East y Data Scope para enfrentar desafíos operativos críticos utilizando un enfoque basado en datos. Los hallazgos y recomendaciones finales se presentarán en forma de reportes detallados y visualizaciones que permitirán una mejor toma de decisiones estratégicas.  

