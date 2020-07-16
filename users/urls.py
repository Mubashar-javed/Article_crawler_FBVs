from users.views import registration
from django.urls import path
# we are just using the Django BuiltIn view like LoginView and Logout view.
# Even we don't need to specify any view for them.
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'user'  # app name for this app.
urlpatterns = [
    path('', registration, name='register'),
    # for class-base-view/CBV we use the attribute as_view()
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

]
