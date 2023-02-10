from django.urls import path

from studentApp import views

urlpatterns = [
   path('', views.login_fun, name='log'),
   path('logdata',views.logdata_fun),# it will  data and check as supruser and redirect to home.html page

   path('reg',views.reg_fun,name ='reg'),  #it will redirect to register.html page
   path('regdata',views.regdata_fun), # it will create a superuser account

   path('home', views.home_fun,name='home'),   # it will redirect to home.html

   path('add_students',views.addstudent_fun,name='add'),  # it will redirect to addstudent
   path('readdata',views.readdata_fun), #it will insert record into student table

   path('display',views.display_fun,name='display'),  # it will display student table data, in  display.html file

   path('Update/<int:id>',views.update_fun,name='Update'), #it will update student record
   path('Delete/<int:id>',views.delete_fun,name='Delete'),
   path('log_out',views.log_out_fun,name="log_out")

 ]

