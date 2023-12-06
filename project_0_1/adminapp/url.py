
from django.urls import path,include
from . import views

urlpatterns = [
    path('useradmin/',views.adminpage,name='tablepage'),
    path('edit/<id>',views.editpage,name='editpage'),
    path('delete/<id>',views.delete_record,name='delete_record'),
    path('adduser/',views.adduser,name='adduser'),

    

]
