### Grupo05
Integrantes
- Emilia Romero
- Iñaki Goyeneche
- Julia Saenz
# Descripción del proyecto
CIDEPINT es el Centro de Investigación y Desarrollo en Tecnología de Pinturas de Argentina, nacido en los años 70 a partir de una colaboración entre varias instituciones. Su objetivo principal es promover la competitividad de los productos de pintura argentinos a nivel nacional e internacional mediante investigaciones y desarrollos en tecnología de recubrimientos. Además, se dedica a la formación de profesionales especializados y a la creación de normas en la industria. Con el tiempo, ha ampliado sus áreas de enfoque para incluir temas como el tratamiento de aceros, la protección contra la corrosión y soluciones ecológicas. Sus objetivos incluyen investigar, formar recursos humanos, difundir resultados, organizar cursos y colaborar con instituciones afines.

CIDEPINT plantea la necesidad de que exista una plataforma para mostrar y ofrecer los servicios que prestan las diferentes Instituciones.

La aplicación tendrá un aplicación interna de administración (para usuarios y administradores) en Python y Flask, y un portal web en Vue.js que será donde se podrán buscar los servicios ofrecidos por las instituciones registradas. Utilizaremos una base de datos PostgreSQL y se implementarán las API necesarias para las consultas.
# Cómo acceder
**Superusuario**
- Usuario: ```admin@example.com```
- Contraseña: ```Admin123```
### Comandos para base de datos
```flask resetdb```: Elimina y arma los modelos de datos vacios 

```flask seedsdb```: Carga las tablas con datos cargados en la carpeta ```web/seeds```

# Dependencias del Proyecto

### Manejo de Dependencias y Entorno
- [**asdf**](https://asdf-vm.com/): para Sistemas Operativos Linux
- [**venv**](https://docs.python.org/3/library/venv.html): para Sistemas Operativos Windows
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
_Servidor de Base de Datos: Postgres 15_
- [**psycopg2-binary**](https://pypi.org/project/psycopg2-binary/): 2.9.7. Esta biblioteca proporciona soporte para bases de datos PostgreSQL
- [**Flask-SQLAlchemy**](https://flask-sqlalchemy.palletsprojects.com/en/3.x/): 3.1.1. extensión de Flask que simplifica el manejo de bases de datos SQL

### Dependencias de Entorno y Configuración
- [**Python-dotenv**](https://pypi.org/project/python-dotenv/): 1.0.0. cargar variables de entorno y configuraciones desde archivos .env

### Sesiones y Seguridad
- [**Flask-Session**](https://flask-session.readthedocs.io/en/latest/): 0.5.0. manejo de sesiones en aplicaciones web Flask
- [**Flask-Bcrypt**](https://flask-bcrypt.readthedocs.io/en/latest/): 1.0.1. cifrado de contraseñas y la gestión de seguridad
- [**Flask-Mail**](https://pythonhosted.org/Flask-Mail/): 0.9.1. facilita el envío de correos electrónicos desde la aplicación web

# API
### Dependencias
- [**marshmallow**](https://marshmallow.readthedocs.io/en/stable/): 3.20.1. Para la serialización y validación de datos
### Endpoints
#### Autenticación

_Devuelve mensaje de éxito si existe un usuario con esa contraseña registrado en el sistema_
- [ ] Requiere autenticación
- Tipo: _POST_
- Ruta: ```/api/auth```
- Cuerpo:\
    *{\
    "user": "john.doe@mail.com",\
    "password": "QXR0mi38a2"\
    }*
- Ejemplo: ```POST https://admin-grupo05.proyecto2023.unlp.edu.ar/api/auth```
#### Información de las Instituciones

_Obtiene todas las instituciones dadas de alta en el sistema_
- [x] Requiere autenticación
- Tipo: _GET_
- Ruta: ```/api/institutions{?page,per_page}```
    - page ```integer``` (opcional): número de página. **Default 1**
    - per_page```integer``` (opcional): cantidad de elementos por página **Default 1**
- Encabezados: 
    - *Authorization*: *{id del usuario}*
- Ejemplo:```GET https://admin-grupo05.proyecto2023.unlp.edu.ar/api/institutions?page=2&per_page=10```

#### Información de perfil

_Obtiene toda la información del perfil del usuario autenticado._
- [x] Requiere autenticación
- Tipo: _GET_
- Ruta: ```/api/profile```
- Encabezados: 
    - *Authorization*: *{id del usuario}*
- Ejemplo: ```GET https://admin-grupo05.proyecto2023.unlp.edu.ar/api/me/profile```


#### Listado de solicitudes de servicio realizadas por el usuario logueado

_Obtiene el listado de solicitudes realizadas por el usuario autenticado._
- [x] Requiere autenticación
- Tipo: _GET_
- Ruta: ```/api/me/requests{?page,per_page,sort,order}```
    - page ```integer``` (opcional): número de página. **Default 1**
    - per_page```integer``` (opcional): cantidad de elementos por página **Default 1**
    - sort ```text``` (opcional): criterio de ordenación
    - order ```text``` (opcional): Orden DESCENDIENTE o ASCENDENTE **Default desc**
- Encabezados: 
    - *Authorization*: *{id del usuario}*
- Ejemplo: ```GET https://admin-grupo05.proyecto2023.unlp.edu.ar/api/me/requests?page=2&per_page=10&sort=creation_date&order=desc```

#### Obtiene la solicitud de servicio

_Obtiene la solicitud realizada por el usuario autenticado_
- [x] Requiere autenticación
- Tipo: _GET_
- Ruta: ```/api/me/requests/{id}```
    - id ```integer``` (requerido): id de la solicitud de servicio.
- Encabezados: 
    - *Authorization*: *{id del usuario}*
- Ejemplo: ```GET https://admin-grupo05.proyecto2023.unlp.edu.ar/api/me/requests/123```


#### Carga una solicitud de servicio

_Carga una solicitud de servicio por un usuario autenticado_
- [x] Requiere autenticación
- Tipo: _POST_
- Ruta: ```/api/me/requests```
- Encabezados: 
    - *Authorization*: *{id del usuario}*
- Cuerpo: \
{\
  "title": "a title",\
  "description": "a long description"\
}
- Ejemplo:```POST https://admin-grupo05.proyecto2023.unlp.edu.ar/api/me/requests```


#### Carga una nota en solicitud de servicio

_Carga una nota en la solicitud de servicio por un usuario autenticado._
- [x] Requiere autenticación
- Tipo: _POST_
- Ruta: ```/api/me/requests/{id}/notes```
    - id ```integer``` (requerido): Id de la solicitud de servicio
- Encabezados: 
    - *Authorization*: *{id del usuario}*
- Cuerpo: \
{\
  "text": "a long description"\
}
- Ejemplo: ```POST https://admin-grupo05.proyecto2023.unlp.edu.ar/api/me/requests/123/notes```
#### Buscador de servicios

_Obtiene un listado de tipos habilitado, filtrado por el criterio de búsqueda._
- [x] Requiere autenticación
- Tipo: _GET_
- Ruta: ```/api/services/search{?q,type,page,per_page}```
    - q ```string``` (requerido): El término de búsqueda principal
    - type ```string``` (opcional): El tipo de búsqueda
    - page ```integer``` (opcional): Número de página actual
    - per_page ```integer``` (opcional): Cantidad de elementos por página
- Encabezados: 
    - *Authorization*: *{id del usuario}*
- Ejemplo: ```GET https://admin-grupo05.proyecto2023.unlp.edu.ar/api/services/search?q=&type=&page=2&per_page=10```


#### Obtener servicio

_Obtiene el detalle del servicio._
- [ ] Requiere autenticación
- Tipo: _GET_
- Ruta: ```/api/services/{id}```
    - id ```integer``` (requerido): Id del servicio
- Ejemplo:```GET https://admin-grupo05.proyecto2023.unlp.edu.ar/api/services/123```

#### Tipos de servicios

_Obtiene el listado de tipos de servicios._
- [ ] Requiere autenticación
- Tipo: _GET_
- Ruta: ```/api/services-types```
- Ejemplo: 
```GET https://admin-grupo05.proyecto2023.unlp.edu.ar/api/services-types```

# Estructura
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
- `.env.example`: Contiene las siguientes variables de entorno necesarias para funcionar de forma local:
    - puerto de la app Vue para la redireccion en desarrollo. Por defecto, es el puerto **5173**, pero debe setearla con su puerto correspondiente.
    - agregar variables para la conexión con la base de datos
