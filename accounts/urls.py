from django.urls import path
from . views import home, login_page, register_page, profile, logout_page, forget_password, verify_otp, reset_password

urlpatterns = [
    path('', home , name="home"),
    path('register/', register_page , name="register_page"),
    path('login/', login_page , name="login_page"),
    path('logout/', logout_page , name="logout_page"),
    path('dashboard/profile/', profile, name="profile"),
    
    path('forget-password/', forget_password , name='forget_password'),
    path('verify-otp/', verify_otp, name='verify_otp'),
    path('reset-password/', reset_password, name='reset_password'),
]
