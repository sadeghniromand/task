from django.urls import path
from . import views

app_name = 'comment'
urlpatterns = [
    path('create/<int:pk>', views.CreateCommentView.as_view(), name='create_comment'),
]
