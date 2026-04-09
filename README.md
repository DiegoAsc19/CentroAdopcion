CentroAdopcion/
├── venv/                   # Entorno virtual (librerías instaladas)
├── static/                 # Archivos estáticos
│   ├── style.css           # Estilos CSS de tu catálogo y formularios
│   └── images/              # (Opcional) Fotos de los perritos
├── templates/              # Plantillas HTML (Jinja2)
│   ├── catalogo.html       # Página principal con el historial
│   └── confirmacion.html   # Formulario de adopción
├── config.py               # Credenciales de MariaDB (Host, User, Pass)
├── database.py             # Lógica de consultas SQL y conexiones
├── models.py               # Clases de Python (Dog, Person)
├── routes.py               # Archivo principal que corre Flask
└── README.md               # Documentación que acabamos de crear
# 🐾 Centro de Adopción de Mascotas "Huellitas"

¡Bienvenido al sistema de gestión de adopciones "Huellitas"! Este proyecto es una aplicación web dinámica diseñada para conectar perritos rescatados con nuevos hogares. Permite gestionar el catálogo de mascotas, realizar procesos de adopción seguros y visualizar un historial de transacciones en tiempo real.

---

## 📖 Descripción del Proyecto

Este sistema resuelve la necesidad de un centro de rescate para automatizar sus procesos. A diferencia de un sitio estático, "Huellitas" utiliza una base de datos relacional para asegurar que cada adopción sea única y que el historial se actualice automáticamente sin intervención manual.

### ¿Cómo funciona para el usuario?
1. **Exploración:** El usuario entra a la página principal y ve una cuadrícula de tarjetas con los perritos disponibles (nombre, raza y edad).
2. **Selección:** Al hacer clic en "¡Quiero Adoptarlo!", el sistema lo dirige a un formulario personalizado para la mascota elegida.
3. **Registro:** El usuario completa sus datos (Nombre, Apellido, Cédula, Dirección).
4. **Confirmación:** Al enviar, el sistema realiza una transacción: guarda al adoptante, crea el registro de adopción y oculta al perro del catálogo.
5. **Historial:** El usuario puede desplegar el menú inferior para confirmar que su adopción se registró correctamente en la lista pública.

---

## 🛠️ Tecnologías Utilizadas

El proyecto emplea un "stack" moderno enfocado en la eficiencia y la estabilidad:

* **Backend:** `Python 3.12` con el micro-framework `Flask`.
* **Base de Datos:** `MariaDB / MySQL` para el almacenamiento relacional de datos.
* **Frontend:** `HTML5`, `CSS3` (utilizando variables y Flexbox para diseño responsivo) y `Jinja2` como motor de plantillas.
* **Servidor:** Entorno de desarrollo local sobre `Ubuntu Linux`.
* **Conectividad:** `mysql-connector-python` para la comunicación fluida entre el código y los datos.

---

## 🗄️ Estructura de la Base de Datos

El sistema se basa en un modelo relacional de tres tablas principales:

* **Dog:** Almacena la información de las mascotas y su estado de disponibilidad (`adopted`).
* **Adopter:** Guarda la información personal de los ciudadanos interesados.
* **Adoption:** Tabla intermedia que vincula perros y personas, registrando la fecha exacta mediante `TIMESTAMP`.

---

## 🚀 Instalación y Configuración

Sigue estos pasos para replicar el entorno en tu máquina local:

### 1. Preparar el Entorno
Asegúrate de estar en tu terminal (se recomienda Fish o Bash en Ubuntu):
```bash
# Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate.fish

# Instalar dependencias
pip install flask mysql-connector-python
