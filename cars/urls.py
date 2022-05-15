from django.urls import path
from cars import views

app_name = 'cars'

urlpatterns = [
    path('review/', views.review, name='review'),
    path('thanks/', views.thank_you, name='ty')
]