from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from . import views


urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/signup/', views.SignUpView.as_view(), name='sign-up'),
    path('api/notes/', views.NoteListView.as_view(), name='notes'),
    path('api/note-create/', views.NoteCreateView.as_view(), name='note-create'),
    path('api/notes/<int:pk>', views.NoteDetailView.as_view(), name='note-detail'),
]

