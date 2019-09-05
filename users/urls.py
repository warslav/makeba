from django.urls import path

from .views import SignUpView, PersonalAreaView, ChangeUserView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<int:pk>/personal/', PersonalAreaView.as_view(), name='home'),
    path('<int:pk>/change/', ChangeUserView.as_view(), name='change_user'),
]
