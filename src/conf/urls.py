import django
import sys
print (sys.path)

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog, set_language
from django.contrib.auth.views import LoginView, LogoutView

from .account.urls import urlpatterns as account_urls

from menus.views import HomeView, AllUserRecentItemListView
from profiles.views import ProfileFollowToggle, RegisterView, activate_user_view

from machina.app import board
handler404 = 'conf.core.views.handle_404'
handler403 = 'conf.core.views.handle_404'

non_translatable_urlpatterns = [
    url(r'^jesses/', admin.site.urls),
    url(r'^i18n/$', set_language, name='set_language'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

non_translatable_urlpatterns_DEBUG = [
    # DEBUG FALSE에서 정적파일 쓰고싶으면 python manage.py runserver --insecure
    # 또는 아래 처럼
    url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root':settings.STATIC_ROOT}),
]

translatable_urlpatterns = [
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^recent/$', AllUserRecentItemListView.as_view(), name='recent'),
    url(r'^signup/$', RegisterView.as_view(), name='signup'),
    url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name='activate'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^profile-follow/$', ProfileFollowToggle.as_view(), name='follow'),
    url(r'^u/', include('profiles.urls', namespace='profiles')),
    url(r'^items/', include('menus.urls', namespace='menus')),
    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),

    url(r'^account/', include((account_urls, 'account'), namespace='account')),
    # Apps
    url(r'^forum/', include(board.urls)),
    ]

if settings.DEBUG == False and settings.LOCAL == True:
    urlpatterns = non_translatable_urlpatterns + non_translatable_urlpatterns_DEBUG + i18n_patterns(
    *translatable_urlpatterns)
else:
    urlpatterns = non_translatable_urlpatterns + i18n_patterns(
        *translatable_urlpatterns)
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
