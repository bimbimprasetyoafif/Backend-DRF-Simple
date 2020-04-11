from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import FilmList, FilmDetail,GambarList, GambarDetail, FileUploadView

urlpatterns = [
    path('film', FilmList.as_view()),
    path('film/<int:pk>', FilmDetail.as_view()),
    path('gambar/upload', FileUploadView.as_view()),
    path('gambar', GambarList.as_view()),
    path('gambar/<int:pk>', GambarDetail.as_view()),
]