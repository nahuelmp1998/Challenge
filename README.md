# Challenge

## Requirements

- Python 3.0 or bigger
- Dependencies at`requirements.txt`

## Instalación y Ejecución

1. Clone the repository:

   ```bash
   git clone https://github.com/tu_usuario/nombre_del_repositorio.git
   cd nombre_del_repositorio

2. Create the virtual enviorement
    ```bash
    python -m venv venv

3. Activate the virtual enviorement
    * For Windows
        ```bash
        venv\Scripts\activate
    * For MacOs/Linux
        ```bash
        source venv/bin/activate
4. Instalar las dependencias:
    ```bash
        pip install -r requirements.txt
5. Execute the application:
    ```bash
        uvicorn main:app --reload
