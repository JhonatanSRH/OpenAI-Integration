# OpenAI Integration

Este es un proyecto web desarrollado con FastAPI, con el proposito de integrarse via API a servicios de OpenAI.

## Requisitos

- Python 3.9+
- FastAPI
- SQLAlchemy
- SQLmodel
- Pytest
- Uvicorn

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/api_chatbot.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd api_chatbot
    ```
3. Crea un entorno virtual:
    ```bash
    python -m venv env
    ```
4. Activa el entorno virtual:
    - En Windows:
        ```bash
        .\env\Scripts\activate
        ```
    - En Unix o MacOS:
        ```bash
        source env/bin/activate
        ```
5. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Inicia el servidor de desarrollo:
    ```bash
    uvicorn main:app --reload
    ```
2. En el navegador busca la ruta `http://127.0.0.1:8000` para ver la aplicación en funcionamiento.

## Estructura del Proyecto

```
.
├── app
│   ├── main.py
│   ├── config
│   │   ├── settings.py
│   │   └── db.py
│   ├── crud
│   │   └── user.py
│   ├── models
│   │   ├── messages.py
│   │   └── user.py
│   ├── routers
│   │   └── user.py
│   └── schemas
│       └── user.py
├── tests
│   └── test_user.py
├── .gitignore
├── requirements.txt
└── README.md
```
