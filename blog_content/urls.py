from django.urls import path
from .views import Homepage
from .views import About
from .views import Details, NewPost

urlpatterns = [
    path('post/<int:pk>/', Details.as_view(), name='content'),

    path('', Homepage.as_view(), name='homepage'),
    path('about/', About.as_view(), name = 'about'),
    path('post/new_post/', NewPost.as_view(), name='post_new')
]