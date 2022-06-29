from django.urls import path

from user.views import SignUp, Login, SignOut, UserInfo

app_name = 'user'
urlpatterns = [
    path('signup/v0/', SignUp.as_view(), name='signup-v0'),
    path('login/v0/', Login.as_view(), name='login-v0'),
    path('signout/v0/', SignOut.as_view(), name='signout-v0'),
    path('me/v0/', UserInfo.as_view(), name='user-info-v0'),
]