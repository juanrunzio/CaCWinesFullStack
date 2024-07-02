# CaCWines

- Correr app y instalar las dependecias necesarias:

  ```bash
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  python app.py
  ```

- Configurar backend:
  - Con postgres funcionando:
    ```bash
    psql
    ```
  - Configurar db:
    ```sql
    CREATE DATABASE cacwine_reviews_db;
    CREATE USER miusuario WITH PASSWORD 'micontraseña';
    GRANT ALL PRIVILEGES ON DATABASE cacwine_reviews_db TO miusuario;
    \c cacwine_reviews_db
    GRANT ALL PRIVILEGES ON SCHEMA public TO miusuario;
    \q
    ```
  - Configurar el codigo con el usuario:
    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://miusuario:micontraseña@localhost/cacwine_reviews_db'
    ```
