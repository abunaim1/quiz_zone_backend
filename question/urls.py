from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('list', views.QuestionViewSet)
router.register('category', views.QuestionCategoryViewSet)
router.register('question_paper', views.QuestionPaperViewSet)
router.register('answer_option', views.AnswerOptionViewset)
router.register('scriptSubmission', views.ScriptSubmissionViewSet)
urlpatterns = [
    path('', include(router.urls))
]
