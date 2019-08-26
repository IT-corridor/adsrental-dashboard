import os

from django.core.wsgi import get_wsgi_application
from werkzeug.debug import DebuggedApplication

from config.environment import SETTINGS_MODULE

os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE)
application = get_wsgi_application()  # pylint: disable=C0103
application = DebuggedApplication(application, evalex=True)  # pylint: disable=C0103
