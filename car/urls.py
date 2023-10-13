from django.urls import path

from .views import *

urlpatterns = [
    path('', CarHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('bmw/<slug:bmw>/', categories),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post')


]