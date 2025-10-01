from django.urls import include, path
from mysite.admin import admin_site


urlpatterns = [
    path('admin/', admin_site.urls),
    path('accounts/', include("accounts.urls")),
    path('polls/', include("polls.urls")),
    path('contacts/', include("contacts.urls"))
]
