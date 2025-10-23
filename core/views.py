from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Patient, PhotoPatient, PDFPatient
from django.shortcuts import get_object_or_404, redirect
from .forms import PhotoPatientForm, PDFPatientForm, MedicoRegistrationForm

class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = 'core/dashboard.html'
    context_object_name = 'pacientes'

    def get_queryset(self):
        """ FILTRAR OS PACIENTES PARA MOSTRAR APENAS OS DO MÉDICO LOGADO """
        return Patient.objects.filter(medico=self.request.user).order_by('-data_registro')
    
class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    fields = ['nome_completo', 'data_nascimento', 'telefone', 'email', 'historico_medico', 'alergias']
    template_name = 'core/patient_form.html'

    def form_valid(self, form):
        """ SOBRESCREVER O METODO PARA ADICIONAR O MEDICO ANTES DE SALVAR """
        form.instance.medico = self.request.user
        return super().form_valid(form)
    
class PatientDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Patient
    template_name = 'core/detalhe_paciente.html'
    context_object_name = 'paciente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paciente = self.get_object()

        context['fotos'] = paciente.fotos.all()
        context['pdfs'] = paciente.pdfs.all()
        return context
    
    def test_func(self):
        """ GARANTE QUE SÓ O MEDICO QUE CRIOU O PACIENTE PODE VE-LO """
        paciente = self.get_object()
        return paciente.medico == self.request.user
    
class PatientUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Patient
    fields = ['nome_completo', 'data_nascimento', 'telefone', 'email', 'historico_medico', 'alergias']
    template_name = 'core/patient_form.html'

    def test_func(self):
        paciente = self.get_object()
        return paciente.medico == self.request.user

class PatientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Patient
    template_name = 'core/patient_confirm_delete.html'
    success_url = reverse_lazy('dashboard') # Redireciona para o Dashboard após apagar o paciente
    
    def test_func(self):
        paciente = self.get_object()
        return paciente.medico == self.request.user
    
class MediaUploadMixin(LoginRequiredMixin, UserPassesTestMixin):
    def form_valid(self, form):
        paciente = get_object_or_404(Patient, pk=self.kwargs['pk'])
        form.instance.paciente = paciente
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('detalhe_paciente', kwargs={'pk': self.kwargs['pk']})
    
    def test_func(self):
        paciente = get_object_or_404(Patient, pk=self.kwargs['pk'])
        return paciente.medico == self.request.user

class PhotoUploadView(MediaUploadMixin, CreateView):
    model = PhotoPatient
    form_class = PhotoPatientForm
    template_name = 'core/upload_form.html'

class PDFUploadView(MediaUploadMixin, CreateView):
    model = PDFPatient
    form_class = PDFPatientForm
    template_name = 'core/upload_form.html'


class MedicoRegistrationView(CreateView):
    form_class = MedicoRegistrationForm
    template_name = 'core/medico_register.html'
    success_url = reverse_lazy('login')    