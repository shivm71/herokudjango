from django.urls import path
from . import views

app_name = 'ride'

urlpatterns = [

    path('book/', views.Book.as_view(), name='book'),
    
]


#     # ex: /polls/5/
#     path('all/', views.all, name='get_all_slot'),
#     # ex: /polls/5/results/
#     path('booked/', views.booked, name='get_booked_slot'),
#     path('rpark/', views.randp, name='rand_park'),
#     # ex: /polls/5/vote/
#     path('available/', views.available, name='get_available_slot'),
#     path('park/<int:pk>', views.park, name='park'),
#     path('unpark/<int:pk>', views.unpark, name='unpark'),
#     path('slot_info', views.slot_info, name='slot_info'),
#     path('vehicle_info', views.vehicle_info, name='vehicle_info'),
# ]