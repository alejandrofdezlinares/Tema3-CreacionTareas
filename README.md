Permite a los usuarios gestionar, organizar y realizar el seguimiento de sus tareas pendientes de forma sencilla y eficiente. A través de una interfaz interactiva y modular, la plataforma facilita la creación de nuevos ítems, la actualización de sus estados de avance y el almacenamiento persistente de la información mediante una base de datos integrada.

📊 Análisis de la Estructura del Proyecto

A partir de la inspección de los archivos incluidos en el repositorio, se identifica la siguiente arquitectura:

```text
Tema3-CreacionTareas/
├── gestion_tareas/              # Módulo de configuración principal de Django
│   ├── settings.py              # Configuración global del proyecto
│   ├── urls.py                  # Enrutamiento global de URLs
│   ├── asgi.py                  # Configuración ASGI para ejecución asíncrona
│   └── wsgi.py                  # Configuración WSGI para despliegue en servidor web
├── tareas/                      # Aplicación principal de gestión de tareas
│   ├── admin.py                 # Registro de modelos en el panel de administración
│   ├── apps.py                  # Configuración de la aplicación 'tareas'
│   ├── models.py                # Definición de los modelos de datos de tareas
│   ├── views.py                 # Vistas para manejar la lógica de la aplicación
│   ├── tests.py                 # Pruebas unitarias de la aplicación
│   ├── fixtures/
│   │   └── copia_de_seguridad.json # Datos iniciales/respaldo en formato JSON
│   └── migrations/              # Historial de migraciones de la base de datos
│       └── 0001_initial.py
├── manage.py                    # Script de línea de comandos de Django
├── seed.py                      # Script personalizado para la carga/poblado de datos
├── db.sqlite3                   # Base de datos SQLite local
└── .gitignore                   # Archivo para ignorar archivos no deseados en Git
