# Grupo05
Integrantes
- Emilia Romero
- Iñaki Goyeneche
- Julia Saenz

# Entrega Etapa 1
**Superusuario**
- admin@example.com
- admin123
## Estructura
`admin`: aplicación interna de CIDEPINT
- `flask-session`: configuración de sesiones para flask
- `src/`
    - `core/`: código fuente principal de la aplicación Flask
        - `api/`: código relacionado a la API
        - `common/`: funciones y configuraciones compartidas en la aplicación. Contiene decoradores, serializers y validaciones del lado del servidor
        - `controllers/`: los controladores reciben las peticiones de los usuarios, se comunican con el modelo y actualizan las vistas 
        - `models/`: definición de los modelos de datos con SQLAlchemy
    - `web/`: código relacionado a la aplicación web
        - `helpers/`: funcionalidades auxiliares de la aplicación web. Contiene funciones para el parseo de datos y el chequeo de sesiones
        - `routes/`: definición de las URL de la apliación, manejo de las solicitudes HTTP y comportamiento de la aplicación
        - `seeds/`: código para cargar datos iniciales en la base de datos 
        - `templates/`: páginas de html creadas con jinja para visualizar la aplicación web
            - `components/`: componentes o plantillas reutilizables o expandibles
            - `modules/`: plantillas para los diferentes modulos de la aplicación
            - `pages/`: las páginas individuales de la aplicación 
            - `layout.html`: layout principal del que extienden las páginas.
- `static/`: archivos estáticos usados del lado del cliente
    - `assets/`: logo de la aplicación
    - `css/`: archivos CSS
    - `js/`: funciones de Javascript para la funcionalidad del lado del cliente. Muestra de información y validaciones del lado del cliente
- `app.py`: Punto de entrada principal de la aplicación Flask

## Dependencias del Proyecto

### Manejo de Dependencias y Entorno
- [**Poetry**](https://python-poetry.org/): 1.6.1.

### Framework y Herramientas de Desarrollo
- [**Python**](https://www.python.org/downloads/release/python-3810/): 3.8.10.
- [**Flask**](https://flask.palletsprojects.com/en/2.2.x/): 2.2.3. 
- [**Werkzeug**](https://werkzeug.palletsprojects.com/en/2.3.x/): 2.3.7. biblioteca WSGI para Python. Manejo de solicitudes y respuestas HTTP
- **PEP8**: PEP 8 (Python Enhancement Proposal 8) la guía de estilo de código para Python

### Plantillas y Frontend
- [**Jinja**](https://jinja.palletsprojects.com/) Motor de plantillas utilizado en el proyecto para renderizar contenido dinámico en las páginas web
- [**Bootstrap**](https://getbootstrap.com/): framework de diseño y estilos CSS

### Dependencias de Bases de Datos
- [**psycopg2-binary**](https://pypi.org/project/psycopg2-binary/): 2.9.7. Esta biblioteca proporciona soporte para bases de datos PostgreSQL
- [**Flask-SQLAlchemy**](https://flask-sqlalchemy.palletsprojects.com/en/3.x/): 3.1.1. extensión de Flask que simplifica el manejo de bases de datos SQL

### Dependencias de Entorno y Configuración
- [**Python-dotenv**](https://pypi.org/project/python-dotenv/): 1.0.0. cargar variables de entorno y configuraciones desde archivos .env

### Sesiones y Seguridad
- [**Flask-Session**](https://flask-session.readthedocs.io/en/latest/): 0.5.0. manejo de sesiones en aplicaciones web Flask
- [**Flask-Bcrypt**](https://flask-bcrypt.readthedocs.io/en/latest/): 1.0.1. cifrado de contraseñas y la gestión de seguridad
- [**Flask-Mail**](https://pythonhosted.org/Flask-Mail/): 0.9.1. facilita el envío de correos electrónicos desde la aplicación web

