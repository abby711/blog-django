from django.urls import path
from blog.views import postlist,postdetail,likeview

app_name="blog"
urlpatterns=[
    path('',postlist.as_view(),name='post-list'),
    path('detail/<int:pk>/',postdetail.as_view(),name='post-detail'),
    path('ajax/likes/',likeview,name='like'),
]
