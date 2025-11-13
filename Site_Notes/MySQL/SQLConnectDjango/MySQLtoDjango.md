// In order to fully connect our django database to MySQL client, we have to 
// make sure were within the virtual environment, install xcode tools
// using the command 'xcode-select --install'
// If SQL client isnt already installed, install it with 'brew install mysql pkg-config'
// make sure the python environment also has the sqlclient 'pip install mysqlclient'

// Go to your django site and configure the Database settings to fit MySQL standards:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'FirstDatabase',
            'USER': 'root',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

// Make sure all regions are correctly inputted otherwise 'python3 manage.py migrate' wont work.

// After, since were tranfserring databases, were gonna have to create a new superuser via the Django
// admin panel. After that, you should see your databse details in both MySQL shell and on the Admin dashboard
// within django. 
