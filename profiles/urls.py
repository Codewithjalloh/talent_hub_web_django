from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('portfolio/add/', views.add_portfolio_item, name='add_portfolio_item'),
    path('portfolio/<int:pk>/edit/', views.edit_portfolio_item, name='edit_portfolio_item'),
    path('portfolio/<int:pk>/delete/', views.delete_portfolio_item, name='delete_portfolio_item'),
    path('browse/', views.browse_talents, name='browse_talents'),
    path('view/<int:pk>/', views.view_profile, name='view_profile'),
] 