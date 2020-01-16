from django.urls import path
from api_app import views
urlpatterns = [
    path('quizes/',views.QuizView.as_view,name='quisez')

]




