from django.urls import path
from products import views
urlpatterns = [
    path("category/", views.CategoryAPIView.as_view()),
]