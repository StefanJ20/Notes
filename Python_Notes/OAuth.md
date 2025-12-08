# OAuth #

OAuth is a provider of authentication endpoints for a website that allows major providers to be connected and used as those endpoints for your web service.
We have to first install the required packages for OAuth with the command: `pip install django-allauth`
We have to update the installed apps in settings.py to include AllAuth and its providers we desire:

```python

INSTALLED_APPS = [

    "django.contrib.sites",  # REQUIRED by allauth
    
    "allauth",
    "allauth.account",      # email/password auth
    "allauth.socialaccount",  # social auth base

    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.github",
]

```

We also have to make sure to set a site ID with `SITE_ID = 1` in settings.py.
We also need to add authentication backends in settings.py.

```python

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",  # default
    "allauth.account.auth_backends.AuthenticationBackend",  # allauth
]

```
We dont have to, but we can make our own login / logout urls:
```python
LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
```
# url patterns in the admins url Dir #

```python
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),  # <--- important
]
```

# create credentials in provider console #

For Google as an example:
    - Go to Google Cloud Console.
    - Create a project (if you don’t have one).
    - Go to APIs & Services → Credentials → Create Credentials → OAuth Client ID.
    - Choose Web application.
    Set Authorized redirect URI to your callback URL.

# Run migrations and create superuser #

`python manage.py migrate`
`python manage.py createsuperuser`

# Start your server #

Redirect to the admin url, you'll now see:

    - Sites
    - Social accounts
    - Social applications (from allauth)

# Open Sites → yoursite.com #

    - Change domain & name to match your local / prod domain, e.g.:
    - Domain: localhost:8000
    - Name: Localhost

# Go to Social applications → Add. #
    - Provider: Google
    - Name: Google OAuth
    - Client id: <paste from Google console>
    - Secret key: <paste from Google console>
    Add your site to the Chosen sites box.

    Now Google login is saved.