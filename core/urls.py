from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    
    
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # URL de Logout: Usa a View generica e redireciona (LOGIN_REDIRECT_URL no settings)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', views.PatientListView.as_view(), name='dashboard'),
    path('pacientes/novo/', views.PatientCreateView.as_view(), name='novo_paciente'),
    path('pacientes/<int:pk>/', views.PatientDetailView.as_view(), name='detalhe_paciente'),
    path('pacientes/<int:pk>/editar/', views.PatientUpdateView.as_view(), name='editar_paciente'),
    path('pacientes/<int:pk>/deletar/', views.PatientDeleteView.as_view(), name='deletar_paciente'),
    path('register/', views.MedicoRegistrationView.as_view(), name='register_medico'),
    path('pacientes/<int:pk>/upload_foto/', views.PhotoUploadView.as_view(), name='upload_foto'),
    path('pacientes/<int:pk>/upload_pdf/', views.PDFUploadView.as_view(), name='upload_pdf'),
]
