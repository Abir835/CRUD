from first_app import views
from django.urls import path

app_name = "first_app"
urlpatterns = [
    path('', views.Index, name='index'),
    path('student_form/', views.Student_Form, name='student_form'),
    path('student_info/<int:student_id>/', views.StudentInfo, name='student_info'),
    path('student_update/<int:student_id>/', views.StudentUpdate, name='student_update'),
    path('student_delete/<int:student_id>/', views.StudentDelete, name='student_delete'),
]
