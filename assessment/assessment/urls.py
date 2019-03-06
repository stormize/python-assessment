from django.contrib import admin
from . import views
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
app_name="assessment"
urlpatterns = [
    path('signup/', views.signUp,name="signUp"),
    path('signin/', views.signIn,name="signIn"),
    path('signout/',views.signOut,name="signOut"),
    path('welcome/',views.welcome,name="welcome"),
    path('admin', admin.site.urls), 
    path('app/', include('myapp.urls')),
    #path('', include('django.contrib.auth.urls')),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='registeration/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registeration/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registeration/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registeration/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)