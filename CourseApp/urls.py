from django.urls import path
from . import views

urlpatterns = [
    path('create-course/', views.create_course),
    path('delete-course/<int:course_id>/', views.delete_course),
    path('update-course/', views.update_course),
    path('get-course/<int:course_id>/', views.get_course),
    path('get-all-courses/', views.get_all_courses),
]