from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wishme/<str:name>", views.wishme, name="wishme"),
    path("add/<int:num1>/<int:num2>", views.add, name="addition"),
    path("sayhello", views.sayhello, name="sayhello"),
    path("employee", views.employee, name="employee"),
    path("time", views.current_time, name="current_time"),
    path("home", views.home, name="home"),
    path('signup', views.signup, name='signup'), # Add this
    path('customized_crispy/', views.customized_crispy_signup, name='customized_crispy_signup'),
    path('thanks/', views.thanksView, name='thanks'), 
    path('students/', views.studentsView, name='students'), 
    path('add-student/', views.studentsAddView, name='add-student'), 
    path('edit-student/<int:id>', views.studentsEditView, name='edit-student'), 
    path('students/delete/<int:id>', views.studentsDeleteView, name='students_delete'), 

     path('departments/', views.departmentsView, name='departments'), 
    path('add-department/', views.departmentAddView, name='add-department'), 


    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),


]
