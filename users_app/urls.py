from django.conf.urls import url
from users_app.views import users_data,add_user,update

urlpatterns = [
    url('users/', users_data,name='users'),
    url('add/',add_user,name='add_user'),
    url('iou/',update,name='update'),
]