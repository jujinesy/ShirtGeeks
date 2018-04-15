import django
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog, set_language
from django.contrib.auth.views import LoginView, LogoutView



from menus.views import HomeView, AllUserRecentItemListView
from profiles.views import ProfileFollowToggle, RegisterView, activate_user_view

non_translatable_urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^i18n/$', set_language, name='set_language'),
    # DEBUG FALSE에서 정적파일 쓰고싶으면 python manage.py runserver --insecure
# 또는 아래 처럼

    # url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root':settings.STATIC_ROOT}),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

translatable_urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^recent/$', AllUserRecentItemListView.as_view(), name='recent'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name='activate'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^profile-follow/$', ProfileFollowToggle.as_view(), name='follow'),
    url(r'^u/', include('profiles.urls', namespace='profiles')),
    url(r'^items/', include('menus.urls', namespace='menus')),
    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    ]

urlpatterns = non_translatable_urlpatterns + i18n_patterns(
    *translatable_urlpatterns)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
