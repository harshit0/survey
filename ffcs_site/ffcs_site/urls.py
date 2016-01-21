"""ffcs_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from form.views import InitialView, ProjectView, AcademicView,PersonalView, ThanksView
urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^initial/$', InitialView),
	url(r'^step2/$',ProjectView),
	url(r'^step3/$',AcademicView),
	url(r'^info/$',PersonalView),
	url(r'^thank/$',ThanksView),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
