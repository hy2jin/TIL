from django.urls import path
from . import views

# namespace
app_name = 'articles'
urlpatterns = [
    # articles/로 요청이 들어왔을 때, index view 함수 실행, pattern_name = index
    path('', views.index, name='index'),
    # GET, POST 다르게 작동
    path('create/', views.create, name='create'),
    # variable routing -> url converter : int, str, slug, uuid...
    # 특정값을 지정할 수 있는 unique 값은? --> Primary Key -> integer
    # <값 정의 : 변수명>/
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
]
