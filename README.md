ProgrAmando - Plataforma de Cursos de Programación

Video DEMO: https://drive.google.com/file/d/1Ij_NTVnRS2-tKFLAtXYXuNHVRGX3sV6P/view?usp=sharing

ProgrAmando una aplicación web construida con **Django** que permite a los usuarios registrarse, iniciar sesión y acceder a cursos sobre programación.

Características

- Registro y login de usuarios
- Edición de perfil (nombre, apellido y avatar)
- Visualización de cursos disponibles
- Solo los administradores pueden crear nuevos cursos
- Uso de vistas basadas en clases (CBV) y funciones (FBV)
- Plantillas heredadas con `base.html`
- Autenticación y autorización
- Carga de imágenes para el avatar de usuario

Tecnologías utilizadas

- Python 3.13
- Django 5.2.4
- Bootstrap 5
- HTML5, CSS3

Estructura principal

web-cursos/
├── cursos/
│ ├── models.py
│ ├── views.py
│ ├── templates/cursos/
├── inicio/
│ ├── views.py
│ ├── templates/inicio/
│ │ ├── inicio.html
│ │ └── about.html
├── usuarios/
│ ├── views.py
│ ├── forms.py
│ ├── templates/usuarios/
├── templates/
│ └── base.html
├── static/
│ └── css/
└── manage.py

Roles

- **Usuarios**: pueden visualizar cursos, editar su perfil y cargar un avatar.
- **Administradores**: además de lo anterior, pueden crear nuevos cursos desde el panel correspondiente.


