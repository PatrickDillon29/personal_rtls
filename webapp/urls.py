from django.urls import path

from . import views

app_name = 'webapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('live_data/', views.live_data, name='live_data'),
    path('hist_data/', views.hist_data, name='hist_data'),
    path('hist_data/<int:requested_id>/', views.get_tag_data, name='hist_tag_data'),
    path('tag_config/', views.tag_config, name='tag_config'),
    path('move_transactions/', views.move_transactions, name='move_transactions'),
    path('demo_mode', views.demo_mode, name='demo_mode'),
    path('conveyor_config', views.conveyor_config, name='conveyor_config')
]