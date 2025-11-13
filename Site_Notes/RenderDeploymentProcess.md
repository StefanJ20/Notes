Firstly, In order to use our websites data and database, we need to install it into python:

    pip install gunicorn uvicorn 'whitenoise[brotli]' dj-database-url pymysql
    pip freeze > requirements.txt

    Add this to serttings.py BEFORE the section on databases:

    import os
    try:
        import pymysql 
        pymysql.install_as_MySQLdb()
    except Exception:
        pass

    also, change DATABASES to something that should look like this:

    DEBUG = 'RENDER' not in os.environ

    host = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
    ALLOWED_HOSTS = ['localhost', '127.0.0.1'] if DEBUG else ([host] if host else [])
    CSRF_TRUSTED_ORIGINS = [f"https://{host}"] if (not DEBUG and host) else []

    Your environment likely needs cryptography for MySQL authentication, so make sure to install cryptography and freeze requirements.

    python -m pip install --upgrade pip setuptools wheel
    python -m pip install cryptography
    pip freeze > requirements.txt

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.environ["MYSQL_DATABASE"],
            "USER": os.environ["MYSQL_USER"],   
            "PASSWORD": os.environ["MYSQL_PASSWORD"],
            "HOST": os.environ.get("MYSQL_HOST", "mysql"),
            "PORT": os.environ.get("MYSQL_PORT", "3306"),
            "OPTIONS": {"charset": "utf8mb4"},
        }
    }

    Also, add the secret key in settings.py:

    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-not-secret")

    Add these categories to the MIDDLEWARE:

    # settings.py
        MIDDLEWARE = [
            "django.middleware.security.SecurityMiddleware",
            "whitenoise.middleware.WhiteNoiseMiddleware",
        ]

        if not DEBUG:
            STATIC_ROOT = BASE_DIR / "staticfiles"
            STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

    For a custom domain after you've started your server, do:

    extra_host = os.environ.get("EXTRA_ALLOWED_HOST")  # set this to your custom domain
    if not DEBUG and extra_host:
        ALLOWED_HOSTS.append(extra_host)
        CSRF_TRUSTED_ORIGINS.append(f"https://{extra_host}")


    Make sure to update your MySQL Schema in order to be able to create a service user, a user that interacts with other real users to save their data.
    
    CREATE DATABASE IF NOT EXISTS BackendForums CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;        

    CREATE USER IF NOT EXISTS 'backendforums'@'%' IDENTIFIED BY 'StrongRandomPassword';

    GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, INDEX, DROP, REFERENCES
    ON BackendForums.* TO 'backendforums'@'%';
    FLUSH PRIVILEGES;

    SHOW GRANTS FOR 'backendforums'@'%';   -- sanity check

    Make sure to create an .env file after installing dotenv from python with `pip install python-dotenv`

    # Django
    SECRET_KEY=dev-only-not-secret

    # MySQL (local)
    MYSQL_DATABASE=BackendForums
    MYSQL_USER=root            # or your local app user
    MYSQL_PASSWORD=thePassword # your local MySQL password
    MYSQL_HOST=127.0.0.1       # use TCP; avoids socket issues
    MYSQL_PORT=3306

    After this, on Render > Environment, make sure the info looks like this:

        SECRET_KEY      = <StrongRandomString>
        MYSQL_HOST      = mysql 
        MYSQL_PORT      = 3306
        MYSQL_DATABASE  = BackendForums
        MYSQL_USER      = backendforums
        MYSQL_PASSWORD  = StrongRandomPassword
        WEB_CONCURRENCY = 4              # optional



In order to deploy a Web Application, We first need to install the dependencies on the server through a build.sh file:

    set -o errexit

    pip install -r requirements.txt
    python manage.py collectstatic --no-input
    python manage.py migrate

    make the file executeable with:

        chmod +x build.sh

Ready to start, use Render start command on the home page in Render:

    python -m gunicorn <project_module>.asgi:application -k uvicorn.workers.UvicornWorker

Then via the Render Shell, create a new superuser:

    After first deploy, run python manage.py createsuperuser in Render Shell once.

    Optional sanity: run python manage.py check --deploy and fix any warnings.  





