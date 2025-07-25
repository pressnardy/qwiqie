from django.urls import path
from . import views

app_name = 'escorts'


urlpatterns = [
    path('', views.index, name='index'),
    path('female/filters', views.female_filters, name='female_filters'),
    path('filters/location/', views.filter_location, name='filter_location'),
    path('filter_service/<str:service_name>', views.filter_service, name='filter_service'),
    path('gender', views.filter_gender, name='filter_gender'),
    path('females', views.get_females, name='females'),
    path('view/<str:phone_number>', views.view_escort, name="view_escort"),
    path('create/', views.create_escort, name='create_escort'),
    path('<str:phone_number>/delete/', views.delete_escort, name='delete_escort'),
    path('<str:phone_number>/profile/', views.profile, name='profile'),
    path('<str:phone_number>/edit/', views.edit_escort_details, name='edit_details'),
    path('<str:phone_number>/add-service/', views.add_service, name='add_service'),
    path('<str:phone_number>/<int:service_id>/remove-service/', views.remove_service, name='remove_service'),
    path('<str:phone_number>/add-image/', views.add_image, name='add_image'),
    path('<str:phone_number>/<int:image_id>/remove-image/', views.remove_image, name='remove_image'),
]

