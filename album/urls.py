from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.AlbumCreateView.as_view(), name='add_album'),
    path('update/<int:id>/', views.AlbumEditView.as_view(), name='edit_album'),
    path('delete/<int:pk>/', views.AlbumDeleteView.as_view(), name='delete_album')
]
