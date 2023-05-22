from django.urls import path
from .views import CategoryAPIView, CategoryDetailAPIView, QuestionAPIView, QuestionDetailAPIView, QuestionFilterAPIView

urlpatterns = [
    path('categories/', CategoryAPIView.as_view(), name='category-list'),
    path('categories/<int:category_id>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('questions/', QuestionAPIView.as_view(), name='question-list'),
    path('questions/<int:question_id>/', QuestionDetailAPIView.as_view(), name='question-detail'),
    path('filter/<int:category>/', QuestionFilterAPIView.as_view(), name='question-filter'),
]
