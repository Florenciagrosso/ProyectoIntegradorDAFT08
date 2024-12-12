# Sprint 1

## 1. Crear el repositorio público y compartirlo con el equipo

### Descripción:
Para la implementación del proyecto desarrolló un repositorio público en GitHub, donde manejan y detallan cada una de las actividades en el desarrollo del proyecto, junto a la colaboración entre los miembros del equipo. Este repositorio funciona como el espacio de trabajo colaborativo en el que se almacenan cada uno de los recursos necesarios en el proyecto, siendo scripts, visulizaciones y toda la documentación.

Por otro lado, la implementación de control de versiones también es una parte importante dentro de la realización de un trabajo en conjunto. Con GITHUB podemos controlar ese historial de versiones en caso de errores o fallos dentro de cada script subido y modificado.

## 2. Identificar los archivos a usar y armar la estructura de carpetas a usar en el repositorio

### Descripción:

En esta etapa inicial del proyecto, fue crucial realizar una identificación clara y precisa de los archivos de datos que se ibas a implementar para llevar a cabo el análisis y las operaciones de la aerolínea. La correcta identificación y organización de estos archivos permiten un flujo de trabajo eficiente y minimizan el riesgo de errores durante el desarrollo.

Además, se definió una estructura de carpetas en el repositorio que facilitara la colaboración entre los miembros del equipo, organizando los archivos de forma lógica y asegurando que cada sección del proyecto tuviera su propio espacio dentro del repositorio. Este enfoque garantiza que los desarrolladores puedan trabajar en diferentes aspectos del proyecto sin interferencias, manteniendo una separación clara entre scripts, datos, documentación y otros recursos.

## 3. Creación de la Base de Datos

### 3.1 Creación de la Base de Datos

**Descripción:**

La base de datos es el pilar fundamental sobre el cual se desarrolló todo el sistema de análisis de datos para **Wings of the East**. En este proyecto, se optó por usar **SQL Server** como gestor de bases de datos por su robustez y capacidad para manejar grandes volúmenes de datos transaccionales.

El enfoque inicial fue crear una estructura de base de datos que permitiera almacenar de forma eficiente los datos de tiquetes, horarios, vuelos, manteniendo una trazabilidad clara de cada operación realizada en el sistema. Se buscó una arquitectura que permitiera realizar consultas rápidas y eficaces, que brindaran insights útiles para la toma de decisiones.

### 3.2 Identificación de Entidades y Tablas

**Descripción:**

La correcta identificación de las entidades y tablas fue crucial para el éxito del proyecto, ya que esto permitió la creación de un modelo de datos que reflejara con precisión las necesidades operativas y analíticas de **Wings of the East**. Durante este proceso, se analizaron todos los aspectos del negocio, desde ll compra de tiquetes hasta el retraso de los vuelos.

### 3.3 Creación de Tablas y Objetos SQL

**Descripción:**

Una vez definidas las entidades clave, el siguiente paso fue la creación de las tablas en **SQL Server**. Cada tabla fue diseñada para reflejar la estructura de las entidades previamente identificadas. Se aplicaron reglas de normalización para evitar redundancias de datos y asegurar que cada tabla se mantuviera consistente con el modelo de datos establecido.
## Punto 4: Identificar las entidades/tablas a usar en la BD

**Descripción:**

El éxito del proyecto depende en gran medida de la correcta identificación de las entidades y tablas que reflejan las operaciones comerciales de **Wings of the East**. En esta etapa, se llevó a cabo un análisis exhaustivo de los datos proporcionados por la empresa, con el objetivo de modelar el sistema de información a través de una base de datos robusta y eficiente que permitiera gestionar de forma adecuada los datos de los vuelos, horarios, tiquetes y demás.

## Punto 5: Crear las tablas y objetos SQL necesarios

**Descripción:**

Una vez identificadas las entidades principales y las tablas necesarias, el siguiente paso fue implementar estas tablas en la base de datos **SQL Server**. Este proceso incluyó la definición detallada de las columnas de cada tabla, así como la configuración de relaciones mediante claves foráneas, asegurando la integridad referencial de los datos.

## Punto 6: Crear el flujo que importe los datos a la base de datos

**Descripción:**

El proceso de creación del flujo que permita la importación de datos a la base de datos fue una de las etapas clave para garantizar la fiabilidad y la precisión en la gestión de la información dentro de **Wings of the East**. Este flujo de datos fue diseñado para cargar de manera eficiente los tiquetes, vuelos, horarios, entreo otros, permitiendo que la empresa tenga acceso a datos en tiempo real. El enfoque fue asegurar que los datos se procesaran, transformaran y cargaran en la base de datos con la máxima integridad y sin pérdida de información.

## 7. Validar que todos tengan acceso a dicha base de datos y que puedan extraer datos sin problemas

### Descripción:

Una vez establecida la base de datos SQL Server y cargados todos los datos, el siguiente paso clave fue garantizar que todos los miembros del equipo tuvieran acceso sin problemas a dicha base de datos y pudieran extraer los datos requeridos para el análisis en tiempo real.

Se realizaron pruebas de acceso y conectividad con cada miembro del equipo para verificar que todos pudieran interactuar con la base de datos a través de sus propios entornos locales y herramientas. Estas pruebas incluyeron la verificación de los permisos de lectura y escritura, asegurándose de que cada miembro pudiera realizar consultas SQL, extraer datasets, y ejecutar scripts para alimentar el análisis en Python y Power BI sin interrupciones.

Se generaron credenciales personalizadas para cada miembro del equipo, otorgando los permisos necesarios para asegurar que cada uno tuviera los privilegios adecuados para trabajar sobre la base de datos sin comprometer la integridad de la misma.
## 8. Crear el método de automatización de ingesta de datos nuevos

### Acción Realizada:

El equipo de **Wings of the East** implementó un método automatizado para la ingesta de datos nuevos que garantiza la actualización constante de la base de datos sin intervención manual. Este proceso es clave para mantener la integridad y actualidad de los datos en todo momento, asegurando que el sistema refleje la información más reciente, tanto en el análisis de inventarios como en las métricas de costos y los horarios de cada vuelo.

El flujo de automatización se estructuró en varias fases críticas, todas documentadas y validadas:


