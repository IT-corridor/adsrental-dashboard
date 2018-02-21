from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import handler404, handler500

from adsrental.views.errors import Error404View, Error500View

admin.site.site_header = 'Adsrental Administration'

urlpatterns = [
    url(r'^app/admin_tools/', include('admin_tools.urls')),
    # url(r'^admin/', admin.site.urls),
    url(r'^', include('adsrental.urls')),
    url(r'^app/admin/', admin.site.urls),
    url(r'^app/', include('adsrental.urls')),
]

handler404 = Error404View.as_view()  # noqa: F811
handler500 = Error500View.as_view()  # noqa: F811
