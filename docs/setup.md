# Setup instructions

This page instructs software engineers how to get started working with the Django codebase and PostgreSQL database.

## Local setup

1. Ensure you have a working installation of Python 3

2. Set up a virtual environment for the project using e.g. venv or conda
    - Note: The application has been tested with Python **3.8.13**
    - Example:
        ```
            conda create --name seshat38 python=3.8.13
            conda activate seshat38
        ```

3. Create a fork of the GitHub repo with all branches: https://github.com/MajidBenam/seshat

4. Clone your fork to your local machine

5. Ensure you have a working installation of PostgreSQL **version 12**
    - <details><summary>Example instructions for macOS</summary>

        - `brew install postgres@12`
        - `brew services start postgresql@12`
        - Update `~/.zshrc` (or equivalent for your terminal) with:
            ```
                export PATH="/opt/homebrew/opt/postgresql@12/bin:$PATH"
                export LDFLAGS="-L/opt/homebrew/opt/postgresql@12/lib"
                export CPPFLAGS="-I/opt/homebrew/opt/postgresql@12/include"
            ```
        - Open a new terminal
        </details>
    - Check the installation works with `psql postgres` and do `\l` to see Owner username
    - In psql, create a default superuser called "postgres", which is needed to restore the Seshat database from backup:
        ```
            CREATE USER postgres SUPERUSER;
        ```

6. After PostgreSQL is installed, install the Python packages in your environment (some packages have psql as a dependency). From the top level of the `seshat` repo:
    ```
        pip install -r requirements.txt
    ```

7. Restore Seshat database from dump:
    - Note: you'll need a dump file of the Seshat database, which can be provided by one of the current developers
        ```
        createdb -U postgres <seshat_db_name>

        pg_restore -U postgres -d <seshat_db_name> /path/to/file.dump
        ```
    - Connect to the new test database to make sure things are in order
        ```
            psql -U postgres -d <seshat_db_name>
        ```

8. Create a config with your database info for Django

10. Create stuff in settings/base.py

11. `python manage.py runserver`



## Production setup (AWS)

_TODO_