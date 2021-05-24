from django.urls import path
from .views import quizHome, CheckAns, checkScore, testPlay, Login, Logout, Intro, regFeedback
urlpatterns = [
    path('', Intro, name=""),
    path('quiz-home', quizHome, name="quiz-home"),
    path('checkans', CheckAns, name="checkans"),
    path('login', Login, name="login"),
    path('test-playground/<int:id>', testPlay, name="test-playground"),
    path('test-result', checkScore, name="test-result"),
    path('logout', Logout, name='logout'),
    path('feedback', regFeedback, name='feedback')

]