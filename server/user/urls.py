from django.urls import path

from user.views import FavouriteProductView, RemoveFromFavourites, RecentProductView, SignUp, Login, SignOut, UserView

app_name = 'user'
urlpatterns = [
    path('signup/v0/', SignUp.as_view(), name='signup-v0'),
    path('login/v0/', Login.as_view(), name='login-v0'),
    path('signout/v0/', SignOut.as_view(), name='signout-v0'),
    path('me/v0/', UserView.as_view(), name='user-info-v0'),
    path('favourites/v0/', FavouriteProductView.as_view(), name='user-favourites-v0'),
    path('favourites/<product_id>/v0/', RemoveFromFavourites.as_view(), name='remove-from-favourites-v0'),
    path('recents/v0/', RecentProductView.as_view(), name='user-recent-v0'),
]