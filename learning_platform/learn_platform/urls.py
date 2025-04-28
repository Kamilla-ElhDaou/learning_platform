from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from users import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls', namespace='courses')),
    path(
        'auth/registration/',
        views.UserCreateView.as_view(),
        name='registration',
    ),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('pages.urls', namespace='pages')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
