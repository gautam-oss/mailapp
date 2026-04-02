from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("app.accounts.urls")),
    path("mail/", include("app.mailer.urls")),
    path("", RedirectView.as_view(url="/mail/compose/", permanent=False)),
]