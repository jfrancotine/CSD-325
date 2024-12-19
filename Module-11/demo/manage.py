#Jose Franco
#12/18/2024
#Django basics. Web server that will be viewed by your local host (127.0.0.1:8080)

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
    try:
        #Import the Django command-line execution module
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        #Raise an error if Django is not installed or the virtual environment is not activated
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    #Execute the command passed in the system arguments
    execute_from_command_line(sys.argv)

#Entry point of the script; calls the main function when the script is executed
if __name__ == '__main__':
    main()
