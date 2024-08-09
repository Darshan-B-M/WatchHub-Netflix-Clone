from django.urls import path
from .views import Home, ProfileList,ProfileCreate,Watch,ShowMovieDetail,ShowMovie

app_name = 'core'

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('profile/', ProfileList.as_view(), name='profilelist'),
    path('profile/create/',ProfileCreate.as_view(),name="profile_Create"),
    path('watch/<str:profile_id>/',Watch.as_view(),name='watch'),
    path('movie/detail/<str:movie_id>/',ShowMovieDetail.as_view(),name='show_det'),
    path('play/<uuid:movie_id>/', ShowMovie.as_view(), name='play'), 

]
