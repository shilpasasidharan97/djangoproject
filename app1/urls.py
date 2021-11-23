from django.urls import path
from . import views


app_name= 'app1'

urlpatterns = [
    path('hello',views.hello),
    path('',views.index,name='home'),
    path('htmlpage',views.html,name='html'),
    path('csspage',views.css,name='css'),
    path('jspage',views.java,name='js'),
]