from django.urls import path

from .views import CustomTokenRefreshView, LoginView, LogoutView, RegisterView

urlpatterns = [
    path("register", RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
    # path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"), - встроенный, ответ не соответствует образцу
    path("token/refresh", CustomTokenRefreshView.as_view(), name="token_refresh"),
    path("logout", LogoutView.as_view(), name="logout"),
]
