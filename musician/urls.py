from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.AddMusician.as_view(), name='add_musician'),
    path('update/<int:id>/', views.MusicianEditView.as_view(), name='edit_musician')
]
