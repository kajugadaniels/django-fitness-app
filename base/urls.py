from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('services/', views.services, name='services'),
    path('services/personalized-workout/', views.personalized_workout, name='personalized_workout'),
    path('exercise/body-part/<str:body_part>/', views.personalized_workout, name='exercise_list_by_body_part'),
    path('exercise/equipment-tool/<str:equipment_tool>/', views.personalized_workout, name='exercise_list_by_equipment_tool'),
    path('exercise/<int:exercise_id>/', views.show_single_exercise, name='show_single_exercise'),
    path('services/eat-smart', views.eatSmart, name='eatSmart'),

    path('trainers/', views.trainers, name='trainers'),
    path('contact/', views.contact, name='contact'),
    path('join-community/', views.joinCommunity, name='joinCommunity'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
